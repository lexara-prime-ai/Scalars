# Import the sys & subprocess modules
import sys
import subprocess
from utils.error_handling import ErrorHandler
from utils.logger import Logger


class Program:
    def __init__(self) -> None:
        self.state = "Running..."
        self.error_handling = ErrorHandler()
        self.logging = Logger()

    def package_installer(self, package_name: str):
        try:
            print(f"Attempting to install package: {package_name}")

            result = subprocess.check_call([
                sys.executable,
                "-m",
                "pip",
                "install",
                package_name
            ])

            self.logging.parse_entry("Yes I attempted...")
        except Exception as e:
            self.error_handling.parse_error(e)

    def __call__(self):
        self.package_installer("torch")


if __name__ == "__main__":
    Program()()
