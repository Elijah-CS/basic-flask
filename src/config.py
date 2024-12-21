
class Config():

    def __init__(self, port: int, num_workers: int):
        self._port = port
        self._num_workers = num_workers

    @property
    def port(self) -> int:
        return self._port 
    
    @property
    def num_workers(self) -> int:
        return self._num_workers 