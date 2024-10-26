# Runner singleton used to run functions with a single entrypoint
from typing import Callable
import logging


class Runner:
    _logger : logging.Logger
    # remember to use a unique key and add the function to the map here
    funcMap: dict[str, Callable[..., object]] 
    
    def __init__(self, logger : logging.Logger | None = None) -> None:
        self._logger = logging.getLogger(__name__) if (logger is None) else logger
        self.funcMap = {}

    def register(self, key: str, callback: Callable[..., object]) -> None:
        '''Register a function to the Runner instance, is upsert'''
        if (self.funcMap.get(key) is not None): 
            self._logger.info(f"Callback for key: {key} has been updated")
            
        self.funcMap[key] = callback

    # run from map
    def run(self, key: str, args: list[object]) -> object:
        '''Run based on key, passing in the string arguments'''
        method = self.funcMap.get(key, None)
        
        if method is None or not callable(method): 
            self._logger.info(f"")
            return None
        
        return method(*args)

