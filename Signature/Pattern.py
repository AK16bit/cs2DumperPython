from operator import itemgetter
from typing import Self, Optional, Union

from CS2 import cs2
from pyMeow import Module
from pyMeow.pyMeow import aob_scan_module


class Pattern:
    def __init__(self, pattern: str, module: Union[str, Module]):
        self.pattern = pattern
        if isinstance(module, str):
            self.module = {module.name: module for module in cs2.modules()}.get(module)
        else:
            self.module = module

        self._address: Optional[int] = None

    @property
    def address(self) -> int:
        return self._address

    @property
    def offset(self) -> int:
        offset = self._address - self.module.base * (self._address // self.module.base)

        return offset

    def search(self) -> Self:
        self._address = aob_scan_module(cs2.process, self.module.name, self.pattern)[0]

        return self

    def add(self, value: int) -> Self:
        address = self._address
        address = address + value

        self._address = address
        return self

    def rip(self, offset: int = 3, length: int = 7) -> Self:
        address = self._address
        address = address + cs2.i32(address + offset) + length

        self._address = address
        return self

    def slice(self, start: int, end: int) -> Self:
        address = self._address
        address = cs2.bytes(address + start, end - start)
        address = int.from_bytes(address, byteorder="little")

        self._address = address
        return self

    def read(self) -> Self:
        address = self._address
        address = cs2.u64(address)

        self._address = address
        return self
