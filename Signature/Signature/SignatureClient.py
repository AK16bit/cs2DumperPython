from typing import Callable, Sequence

from CS2 import cs2
from Signature.Pattern import Pattern



# def clientSignatures() -> Sequence[Callable]:
#     return (
#         dwCSGOInput,
#         dwEntityList, dwGameEntitySystem, dwGameEntitySystem_getHighestEntityIndex,
#         dwGameRules, dwGlobalVars,
#         dwGlowManager,
#         dwLocalPlayerController, dwLocalPlayerPawn,
#         dwPlantedC4,
#         dwPrediction,
#         dwSensitivity, dwSensitivity_sensitivity,
#         dwViewAngles, dwViewMatrix, dwViewRender
#     )

def clientSignatures() -> Sequence[Pattern]:
    # dwCSGOInput
    yield (
        # Pattern("48 89 05 ?? ?? ?? ?? 48 8D 05 ?? ?? ?? ?? 48 89 0D ?? ?? ?? ?? 48 89 05 ?? ?? ?? ?? 48 8D 05", cs2.client)
        Pattern("48 8D 0D ?? ?? ?? ?? E8 ?? ?? ?? ?? 48 8D 05 ?? ?? ?? ?? 48 C7 05 ?? ?? ?? ?? ?? ?? ?? ?? 48 89 05 ?? ?? ?? ?? 48 8D 0D ?? ?? ?? ?? 48 8D 05", cs2.client)
        .search()
        .rip()
        .setName("dwCSGOInput")
    )

    # dwEntityList
    yield (
        Pattern("48 89 35 ?? ?? ?? ?? 48 85 F6", cs2.client)
        .search()
        .rip()
        .setName("dwEntityList")
    )

    # dwGameEntitySystem
    yield (
        Pattern("48 8B 1D ?? ?? ?? ?? 48 89 1D", cs2.client)
        .search()
        .rip()
        .setName("dwGameEntitySystem")
    )

    # dwGameEntitySystem_getHighestEntityIndex
    yield (
        Pattern("8B 81 ?? ?? ?? ?? 89 02 48 8B C2 C3 CC CC CC CC 48 89 5C 24 ?? 48 89 6C 24", cs2.client)
        .search()
        .slice(2, 4)
        .setName("dwGameEntitySystem_getHighestEntityIndex")
    )

    # dwGameRules
    yield (
        Pattern("48 89 1D ?? ?? ?? ?? FF 15 ?? ?? ?? ?? 84 C0", cs2.client)
        .search()
        .rip()
        .setName("dwGameRules")
    )

    # dwGlobalVars
    yield (
        Pattern("48 89 0D ?? ?? ?? ?? 48 89 41", cs2.client)
        .search()
        .rip()
        .setName("dwGlobalVars")
    )

    # dwGlowManager
    yield (
        Pattern("48 8B 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 8B 41", cs2.client)
        .search()
        .rip()
        .setName("dwGlowManager")
    )

    # dwLocalPlayerController
    yield (
        Pattern("48 89 05 ?? ?? ?? ?? 8B 9E", cs2.client)
        .search()
        .rip()
        .setName("dwLocalPlayerController")
    )

    # dwLocalPlayerPawn
    yield (
        Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 83 EC ?? 8B 0D", cs2.client)
        .search()
        .rip()
        .add(0x148)
        .setName("dwLocalPlayerPawn")
    )

    # dwPlantedC4
    yield (
        Pattern("48 8B 15 ?? ?? ?? ?? 41 FF C0", cs2.client)
        .search()
        .rip()
        .setName("dwPlantedC4")
    )

    # dwPrediction
    yield (
        Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 83 EC ?? 8B 0D", cs2.client)
        .search()
        .rip()
        .setName('dwPrediction')
    )

    # dwSensitivity
    yield (
        Pattern("48 8B 05 ?? ?? ?? ?? 48 8B 40 ?? F3 41 0F 59 F4", cs2.client)
        .search()
        .rip()
        .setName("dwSensitivity")
    )

    # dwSensitivity_sensitivity
    yield (
        Pattern("FF 50 ?? 4C 8B C6 48 8D 55 ?? 48 8B CF E8 ?? ?? ?? ?? 84 C0 0F 85 ?? ?? ?? ?? 4C 8D 45 ?? 8B D3 48 8B CF E8 ?? ?? ?? ?? E9 ?? ?? ?? ?? F3 0F 10 06", cs2.client)
        .search()
        .slice(2, 3)
        .setName("dwSensitivity_sensitivity")
    )

    # dwViewAngles
    yield (
        Pattern("48 8D 0D ?? ?? ?? ?? E8 ?? ?? ?? ?? 48 8D 05 ?? ?? ?? ?? 48 C7 05 ?? ?? ?? ?? ?? ?? ?? ?? 48 89 05 ?? ?? ?? ?? 48 8D 0D ?? ?? ?? ?? 48 8D 05", cs2.client)
        .search()
        .rip()
        .add(0x5418)
        .setName("dwViewAngles")
    )

    # dwViewMatrix
    yield (
        Pattern("48 8D 0D ?? ?? ?? ?? 48 C1 E0 06", cs2.client)
        .search()
        .rip()
        .setName("dwViewMatrix")
    )

    # dwViewRender
    yield (
        Pattern("48 89 05 ?? ?? ?? ?? 48 8B C8 48 85 C0", cs2.client)
        .search()
        .rip()
        .setName("dwViewRender")
    )

    # dwWeaponC4
    yield (
        Pattern("48 8B 15 ?? ?? ?? ?? FF C0 89 05 ?? ?? ?? ?? 48 8B C6 48 89 34 EA 48 8B 6C 24 ?? C6 86 ?? ?? ?? ?? ?? 80 BE", cs2.client)
        .search()
        .rip()
        .setName("dwWeaponC4")
    )







