from typing import Optional

from CS2 import cs2
from Schema.Offset import Offset


class StructSchemaSystem:
    def __init__(self, schemaSysAddr):
        self.schemaSysAddr = schemaSysAddr
        self.moduleBaseAddr = None

    def baseAddr(self) -> Optional[int]:
        if self.moduleBaseAddr is None:
            self.moduleBaseAddr = cs2.u64(self.schemaSysAddr + Offset.StructSchemaSystem.MODULE_BASE)
        return self.moduleBaseAddr

    def modulesCount(self) -> Optional[int]:
        return cs2.u32(self.schemaSysAddr + Offset.StructSchemaSystem.MODULES_COUNT)

    def moduleAddr(self, index: int) -> Optional[int]:
        return cs2.u64(self.baseAddr() + index * Offset.StructSchemaSystem.MODULE_BASE_INDEX)


