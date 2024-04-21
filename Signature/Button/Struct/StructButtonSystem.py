from typing import Optional

from CS2 import cs2
from Signature.Button.Offset import Offset


class StructButtonSystem:
    def __init__(self, convarSysAddr):
        self.buttonSysAddr = convarSysAddr

    def buttonAddr(self) -> Optional[int]:
        return cs2.u64(self.buttonSysAddr)

    def buttonAddrNext(self, buttonAddr: int) -> Optional[int]:
        return cs2.u64(buttonAddr + Offset.StructButtonSystem.BUTTON_NEXT)

