from typing import Optional

from CS2 import cs2
from Convar.Offset import Offset


class StructConvar:
    def __init__(self, convarAddr):
        self.convarAddr = convarAddr

        self._name = None

    @property
    def name(self) -> Optional[str]:
        if self._name is None:
            nameAddr = cs2.u64(self.convarAddr + Offset.StructConvar.NAME)
            self._name = cs2.str(nameAddr, 64)
        return self._name

