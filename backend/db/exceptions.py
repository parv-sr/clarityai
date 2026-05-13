class StoreAlreadyExists(Exception):
    def __init__(self, is_installed: bool, message: str = "Vector store already exists!"):
        self.is_installed = is_installed
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Is the Vector store installed? - {"True" if self.is_installed else "False"}"