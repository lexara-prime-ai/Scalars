class Logger:
    def __init__(self) -> None:
        self.util_identifier: str = "LOGGER"
        self.BASE_LOG_DIR_PATH: str = "./logs/"
        self.file_paths: list[str] = [f"{self.BASE_LOG_DIR_PATH}logs.txt"]
        self.file_io_options: list[str] = ["a", "w", "r"]

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
        print(f"""
            * * * WRITING TO FILE WITH THE FOLLOWING OPTIONS * * *
              FILE_PATH: {self.file_paths[0]}
              FILE_IO_OPTION: {self.file_io_options[0]}
        """)
        f = open(self.file_paths[0], self.file_io_options[0])
        f.write(parsed_entry)
        f.close()
