"""Build the first BrisartOS boot image using Python only.

This script writes a 512-byte BIOS boot sector image. It does not call an
assembler, compiler, linker, GRUB, Linux build system, or external package.

The boot image is intentionally tiny: it prints a BrisartOS message using BIOS
video interrupt 0x10 and then halts forever.
"""

from pathlib import Path

BOOT_LOAD_ADDRESS = 0x7C00
IMAGE_SIZE = 512
SIGNATURE = b"\x55\xAA"
OUTPUT = Path("build/brisartos_boot.img")

MESSAGE = (
    "BrisartOS PYBOOT 0.1.0-alpha\r\n"
    "Python-made bare-metal boot image\r\n"
    "Local-first. Custom. Offline-capable.\r\n"
)


def rel8(source_after_operand: int, target: int) -> int:
    value = target - source_after_operand
    if not -128 <= value <= 127:
        raise ValueError(f"relative jump out of range: {value}")
    return value & 0xFF


def build_boot_sector() -> bytes:
    code = bytearray()

    # Clear AX, then point DS and ES at segment 0.
    code += b"\x31\xC0"      # xor ax, ax
    code += b"\x8E\xD8"      # mov ds, ax
    code += b"\x8E\xC0"      # mov es, ax

    # Patch SI after we know where the message will land.
    mov_si_index = len(code)
    code += b"\xBE\x00\x00"  # mov si, imm16

    print_loop = len(code)
    code += b"\xAC"          # lodsb
    code += b"\x84\xC0"      # test al, al

    jz_index = len(code)
    code += b"\x74\x00"      # jz hang

    code += b"\xB4\x0E"      # mov ah, 0x0e
    code += b"\xCD\x10"      # int 0x10

    jmp_index = len(code)
    code += b"\xEB\x00"      # jmp print_loop

    hang = len(code)
    code += b"\xF4"          # hlt
    code += b"\xEB\xFD"      # jmp hang

    message_offset = BOOT_LOAD_ADDRESS + len(code)
    code[mov_si_index + 1] = message_offset & 0xFF
    code[mov_si_index + 2] = (message_offset >> 8) & 0xFF

    code[jz_index + 1] = rel8(jz_index + 2, hang)
    code[jmp_index + 1] = rel8(jmp_index + 2, print_loop)

    message = MESSAGE.encode("ascii") + b"\x00"
    sector = code + message

    if len(sector) > IMAGE_SIZE - 2:
        raise ValueError("boot sector is too large")

    sector += b"\x00" * ((IMAGE_SIZE - 2) - len(sector))
    sector += SIGNATURE

    if len(sector) != IMAGE_SIZE:
        raise AssertionError("boot sector must be exactly 512 bytes")
    if sector[-2:] != SIGNATURE:
        raise AssertionError("boot sector signature missing")

    return bytes(sector)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    sector = build_boot_sector()
    OUTPUT.write_bytes(sector)
    print(f"wrote {OUTPUT} ({len(sector)} bytes)")
    print(f"signature: {sector[-2:].hex()}")


if __name__ == "__main__":
    main()
