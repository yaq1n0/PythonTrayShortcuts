# Runner singleton used to run functions with a single entrypoint
from typing import Callable


class Runner:
    def __init__(self) -> None:
        pass

    # must contain this function input signature
    def exampleRun(args : list[str]) -> int:
        return 0
    
    def concatArgs(args : list[str]) -> str: 
        return ",".join(args)
    
    # remember to use a unique key and add the function to the map here
    funcMap : dict[str, Callable[..., int]]= {
        "exampleRun": exampleRun,
        "concatArgs": concatArgs
    }

    # entry point 
    def run(self, key: str, args: list[str]):
        if key in self.funcMap:
            method = self.funcMap[key]
            if callable(method):
                return method(args)
            else: 
                raise KeyError(f"Non-callable key: {key}")
        else:
            raise KeyError(f"No such function: {key}")
        

