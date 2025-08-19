import json
import core.utils.tools as tools


API_KEY: str = ""
API_SERVICE: str = ""
CONFIG_DICT: dict = {}
VERBOSITY: bool = False

@tools.read_file
def load_config_file(contents: str) -> None:
    """
    The purpose of this method is to load the config file, located in "./core/configuration/config.json.
    This file is extremely recommended as it is a core component.
    :param contents: (str) automatically loaded by using a decorator.
    :return: None.
    """
    global CONFIG_DICT
    CONFIG_DICT = json.loads(contents)
    tools._log("Configuration loaded.") if VERBOSITY else None

def set_api_key(api_key: str):
    global API_KEY
    API_KEY = api_key
    tools._log(f"API key set -> {api_key}.\n", f" Information about API key. \n{"\n".join(f"  * {v}" \
    for k, v in CONFIG_DICT["meta"].items())}") if VERBOSITY else None

def set_service(service: str):
    global API_SERVICE
    API_SERVICE = service
    tools._log(f"Service set -> {service}.") if VERBOSITY else None

def set_verbosity(verbosity: bool):
    global VERBOSITY
    VERBOSITY = verbosity

def init(_path: str = "./core/configuration/config.json"):
    load_config_file(path = "./core/configuration/config.json")
    set_api_key(CONFIG_DICT["API_KEY"])
    set_service(CONFIG_DICT["API_SERVICE"])