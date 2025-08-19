from socket import socket, AF_INET, SOCK_STREAM
import ssl
import core.Network.tools as tools
import core.utils.tools as utils
import core.utils.exceptions

class wrapped(object):


    def __init__(self, __socket, _ssl: bool):
        self.socket = __socket
        self._ssl = _ssl
        self.time: int = 0
        self.finished: bool = False
        self.data: bytes = b""

    def __repr__(self):
        return f"<wrapped socket={self.socket}>"


    def connect(self, target: str, port: int):
        self.socket.connect((target, port))
        if self._ssl:
            context = ssl.create_default_context()
            self.socket = context.wrap_socket(self.socket, server_hostname=target)

    def send(self, data: bytes):
        self.socket.send(data)

    @tools.recv_time
    def recv(self, buffer: int):
        header: bool = False
        while not self.finished:
            retrieved = self.socket.recv(buffer)
            if not header:
                status_code: str = (retrieved.split(b"\r\x0A")[0].split(b" ")[1]).strip().decode("utf-8", errors="ignore")
                if status_code != "200":
                    raise core.utils.exceptions.HttpError(f"Unable to retrieve information. Status code: {status_code}.")
                utils._log(f"Got status code: {status_code}.")
                header = True
            if not retrieved: self.finished = True
            self.data += retrieved
        utils._log(f"received: {len(self.data)} bytes. Acquired for {self.time}s.")


def create_socket(_ssl: bool = False) -> wrapped:
    _object: object = socket(AF_INET, SOCK_STREAM)
    return wrapped(_object, _ssl)





