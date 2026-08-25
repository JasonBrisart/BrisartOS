"""
BrisartOS Boot Sector Emulator / Smoke Test
Pure Python.
No dependencies.
No QEMU, Bochs, VirtualBox, or any external emulator required.

This is a minimal 8086 real-mode interpreter that implements exactly
the instruction subset BrisartOS boot sectors currently use. It loads
a 512-byte boot image at physical address 0x7C00 -- the same address
real BIOS firmware loads a boot sector to -- and executes it exactly
as a CPU would, including BIOS int 0x10 teletype video output.

This does not replace testing on real hardware or a real emulator
before anything is written to a physical disk. It exists so that every
boot sector change can be behaviorally verified offline, in CI, with
nothing installed beyond Python itself, as part of the same
dependency-free philosophy the rest of BrisartOS follows.

Supported opcodes (intentionally small; grows only as real boot code
grows):
    31 /r        XOR r/m16, r16      (register-direct only)
    8E /r        MOV Sreg, r/m16     (register-direct only)
    B8+r imm16   MOV r16, imm16      (not currently emitted, reserved)
    BE imm16     MOV SI, imm16
    AC           LODSB
    84 /r        TEST r/m8, r8       (register-direct only)
    74 rel8      JZ / JE
    B4 imm8      MOV AH, imm8
    CD imm8      INT imm8            (only int 0x10, ah=0x0E supported)
    EB rel8      JMP short
    F4           HLT
"""
from pathlib import Path
import sys

BOOT_LOAD_SEGMENT = 0x0000
BOOT_LOAD_ADDRESS = 0x7C00
IMAGE_SIZE = 512
SIGNATURE = b"\x55\xAA"
MEMORY_SIZE = 0x100000  # 1 MB, matches real-mode addressable memory


class UnsupportedInstruction(Exception):
    pass


