"""
Hello Lab Module
Pure Python.
No dependencies.
"""

MODULE_NAME = "hello_lab"
MODULE_DISPLAY_NAME = "Hello Lab Module"
MODULE_VERSION = "0.1.0"
MODULE_AUTHOR = "Jason Brisart"

MODULE_DESCRIPTION = (
    "Demonstration module for "
    "BrisartOS modular runtime."
)

MODULE_ABI = (
    "brisartos.module.v1"
)

MODULE_PERMISSIONS = (
    "log",
    "module_data",
)


def run(api):

    print()
    print("===================")
    print(" HELLO LAB MODULE")
    print("===================")
    print()

    object_id = (
        api.new_object_id()
    )

    print(
        "Generated Object ID:"
    )

    print(object_id)

    api.write_module_text(
        "hello_lab",
        "hello.txt",
        (
            "Hello from "
            "BrisartOS\n"
            f"Object ID: "
            f"{object_id}\n"
        )
    )

    api.log(
        "hello_lab",
        "module executed"
    )

    print()
    print(
        "File written "
        "successfully."
    )
    print()