import logging

class Config():

    def __init__(self, port: int, log_level: str, num_workers: int):
        self._port = port
        self._num_workers = num_workers

        self._log_level = logging.getLevelNamesMapping()[log_level]

    @property
    def port(self) -> int:
        return self._port 
    
    @property
    def log_level(self) -> int:
        return self._log_level 
    
    @property
    def num_workers(self) -> int:
        return self._num_workers 