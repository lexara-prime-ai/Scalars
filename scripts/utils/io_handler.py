import os
from constants.constants import Constants


class InputOutputHandler:
    def __init__(self) -> None:
        self.util_identifier = "IO_HANDLER"
        self.base_path: str = Constants.BASE_LOG_DIR_PATH
        self.file_paths: list[str] = Constants.FILE_PATHS
        self.file_io_options: list[str] = Constants.FILE_IO_OPTIONS

    def create_logs_directory(self):
        try:
            if not os.path.exists(self.base_path):
                print(
                    f"\nINFO: Creating <logs> directory...\nPATH: {self.base_path}")
                os.mkdir(self.base_path)
            else:
                print("\nINFO: <logs> directory already exists...\nProceeding...")
        except Exception as e:
            print(f"""
                  * * * An error occurred while attempting trying to create the <logs> directory * * *

                  ERROR: {str(e)}
                """)

    def write_to_file(self, path: str, io_option: str, content: str):
        try:
            if not os.path.exists(self.base_path):
                self.create_logs_directory()
                # Perform IO operations
                self.perform_io_operations(path, io_option, content)
            else:
                print(f"""
                    * * * WRITING TO FILE WITH THE FOLLOWING OPTIONS * * *
                                    FILE_PATH: {path}
                                    FILE_IO_OPTION: {io_option}
                """)

                # Perform IO operations
                self.perform_io_operations(path, io_option, content)
        except Exception as e:
            print(f"""
                  * * * An error occurred while attempting trying to perform IO operations * * *

                  ERROR: {str(e)}
                """)

    def perform_io_operations(self, path: str, io_option: str, content: str):
        try:
            file_operations = open(path, io_option)
            file_operations.write(content)
            file_operations.close()
        except Exception as e:
            print(f"""
                  * * * An error occurred while attempting trying to perform IO operations * * *

                  ERROR: {str(e)}
                """)
