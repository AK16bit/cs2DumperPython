from typing import Optional

from CS2 import cs2
from Convar.Offset import Offset


class StructConvarSystem:
    def __init__(self, convarSysAddr):
        self.convarSysAddr = convarSysAddr
        self.convarBaseAddr = None

    def baseAddr(self) -> Optional[int]:
        if self.convarBaseAddr is None:
            self.convarBaseAddr = cs2.u64(self.convarSysAddr + Offset.StructConvarSystem.CONVAR_BASE)
        return self.convarBaseAddr

    def convarCount(self) -> Optional[int]:
        return cs2.u16(self.convarSysAddr + Offset.StructConvarSystem.CONVAR_COUNT)

    def convarAddr(self, index: int) -> Optional[int]:
        return cs2.u64(self.baseAddr() + index * Offset.StructConvarSystem.CONVAR_BASE_INDEX)


