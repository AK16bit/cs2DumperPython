from typing import Optional

from CS2 import cs2
from Schema.Offset import Offset

class StructMember:
    def __init__(self, memberAddr):
        self.memberAddr = memberAddr

        self._name = None
        self._value = None

    @property
    def name(self) -> str:
        if self._name is None:
            strAddr = cs2.u64(self.memberAddr + Offset.StructMember.NAME)
            self._name = cs2.str(strAddr, 128)
        return self._name

    @property
    def value(self) -> int:
        if self._value is None:
            self._value = cs2.u64(self.memberAddr + Offset.StructMember.VALUE)
        return self._value
