from typing import Optional

from CS2 import cs2
from Signature.Button.Offset import Offset


class StructButton:
    def __init__(self, buttonAddr):
        self.buttonAddr = buttonAddr

        self._name = None
        self._value = None

    @property
    def name(self) -> Optional[str]:
        if self._name is None:
            nameAddr = cs2.u64(self.buttonAddr + Offset.StructButton.NAME)
            self._name = cs2.str(nameAddr, 64)
        return self._name

    @property
    def value(self) -> Optional[int]:
        if self._value is None:
            self._value = self.buttonAddr - cs2.client.base + Offset.StructButton.STATE
        return self._value

