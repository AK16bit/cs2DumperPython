from typing import Sequence, Callable

from CS2 import cs2
from Signature.Pattern import Pattern


def engineSignatures() -> Sequence[Callable]:
    return (
        dwBuildNumber,
        dwNetworkGameClient, dwNetworkGameClient_deltaTick, dwNetworkGameClient_getLocalPlayer,
        dwNetworkGameClient_getMaxClients, dwNetworkGameClient_signOnState,
        dwWindowHeight, dwWindowWidth
    )


def dwBuildNumber() -> Pattern:
    return (
        Pattern("89 05 ?? ?? ?? ?? 48 8D 0D ?? ?? ?? ?? FF 15 ?? ?? ?? ?? E9", cs2.engine)
        .search()
        .rip(2, 6)
    )

def dwNetworkGameClient() -> Pattern:
    return (
        Pattern("48 89 3D ?? ?? ?? ?? 48 8D 15", cs2.engine)
        .search()
        .rip()
    )

def dwNetworkGameClient_deltaTick() -> Pattern:
    return (
        Pattern("89 83 ?? ?? ?? ?? 40 B7", cs2.engine)
        .search()
        .slice(2, 4)
    )

def dwNetworkGameClient_getLocalPlayer() -> Pattern:
    return (
        Pattern("48 83 C0 ?? 48 8D 04 40 8B 0C C1 48 8B C2 89 0A C3 C7 02", cs2.engine)
        .search()
        .slice(3, 4)
        .add(0xE6)
    )

def dwNetworkGameClient_getMaxClients() -> Pattern:
    return (
        Pattern("8B 81 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC CC 8B 81 ?? ?? ?? ?? FF C0", cs2.engine)
        .search()
        .slice(2, 4)
    )

def dwNetworkGameClient_signOnState() -> Pattern:
    return (
        Pattern("44 8B 81 ?? ?? ?? ?? 48 8D 0D", cs2.engine)
        .search()
        .slice(3, 5)
    )

def dwWindowHeight() -> Pattern:
    return (
        Pattern("8B 05 ?? ?? ?? ?? 89 03", cs2.engine)
        .search()
        .rip(2, 6)
    )

def dwWindowWidth() -> Pattern:
    return (
        Pattern("8B 05 ?? ?? ?? ?? 89 07", cs2.engine)
        .search()
        .rip(2, 6)
    )