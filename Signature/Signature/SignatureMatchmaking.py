from typing import Sequence, Callable

from CS2 import cs2
from Signature.Pattern import Pattern


def matchmakingSignatures() -> Sequence[Callable]:
    return (
        dwGameTypes, dwGameTypes_mapName
    )

def dwGameTypes() -> Pattern:
    return (
        Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 89 5C 24 ?? 48 89 6C 24 ?? 48 89 74 24", cs2.matchmaking)
        .search()
        .rip()
    )

def dwGameTypes_mapName() -> Pattern:
    return (
        Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 89 5C 24 ?? 48 89 6C 24 ?? 48 89 74 24", cs2.matchmaking)
        .search()
        .rip()
        .add(0x120)
    )


