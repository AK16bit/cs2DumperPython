from logging import debug, error
from typing import Optional, List

from CS2 import cs2
from Signature.Button.Offset import Offset
from Signature.Button.Struct.StructButton import StructButton
from Signature.Button.Struct.StructButtonSystem import StructButtonSystem
from Signature.Container import ContainerSignature, ContainerModule
from utils import errorButDontCloseWindow, int2hex


@errorButDontCloseWindow
def buttonSignature() -> ContainerModule:
    buttonSysAddr = readButtonSysAddr()
    buttonSysStruct = StructButtonSystem(buttonSysAddr)

    buttons: List[ContainerSignature] = list()
    buttonAddr = buttonSysStruct.buttonAddr()
    while buttonAddr:
        buttonStruct = readButton(buttonAddr)
        if buttonStruct is None: break

        buttons.append(buttonStruct)

        debug(" · %s -> Signature: %s (Address: %s) (Offset: %s)" % (
            int2hex(buttonAddr),
            buttonStruct.get("name"),
            int2hex(cs2.client.base + buttonStruct.get("value")),
            int2hex(buttonStruct.get("value"))
        ))

        buttonAddr = buttonSysStruct.buttonAddrNext(buttonAddr)

    return ContainerModule(name=cs2.client.name.replace(".", "_"), signatures=buttons)



def readButtonSysAddr() -> Optional[int]:
    try:
        buttonSysAddr = cs2.client.pattern(Offset.StructButtonSystem.BUTTON_SYSTEM_PATTERN)
        buttonSysAddr = buttonSysAddr + cs2.i32(buttonSysAddr + Offset.StructButtonSystem.BUTTON_SYSTEM_PATTERN_RIP_OFFSET) + Offset.StructButtonSystem.BUTTON_SYSTEM_PATTERN_RIP_LENGTH
    except Exception:
        error("Convar: Convar System Pattern Invalid!")
        return None

    return buttonSysAddr

def readButton(buttonAddr: int) -> Optional[ContainerSignature]:
    buttonStruct = StructButton(buttonAddr)

    try:
        if buttonStruct.name is None: return None
        return ContainerSignature(name="dwForce" + buttonStruct.name.title(), value=buttonStruct.value)
    except Exception: return None
