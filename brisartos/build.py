"""
BrisartOS Build Script
Pure Python.
No dependencies.
Standard library only.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from version import VERSION

BOOT_SIZE = 512
SIGNATURE = b"\x55\xAA"
OUTPUT = Path("build/brisartos_boot.img")
BOOT_MESSAGE = (
    f"BrisartOS {VERSION}\r\n"
    "Python-Made Research OS\r\n"
    "Local-First | Offline-Capable\r\n"
    "Dependencies: None\r\n"
    "Custom Source Only\r\n"
)


def build_image():
    """
    Build a simple boot image.
    This is still an early placeholder image.
    The boot message is embedded into the image
    and can later be printed by the boot runtime.
    """
    image = bytearray()
    #
    # Temporary boot marker bytes.
    #
    image.extend(b"BRISARTOS_BOOT")
    #
    # Embed boot banner.
    #
    image.extend(BOOT_MESSAGE.encode("ascii"))
    #
    # Pad to boot sector size.
    #
    while len(image) < BOOT_SIZE - 2:
        image.append(0)
    #
    # Add boot signature.
    #
    image.extend(SIGNATURE)
    return bytes(image)


def main():
    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )
    image = build_image()
    OUTPUT.write_bytes(image)
    print()
    print("===================================")
    print(" BrisartOS Build Complete")
    print("===================================")
    print(f"Output : {OUTPUT}")
    print(f"Size   : {len(image)} bytes")
    print(f"Message: {BOOT_MESSAGE.splitlines()[0]}")
    print("Signature: 55AA")
    print()


if __name__ == "__main__":
    main()