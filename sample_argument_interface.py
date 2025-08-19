from argparse import Namespace
import _environments.terminal.terminal as terminal
import core.initializator
import core.WeatherMain


def inspect(_argument: Namespace):
    """
    The purpose of this method is to show how arguments can be manipulated and then used, manually.
    :param _argument:
    :return: None.
    """
    _weatherMain: core.WeatherMain.Main = core.WeatherMain.Main()
    _target: str = _argument.target
    _verbosity: bool = _argument.verbose
    core.initializator.set_verbosity(_verbosity)
    _test: str = _argument.test
    _features = _argument.features
    if not _features: core.initializator.init()
    else:
        api, service, configPath, servicePath, _type, finalType, _mapping = _argument.api, _argument.service, _argument.configPath,\
        _argument.servicePath, _argument.serviceType, _argument.finalType, _argument.mapping
        if api: core.initializator.API_KEY = api
        if service: core.initializator.API_SERVICE = service
        if configPath: core.initializator.init(configPath)
        if servicePath: core.initializator.CONFIG_DICT["SPATH"] = servicePath
        if finalType: core.initializator.CONFIG_DICT["_final_type"] = finalType
        if _mapping: core.initializator.CONFIG_DICT["mapping"] = _mapping
    _weatherMain.set_target(("_", _target) if "," not in _target else _target.split(","))
    _weatherMain.activate()
    _weatherMain.output_friendly()

if __name__ == "__main__":
    inspect(terminal.Main())