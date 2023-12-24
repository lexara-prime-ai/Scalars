from utils.io_handler import InputOutputHandler
from constants.constants import Constants


class ErrorHandler:
    def __init__(self) -> None:
        self.util_identifier: str = "ERROR_HANDLER"
        self.file_path: list[str] = Constants.FILE_PATHS[1]
        self.file_io_option: list[str] = Constants.FILE_IO_OPTIONS[0]
        self.io_handler = InputOutputHandler()

    def parse_error(self, error: Exception) -> str:
        result: str = f"""
              * * * AN ERROR OCCURRED * * *
                  __EXCEPTION DETAILS__
                        {error}
            """
        # Log error -> OPTIONAL
        self.log_error(result)
        return result

    def log_error(self, parsed_error: str):
        self.io_handler.write_to_file(
            self.file_path, self.file_io_option, parsed_error)
