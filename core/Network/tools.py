import copy
import threading
import time




def recv_time(function):

    def wrapper(*args, **kwargs):
        if "recv_time_config" not in kwargs:
            raise KeyError("recv_time_config")
        copied: dict = kwargs["recv_time_config"]
        del kwargs["recv_time_config"]
        threading.Thread(target=function, args=args, kwargs=kwargs).start()
        while not copied["_attr"].finished:
            if copied["_attr"].time >= 3: setattr(copied["_attr"], "finished", True)
            copied["_attr"].time += 1
            time.sleep(1)
        return copied["_attr"].data

    return wrapper