class BootSectorCPU:
    """
    A deliberately tiny 8086 real-mode interpreter. It only understands
    the handful of instructions BrisartOS boot sectors currently emit.
    Anything else raises UnsupportedInstruction with the failing
    opcode and address, so a boot sector bug is caught immediately
    instead of silently mis-executing.
    """

    def __init__(self, memory: bytearray):
        self.memory = memory
        self.ax = 0
        self.si = 0
        self.ds = 0
        self.es = 0
        self.cs = 0
        self.ip = BOOT_LOAD_ADDRESS
        self.zero_flag = False
        self.halted = False
        self.output_chars = []
        self.steps = 0

    # -- memory / fetch helpers ------------------------------------

    def _physical(self, segment: int, offset: int) -> int:
        return (segment * 16 + offset) & (MEMORY_SIZE - 1)

    def _fetch8(self) -> int:
        addr = self._physical(self.cs, self.ip)
        value = self.memory[addr]
        self.ip = (self.ip + 1) & 0xFFFF
        return value

    def _fetch16(self) -> int:
        low = self._fetch8()
        high = self._fetch8()
        return (high << 8) | low

    @staticmethod
    def _signed8(value: int) -> int:
        return value - 256 if value >= 128 else value

    # -- register helpers --------------------------------------------

    def _get_reg16(self, code: int) -> int:
        if code == 0b000:  # AX
            return self.ax
        raise UnsupportedInstruction(f"unsupported r16 register code {code:#04b}")

    def _set_sreg(self, code: int, value: int) -> None:
        if code == 0b000:  # ES
            self.es = value
        elif code == 0b011:  # DS
            self.ds = value
        else:
            raise UnsupportedInstruction(f"unsupported segment register code {code:#04b}")

    # -- interrupt handling --------------------------------------------

    def _interrupt(self, vector: int) -> None:
        if vector == 0x10:
            ah = (self.ax >> 8) & 0xFF
            al = self.ax & 0xFF
            if ah == 0x0E:
                # BIOS teletype output: print AL as a character.
                self.output_chars.append(chr(al))
            else:
                raise UnsupportedInstruction(f"unsupported int 0x10 function ah={ah:#04x}")
        else:
            raise UnsupportedInstruction(f"unsupported interrupt {vector:#04x}")

    # -- single instruction step -----------------------------------

    def step(self) -> None:
        start_ip = self.ip
        opcode = self._fetch8()

        if opcode == 0x31:  # XOR r/m16, r16
            modrm = self._fetch8()
            if modrm == 0xC0:  # xor ax, ax
                self.ax = 0
                self.zero_flag = True
            else:
                raise UnsupportedInstruction(f"unsupported XOR modrm {modrm:#04x} at {start_ip:#06x}")

        elif opcode == 0x8E:  # MOV Sreg, r/m16
            modrm = self._fetch8()
            mod = (modrm >> 6) & 0b11
            reg = (modrm >> 3) & 0b111
            rm = modrm & 0b111
            if mod != 0b11:
                raise UnsupportedInstruction(f"unsupported MOV Sreg addressing mode at {start_ip:#06x}")
            self._set_sreg(reg, self._get_reg16(rm))

        elif opcode == 0xBE:  # MOV SI, imm16
            self.si = self._fetch16()

        elif opcode == 0xAC:  # LODSB
            addr = self._physical(self.ds, self.si)
            al = self.memory[addr]
            self.ax = (self.ax & 0xFF00) | al
            self.si = (self.si + 1) & 0xFFFF  # DF assumed 0 (forward)

        elif opcode == 0x84:  # TEST r/m8, r8
            modrm = self._fetch8()
            if modrm == 0xC0:  # test al, al
                al = self.ax & 0xFF
                self.zero_flag = (al == 0)
            else:
                raise UnsupportedInstruction(f"unsupported TEST modrm {modrm:#04x} at {start_ip:#06x}")

        elif opcode == 0x74:  # JZ rel8
            rel = self._signed8(self._fetch8())
            if self.zero_flag:
                self.ip = (self.ip + rel) & 0xFFFF

        elif opcode == 0xB4:  # MOV AH, imm8
            imm = self._fetch8()
            self.ax = (imm << 8) | (self.ax & 0x00FF)

        elif opcode == 0xCD:  # INT imm8
            vector = self._fetch8()
            self._interrupt(vector)

        elif opcode == 0xEB:  # JMP rel8
            rel = self._signed8(self._fetch8())
            self.ip = (self.ip + rel) & 0xFFFF

        elif opcode == 0xF4:  # HLT
            self.halted = True

        else:
            raise UnsupportedInstruction(f"unsupported opcode {opcode:#04x} at {start_ip:#06x}")

    def run(self, max_steps: int = 200_000) -> str:
        while not self.halted:
            self.steps += 1
            if self.steps > max_steps:
                raise RuntimeError(
                    f"boot sector did not HLT within {max_steps} instructions "
                    "(possible infinite loop bug, not the intentional hang-forever HLT loop)"
                )
            self.step()
        return "".join(self.output_chars)


def load_boot_image(path: Path) -> bytearray:
    data = path.read_bytes()
    if len(data) != IMAGE_SIZE:
        raise ValueError(f"expected a {IMAGE_SIZE}-byte boot sector, got {len(data)} bytes")
    if data[-2:] != SIGNATURE:
        raise ValueError(f"missing 0x55AA boot signature, found {data[-2:].hex()}")

    memory = bytearray(MEMORY_SIZE)
    memory[BOOT_LOAD_ADDRESS:BOOT_LOAD_ADDRESS + IMAGE_SIZE] = data
    return memory


def run_boot_image(path: Path, max_steps: int = 200_000) -> str:
    memory = load_boot_image(path)
    cpu = BootSectorCPU(memory)
    return cpu.run(max_steps=max_steps)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python boot_sector_test.py <boot_image_path>")
        return 2

    path = Path(sys.argv[1])
    print()
    print("===================================")
    print(" BrisartOS Boot Sector Smoke Test")
    print("===================================")
    print(f"Image  : {path}")

    try:
        output = run_boot_image(path)
    except (UnsupportedInstruction, ValueError, RuntimeError) as error:
        print(f"Result : FAIL")
        print(f"Reason : {error}")
        print()
        return 1

    print("Result : PASS (CPU reached HLT)")
    print("Captured BIOS int 0x10 teletype output:")
    print("-----------------------------------")
    print(output, end="")
    print("-----------------------------------")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
