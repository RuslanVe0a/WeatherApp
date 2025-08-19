from core.utils.tools import log as logging, warning as warning
import core.utils.exceptions
import core.initializator
import core.Network.requests as requests
import os

core.initializator.init() # an initializator for the main components.


def _construct(dictionary: dict, target: str, api_key: str) -> str:
    header: str = ""
    for k, v in dictionary:
        header += f"{k}={api_key if v == "key" else target}&"
    return header


class Main(object):


    def __init__(self):
        logging("Initializing WeatherMain.")
        self.target: str = ""
        self.results: dict = {}
        self.flags: list = [] # works for filters as well.
        self.settings: dict = {
            "config_file": core.initializator.CONFIG_DICT,
            "API_KEY": os.getenv("API_KEY"),
            "API_SERVICE": core.initializator.API_SERVICE,
        }

    def set_target(self, target: tuple[str, str]):
        if len(target) != 2 or not target[0] or not target[1]:
            raise core.utils.exceptions.InvalidTarget("Invalid target.")
        self.target = target
        logging(f"Target set -> {", ".join(target)}.")

    def set_filters(self, filters: dict):
        if not filters:
            warning("Given filters are empty. No need to add them."); return
        if not isinstance(filters, dict):
            raise TypeError(f"Expected dict, got: {str(type(filters))}")
        self.flags = filters

    def activate(self):
        logging("Activating WeatherMain.")
        _request: object = requests.Get(_class_object=self)
        _request.set_header(_construct(core.initializator.CONFIG_DICT["arguments"]["essential"], self.target[1], self.settings["API_KEY"]))
        _request.send()
        _request.set_type(core.initializator.CONFIG_DICT["type"])
        _request.receive()
        if core.initializator.CONFIG_DICT["_final_type"] == "json":
            self.results = _request.as_json()

    def output_friendly(self):
        logging("Output friendly WeatherMain -- active.")
        print("\n".join(f"  * {k}: {v};" for k, v in self.results.items()), "\n\n")
        return