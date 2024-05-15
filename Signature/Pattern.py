from operator import itemgetter
from typing import Self, Optional, Union, List, Dict

from CS2 import cs2
from pyMeow import Module
from pyMeow.pyMeow import aob_scan_module


class Pattern:
    def __init__(self, pattern: str, module: Union[str, Module], name: Optional[str] = None):
        self._config: Dict = dict(
            name=None,
            pattern=None,
            module=None,
            operations=list()
        )
        self._config.update(dict(module=module.name))

        self.pattern = pattern
        if isinstance(module, str):
            self.module = {module.name: module for module in cs2.modules()}.get(module)
        else:
            self.module = module
        self._address: Optional[int] = None

        self._name: Optional[str] = None
        self.setName(name)


    @property
    def address(self) -> int:
        return self._address

    @property
    def offset(self) -> int:
        offset = self._address - self.module.base * (self._address // self.module.base)

        return offset

    @property
    def config(self) -> Dict[str, Union[str, int, List[Dict[str, Union[str, int]]]]]:
        return self._config

    def search(self) -> Self:
        self._address = aob_scan_module(cs2.process, self.module.name, self.pattern)[0]

        self._config.update(
            pattern=self.pattern
        )
        return self

    def add(self, value: int) -> Self:
        self._address = self._address + value

        self._config.get("operations").append(dict(
            type="add",
            value=value
        ))
        return self

    def rip(self, offset: int = 3, length: int = 7) -> Self:
        address = self._address
        self._address = address + cs2.i32(address + offset) + length

        self._config.get("operations").append(dict(
            type="rip",
            offset=offset,
            length=length
        ))
        return self

    def slice(self, start: int, end: int) -> Self:
        address = cs2.bytes(self._address + start, end - start)
        self._address = int.from_bytes(address, byteorder="little")

        self._config.get("operations").append(dict(
            type="slice",
            start=start,
            end=end
        ))
        return self

    def read(self) -> Self:
        self._address = cs2.u64(self._address)
        self._config.get("operations").append(dict(
            type="read"
        ))
        return self

    def hasName(self) -> bool:
        return self._name is not None

    def getName(self) -> str:
        return self._name

    def setName(self, name: str) -> Self:
        self._name = name
        self._config.update(
            name=name
        )
        return self


