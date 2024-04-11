from typing import TypedDict

__all__ = [
    "StructProcess", "StructModule"
]

class StructProcess(TypedDict):
    name: str
    pid: int
    debug: bool
    handle: int
class StructModule(TypedDict):
    name: str
    base: int
    end: int
    size: int