# def dwCSGOInput() -> Pattern:
#     return (
#         Pattern("48 89 05 ?? ?? ?? ?? 48 8D 05 ?? ?? ?? ?? 48 89 0D ?? ?? ?? ?? 48 89 05 ?? ?? ?? ?? 48 8D 05", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwEntityList() -> Pattern:
#     return (
#         Pattern("48 89 35 ?? ?? ?? ?? 48 85 F6", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwGameEntitySystem() -> Pattern:
#     return (
#         Pattern("48 8B 1D ?? ?? ?? ?? 48 89 1D", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwGameEntitySystem_getHighestEntityIndex() -> Pattern:
#     return (
#         Pattern("8B 81 ?? ?? ?? ?? 89 02 48 8B C2 C3 CC CC CC CC 48 89 5C 24 ?? 48 89 6C 24", cs2.client)
#         .search()
#         .slice(2, 4)
#     )
#
# def dwGameRules() -> Pattern:
#     return (
#         Pattern("48 89 0D ?? ?? ?? ?? 8B 0D ?? ?? ?? ?? FF 15", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwGlobalVars() -> Pattern:
#     return (
#         Pattern("48 89 0D ?? ?? ?? ?? 48 89 41", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwGlowManager() -> Pattern:
#     return (
#         Pattern("48 8B 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 8B 41", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwLocalPlayerController() -> Pattern:
#     return (
#         Pattern("48 8B 05 ?? ?? ?? ?? 48 85 C0 74 ?? 8B 88", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwLocalPlayerPawn() -> Pattern:
#     return (
#         Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 83 EC ?? 8B 0D", cs2.client)
#         .search()
#         .rip()
#         .add(0x138)
#     )
#
# def dwPlantedC4() -> Pattern:
#     return (
#         Pattern("48 8B 15 ?? ?? ?? ?? FF C0 48 8D 4C 24", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwPrediction() -> Pattern:
#     return (
#         Pattern("48 8D 05 ?? ?? ?? ?? C3 CC CC CC CC CC CC CC CC 48 83 EC ?? 8B 0D", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwSensitivity() -> Pattern:
#     return (
#         Pattern("48 8B 05 ?? ?? ?? ?? 48 8B 40 ?? F3 41 0F 59 F4", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwSensitivity_sensitivity() -> Pattern:
#     return (
#         Pattern("FF 50 ?? 4C 8B C6 48 8D 55 ?? 48 8B CF E8 ?? ?? ?? ?? 84 C0 0F 85 ?? ?? ?? ?? 4C 8D 45 ?? 8B D3 48 8B CF E8 ?? ?? ?? ?? E9 ?? ?? ?? ?? F3 0F 10 06", cs2.client)
#         .search()
#         .slice(2, 3)
#     )
#
# def dwViewAngles() -> Pattern:
#     return (
#         Pattern("48 8B 05 ?? ?? ?? ?? 48 8B 40 ?? F3 41 0F 59 F4", cs2.client)
#         .search()
#         .rip()
#         .add(0x5390)
#     )
#
# def dwViewMatrix() -> Pattern:
#     return (
#         Pattern("48 8D 05 ?? ?? ?? ?? 48 8B D3 4C 8D 05", cs2.client)
#         .search()
#         .rip()
#     )
#
# def dwViewRender() -> Pattern:
#     return (
#         Pattern("48 89 05 ?? ?? ?? ?? 48 8B C8 48 85 C0", cs2.client)
#         .search()
#         .rip()
#     )
