"""
BrisartOS Version
Single source of truth for the BrisartOS version string.
Pure Python. No dependencies.
"""

NAME = "BrisartOS"
VERSION = "0.4.4-alpha"


def version_text():
    return f"{NAME} {VERSION}"