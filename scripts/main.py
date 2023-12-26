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
            print(f"> Attempting to install package: {package_name}")

            result = subprocess.check_call([
                sys.executable,
                "-m",
                "pip",
                "install",
                package_name
            ])

            # Log entry
            self.logging.parse_entry(result)

            # Handle imports "dynamically"
            import torch as pt

            # ------------------------#
            # Working with [Scalars]
            x_pt = pt.tensor(36)
            print(f"OUTPUT: {x_pt}")
            print(f"TENSOR_SHAPE: {x_pt.shape}")
            print(f"TENSOR_TYPE: {x_pt.type()}")

        except Exception as e:
            self.error_handling.parse_error(e)

    def __call__(self):
        self.package_installer("torch")


if __name__ == "__main__":
    Program()()
