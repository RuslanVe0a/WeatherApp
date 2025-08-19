import os
import json
import xml.etree.ElementTree as ET
from socket import gethostbyname
import core.Network._socket
import core.initializator
import core.utils.tools as tools

class _abstract_sock(object):

    def __init__(self):
        self.socket = None

    def create_sock(self, host: str, _ssl: bool):
        self.socket = core.Network._socket.create_socket(_ssl)
        self.socket.connect(host, 443 if _ssl else 80)
        return self



class get(_abstract_sock):


    def __init__(self, url: str = "", _class_object = None, _ssl: bool = False) -> None:
        self.url: str = url
        self.classObject: object = _class_object
        self.header: str = ""
        self.type: str = ""
        super().__init__()
        self.create_sock(gethostbyname(self.url) if url else _class_object.settings["config_file"]["API_SERVICE"],
        _ssl)

    def __repr__(self, *args, **kwargs) -> str:
        return f"<requests.get url = {self.url} classObject = {True if self.classObject else False}>"

    def set_header(self, header: str):
        self.header = header

    def send(self):
        _http_header: str = (f"GET /{core.initializator.CONFIG_DICT["SPATH"]}?{self.header} HTTP/1.0\r\x0A\
Host: {core.initializator.API_SERVICE}\r\x0AConnection: Keep-Alive\r\x0AUser-Agent: Python/WeatherCrawler/0.0001\r\x0A\r\x0A")
        self.socket.send(_http_header.encode("utf-8", errors="ignore"))

    def receive(self):
        _data: bytes = self.socket.recv(1024, recv_time_config = {"_attr" : self.socket})

    def set_type(self, type: str):
        self.type = type

    def as_json(self):
        tools._log("Unpacking payload information...")
        _payload: str = self.socket.data.split(b"\r\x0A\r\x0A")[1].decode("utf-8", errors="ignore")
        if self.type == "xml":
            _root = ET.fromstring(_payload)
            location = _root.find(".//location")
            current = _root.find(".//current")
            _targets: dict = {}
            for v, k, f in core.initializator.CONFIG_DICT["mapping"]:
                child = location.find(".//" + k) if f == "location" else current.find(".//" + k)
                _targets[v] = child.text if child is not None else None
            tools._log("Finished.")
            return _targets
        elif self.type == "json":
            return json.loads(_payload)

    def __del__(self):
        pass