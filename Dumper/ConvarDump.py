from typing import Generator, Optional

from CS2 import cs2
from Convar.Offset import Offset
from Convar.Struct.StructConvar import StructConvar
from Convar.Struct.StructConvarSystem import StructConvarSystem
from utils import timeUseInfo, logger, int2hex, errorButDontCloseWindow


@timeUseInfo
@errorButDontCloseWindow
def dumpConvar():
    convarSysAddr = readConvarSysAddr()
    convarSysStruct = StructConvarSystem(convarSysAddr)

    convarsCount = convarSysStruct.convarCount()
    convarsAddr: Generator[int, None, None] = (convarSysStruct.convarAddr(index) for index in range(convarsCount))

    logger.debug("Convars Base Address: %s (Convars Count: %s)" % (
        convarSysStruct.baseAddr(),
        convarsCount
    ))

    convars = list()
    for convarAddr in convarsAddr:
        convarStruct = readConvar(convarAddr)
        if convarStruct is None:
            logger.debug(" · %s -> Convar Address Error!" % (
                int2hex(convarAddr)
            ))

            continue

        logger.debug(" · %s -> Convar: %s" % (
            int2hex(convarAddr),
            convarStruct.name
        ))

        convars.append(convarStruct)

    logger.debug("Convar Dump Success Percent: %.1f%% (%s / %s) " % (
        (len(convars) / convarsCount) * 100,
        len(convars), convarsCount
    ))

def readConvarSysAddr() -> Optional[int]:
    try:
        convarSysAddr = cs2.tier0.pattern(Offset.StructConvarSystem.CONVAR_SYSTEM_PATTERN)
        convarSysAddr = convarSysAddr + cs2.i32(convarSysAddr + Offset.StructConvarSystem.CONVAR_SYSTEM_PATTERN_RIP_OFFSET) + Offset.StructConvarSystem.CONVAR_SYSTEM_PATTERN_RIP_LENGTH
    except Exception:
        logger.error("Convar: Convar System Pattern Invalid!")
        return None

    return convarSysAddr


def readConvar(convarAddr: int) -> Optional[StructConvar]:
    convarStruct = StructConvar(convarAddr)

    try:
        if not convarStruct.name: return None
        return convarStruct

    except Exception: return None
