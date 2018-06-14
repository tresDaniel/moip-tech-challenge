class Error(Exception):
    def __init__(self, message):
        self.message = message


class InvalidCpfError(Error):
    pass


class InvalidEmailError(Error):
    pass


class InvalidCardError(Error):
    pass
