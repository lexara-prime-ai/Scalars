from utils.io_handler import InputOutputHandler
from constants.constants import Constants


class Logger:
    def __init__(self) -> None:
        self.util_identifier: str = "LOGGER"
        self.file_path: list[str] = Constants.FILE_PATHS[0]
        self.file_io_option: list[str] = Constants.FILE_IO_OPTIONS[0]
        self.io_handler = InputOutputHandler()

    def parse_entry(self, message: str) -> str:
        result: str = f"""
              * * * NEW LOG ENTRY * * *
                  __ENTRY DETAILS__
                     {message}
            """
        # Log entry -> OPTIONAL
        self.log_entry(result)
        return result

    def log_entry(self, parsed_entry: str):
        self.io_handler.write_to_file(
            self.file_path, self.file_io_option, parsed_entry)
