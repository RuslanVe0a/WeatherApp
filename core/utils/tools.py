import colorama



colorama.just_fix_windows_console()

def _log(*text, color: str = colorama.Fore.WHITE, head: str = "[LOG]: ") -> None:
    print(head, color, *text, colorama.Style.RESET_ALL, "\n")
    return

def _warning(*text, color: str = colorama.Fore.YELLOW, head: str = "[WARNING]: ") -> None:
    _log(text, color, head)

def _error(*text, color: str = colorama.Fore.RED, head: str = "[ERROR]: ") -> None:
    _log(text, color, head)



def read_file(function):

    def wrapper(*args, **kwargs) -> None:
        # path is a reserved keyword and will be deleted.
        path: str = kwargs["path"]
        del kwargs["path"]
        function(open(path, "r", encoding="utf-8", errors="ignore").read(), *args, **kwargs)
    return wrapper