from typing import Sequence, Callable

from CS2 import cs2
from Signature.Pattern import Pattern


def matchmakingSignatures() -> Sequence[Pattern]:
    # dwGameTypes
    yield (
        Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 89 5C 24 ?? 48 89 6C 24 ?? 48 89 74 24", cs2.matchmaking)
        .search()
        .rip()
        .setName("dwGameTypes")
    )

    # dwGameTypes_mapName
    yield (
        Pattern('48 8B 81 ?? ?? ?? ?? 48 85 C0 74 ?? 48 83 C0', cs2.matchmaking)
        .search()
        .slice(3, 5)
        .setName("dwGameTypes_mapName")
    )




# def dwGameTypes() -> Pattern:
#     return (
#         Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 89 5C 24 ?? 48 89 6C 24 ?? 48 89 74 24", cs2.matchmaking)
#         .search()
#         .rip()
#     )
#
# def dwGameTypes_mapName() -> Pattern:
#     return (
#         Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 89 5C 24 ?? 48 89 6C 24 ?? 48 89 74 24", cs2.matchmaking)
#         .search()
#         .rip()
#         .add(0x120)
#     )


