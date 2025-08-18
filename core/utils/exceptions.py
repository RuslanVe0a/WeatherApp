


class InvalidTarget(Exception):



    def __init__(self, message: str) -> None:
        super().__init__(f"Unhandled error has occurred: {message}")

    def __repr__(self):
        return f"InvalidTarget->Exception"


class HttpError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(f"Unhandled error has occurred: {message}")

    def __repr__(self) -> str:
        return f"HttpError->Exception"