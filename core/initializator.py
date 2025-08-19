import json
import os
from core.utils.tools import log as _log_output, read_file

API_SERVICE: str = ""
CONFIG_DICT: dict = {}
VERBOSITY: bool = False

@read_file
def load_config_file(contents: str):
    """
    The purpose of this method is to load the config file, located in "./core/configuration/config.json.
    This file is extremely recommended as it is a core component.
    :param contents: (str) automatically loaded by using a decorator.
    :return: None.
    """
    global CONFIG_DICT
    CONFIG_DICT = json.loads(contents)
    _log_output("Configuration loaded.") if VERBOSITY else None

def set_api_key(api_key: str):
    os.environ["API_KEY"] = api_key
    _log_output(f"API key set -> {api_key}.\n", f" Information about API key. \n{"\n".join(f"  * {v}" \
    for k, v in CONFIG_DICT["meta"].items())}") if VERBOSITY else None

def set_service(service: str):
    global API_SERVICE
    API_SERVICE = service
    _log_output(f"Service set -> {service}.") if VERBOSITY else None

def set_verbosity(verbosity: bool):
    global VERBOSITY
    VERBOSITY = verbosity

def init(_path: str = "./core/configuration/config.json"):
    load_config_file(path = _path)
    set_api_key(CONFIG_DICT["API_KEY"])
    set_service(CONFIG_DICT["API_SERVICE"])