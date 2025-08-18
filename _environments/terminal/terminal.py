

import argparse
import sys
import _environments.terminal.helper as helper

class Terminal(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="WeatherAPP", usage = f"python {sys.argv[0]} --help/Config [--help]")

    def __repr__(self):
        return "Terminal"

    def load_base(self) -> None:
        self.parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode", default=False, dest="verbose")
        self.parser.add_argument("-t", "--test", action="store_true", help="Run tests", default=False, dest="test")
        self.parser.add_argument("-q", "--query", action="store", help="Provide a target query (i.e Shumen)", default=None, dest="target", required=False)
        _startparser = self.parser.add_subparsers(title = "Config", dest = "config")
        helper.add_subparsers(_startparser)

    def finish(self):
        return self.parser.parse_args()

def Main():
    _terminal: object = Terminal()
    _terminal.load_base()
    _args: argparse.Namespace = _terminal.finish()