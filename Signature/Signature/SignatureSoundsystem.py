from typing import Sequence, Callable

from CS2 import cs2
from Signature.Pattern import Pattern


def soundsystemSignatures() -> Sequence[Pattern]:
    # dwSoundSystem
    yield (
        Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 89 15", cs2.soundsystem)
        .search()
        .rip()
        .setName("dwSoundSystem")
    )

    # dwSoundSystem_engineViewData
    yield (
        Pattern("0F 11 47 ?? 0F 10 4B", cs2.soundsystem)
        .search()
        .slice(3, 4)
        .setName("dwSoundSystem_engineViewData")
    )

