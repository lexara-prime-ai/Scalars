class ErrorHandler:
    def __init__(self) -> None:
        self.util_identifier: str = "ERROR_HANDLER"
        self.file_paths: list[str] = ["error_logs.txt"]
        self.file_io_options: list[str] = ["a", "w", "r"]

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
        print(f"""
            * * * WRITING TO FILE WITH THE FOLLOWING OPTIONS * * *
              FILE_PATH: {self.file_paths[0]}
              FILE_IO_OPTION: {self.file_io_options[0]}
        """)
        f = open(self.file_paths[0], self.file_io_options[0])
        f.write(parsed_error)
        f.close()
