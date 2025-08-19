import argparse



def add_subparsers(subparsers: argparse._SubParsersAction) -> None:
    _config_parser = subparsers.add_parser("config", help="Configure environment")
    _config_parser.add_argument("-a", "--api", help="Provide an API key", default=None, dest="api", required=False)
    _config_parser.add_argument("-s", "--service", help="Provide a service key", default=None, dest="service", required=False)
    _config_parser.add_argument("-c", "--configPath", help="Provide a configuration path", default=None, dest="configPath", required=False)
    _config_parser.add_argument("-sp", "--servicePath", help="Provide a service path (i.e /v1/current.xml)", default=None, dest="servicePath", required=False)
    _config_parser.add_argument("-t", "--type", help="Provide a service type (i.e xml)", default=None, dest="serviceType", required=False)
    _config_parser.add_argument("-ft", "--finalType", help="Provide a final type (i.e json)", default=None, dest="finalType", required=False)
    _config_parser.add_argument("-m", "--mapping", help="Provide a mapping (i.e {'name': ['city', 'location'] ...)", default=None, dest="mapping", required=False)