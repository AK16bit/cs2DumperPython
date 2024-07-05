from typing import Sequence, Callable

from CS2 import cs2, CS2Process
from Signature.Pattern import Pattern


# def engineSignatures() -> Sequence[Callable]:
#     return (
#         dwBuildNumber,
#         dwNetworkGameClient, dwNetworkGameClient_deltaTick, dwNetworkGameClient_getLocalPlayer,
#         dwNetworkGameClient_getMaxClients, dwNetworkGameClient_signOnState,
#         dwWindowHeight, dwWindowWidth,
#         dwSoundService,
#         dwEngineViewData
#     )

def engineSignatures() -> Sequence[Pattern]:
    # dwBuildNumber
    yield (
        Pattern("89 05 ?? ?? ?? ?? 48 8D 0D ?? ?? ?? ?? FF 15 ?? ?? ?? ??", cs2.engine)
        .search()
        .rip(2, 6)
        .setName("dwBuildNumber")
    )

    # dwNetworkGameClient
    yield (
        Pattern("48 89 3D ?? ?? ?? ?? 48 8D 15", cs2.engine)
        .search()
        .rip()
        .setName("dwNetworkGameClient")
    )

    # dwNetworkGameClient_clientTickCount
    yield (
        Pattern("8B 81 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC CC 8B 81 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC CC 83 B9", cs2.engine)
        .search()
        .slice(2, 4)
        .setName("dwNetworkGameClient_clientTickCount")
    )

    # dwNetworkGameClient_deltaTick
    yield (
        Pattern("89 83 ?? ?? ?? ?? 40 B7", cs2.engine)
        .search()
        .slice(2, 4)
        .setName("dwNetworkGameClient_deltaTick")
    )

    # dwNetworkGameClient_isBackgroundMap
    yield (
        Pattern("0F B6 81 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 0F B6 81 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 89 5C 24", cs2.engine)
        .search()
        .slice(3, 6)
        .setName("dwNetworkGameClient_isBackgroundMap")
    )

    # dwNetworkGameClient_localPlayer
    yield (
        Pattern("48 83 C0 ?? 48 8D 04 40 8B 0C C1", cs2.engine)
        .search()
        .slice(3, 4)
        .add(0xE6)
        .setName("dwNetworkGameClient_localPlayer")
    )

    # dwNetworkGameClient_maxClients
    yield (
        Pattern("8B 81 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC CC 8B 81 ?? ?? ?? ?? FF C0", cs2.engine)
        .search()
        .slice(2, 4)
        .setName("dwNetworkGameClient_maxClients")
    )

    # dwNetworkGameClient_serverTickCount
    yield (
        Pattern("8B 81 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC CC 83 B9", cs2.engine)
        .search()
        .slice(2, 4)
        .setName("dwNetworkGameClient_serverTickCount")
    )

    # dwNetworkGameClient_signOnState
    yield (
        Pattern("44 8B 81 ?? ?? ?? ?? 48 8D 0D", cs2.engine)
        .search()
        .slice(3, 5)
        .setName("dwNetworkGameClient_signOnState")
    )

    # dwWindowHeight
    yield (
        Pattern("8B 05 ?? ?? ?? ?? 89 03", cs2.engine)
        .search()
        .rip(2, 6)
        .setName("dwWindowHeight")
    )

    # dwWindowWidth
    yield (
        Pattern("8B 05 ?? ?? ?? ?? 89 07", cs2.engine)
        .search()
        .rip(2, 6)
        .setName("dwWindowWidth")
    )


# def dwBuildNumber() -> Pattern:
#     return (
#         Pattern("89 05 ?? ?? ?? ?? 48 8D 0D ?? ?? ?? ?? FF 15 ?? ?? ?? ??", cs2.engine)
#         .search()
#         .rip(2, 6)
#     )
#
# def dwNetworkGameClient() -> Pattern:
#     return (
#         Pattern("48 89 3D ?? ?? ?? ?? 48 8D 15", cs2.engine)
#         .search()
#         .rip()
#     )
#
# def dwNetworkGameClient_deltaTick() -> Pattern:
#     return (
#         Pattern("89 83 ?? ?? ?? ?? 40 B7", cs2.engine)
#         .search()
#         .slice(2, 4)
#     )
#
# def dwNetworkGameClient_getLocalPlayer() -> Pattern:
#     return (
#         Pattern("48 83 C0 ?? 48 8D 04 40 8B 0C C1 48 8B C2 89 0A C3 C7 02", cs2.engine)
#         .search()
#         .slice(3, 4)
#         .add(0xE6)
#     )
#
# def dwNetworkGameClient_getMaxClients() -> Pattern:
#     return (
#         Pattern("8B 81 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC CC 8B 81 ?? ?? ?? ?? FF C0", cs2.engine)
#         .search()
#         .slice(2, 4)
#     )
#
# def dwNetworkGameClient_signOnState() -> Pattern:
#     return (
#         Pattern("44 8B 81 ?? ?? ?? ?? 48 8D 0D", cs2.engine)
#         .search()
#         .slice(3, 5)
#     )
#
# def dwWindowHeight() -> Pattern:
#     return (
#         Pattern("8B 05 ?? ?? ?? ?? 89 03", cs2.engine)
#         .search()
#         .rip(2, 6)
#     )
#
# def dwWindowWidth() -> Pattern:
#     return (
#         Pattern("8B 05 ?? ?? ?? ?? 89 07", cs2.engine)
#         .search()
#         .rip(2, 6)
#     )
#
# def dwSoundService() -> Pattern:
#     return (
#         Pattern("48 89 05 ?? ?? ?? ?? 4C 8D 44 24 ?? 48 8D 05", cs2.engine)
#         .search()
#         .rip()
#     )
#
# def dwEngineViewData() -> Pattern:
#     return (
#         Pattern("48 89 05 ?? ?? ?? ?? 4C 8D 44 24 ?? 48 8D 05", cs2.engine)
#         .search()
#         .rip()
#         .add(0x9C)
#     )

