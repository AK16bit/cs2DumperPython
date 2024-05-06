from typing import Sequence, Callable

from CS2 import cs2
from Signature.Pattern import Pattern


# def inputsystemSignatures() -> Sequence[Callable]:
#     return (
#         dwInputSystem,
#     )


def inputsystemSignatures() -> Sequence[Pattern]:
    # dwInputSystem
    yield (
        Pattern("48 89 05 ?? ?? ?? ?? 48 8D 05", cs2.inputSystem)
        .search()
        .rip()
        .setName("dwInputSystem")
    )

# def dwInputSystem() -> Pattern:
#     return (
#         Pattern("48 89 05 ?? ?? ?? ?? 48 8D 05", cs2.inputSystem)
#         .search()
#         .rip()
#     )

