"""
BrisartOS Runtime
Pure Python.
No dependencies.
"""

from brisart_platform import PlatformInfo
from system_api import SystemAPI
from module_loader import ModuleLoader


class BrisartRuntime:
    NAME = "BrisartOS"
    VERSION = "0.4.0-alpha"
    PROFILE = "Modular Research Operating Environment"

    def __init__(self):
        self.platform = PlatformInfo()
        self.api = SystemAPI(self.platform)

        self.loader = ModuleLoader(
            modules_path="modules",
            api=self.api
        )

    def boot(self):
        print()
        print("===================================")
        print(" BrisartOS Runtime Boot")
        print("===================================")
        print(f"Version : {self.VERSION}")
        print(f"Profile : {self.PROFILE}")
        print()
        self.loader.discover()

    def version_text(self):
        return (
            f"{self.NAME} {self.VERSION}\n"
            "Pure Python. No Dependencies. Modular."
        )

    def print_system_info(self):
        print()

        info = self.platform.describe()

        for key in sorted(info):
            print(f"{key}: {info[key]}")

        print()

    def print_modules(self):
        print()

        if not self.loader.modules:
            print("No modules found.")
            print()
            return

        for name in sorted(self.loader.modules):
            module = self.loader.modules[name]
            print(f"{name} - {module.display_name}")

        print()

    def describe_module(self, name):
        module = self.loader.get(name)

        if module is None:
            print("module not found")
            return

        print()
        print("Name:", module.name)
        print("Display Name:", module.display_name)
        print("Version:", module.version)
        print("Author:", module.author)
        print("ABI:", module.abi)

        print()
        print(module.description)
        print()

    def run_module(self, name):
        module = self.loader.get(name)

        if module is None:
            print("module not found")
            return

        module.run()

    def reload_modules(self):
        self.loader.discover()
        print("modules reloaded")