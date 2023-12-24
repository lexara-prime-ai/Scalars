import os

class InputOutputHandler:
    def __init__(self) -> None:
        self.util_identifier = "IO_HANDLER"
        self.BASE_LOG_DIR_PATH: str = "./logs/"
        self.file_paths: list[str] = [f"{self.BASE_LOG_DIR_PATH}logs.txt", f"{self.BASE_LOG_DIR_PATH}error_logs.txt"]
        self.file_io_options: list[str] = ["a", "w", "r"]

    def create_logs_directory(self):
        try:
            if not os.path.exists(self.BASE_LOG_DIR_PATH):
                print("\nINFO: Creating <logs> directory...")
                os.mkdir(self.BASE_LOG_DIR_PATH)
            else:
                print("\nINFO: <logs> directory already exists...\nProceeding...")
        except Exception as e:
            print(f"""
                  * * * An error occurred while attempting trying to create the <logs> directory * * *

                  ERROR: {str(e)}
                  """)