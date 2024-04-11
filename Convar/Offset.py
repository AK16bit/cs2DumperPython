from typing import Final


class Offset:
    class StructConvar:
        NAME: Final[int]        = 0x0
        DESCRIPTION: Final[int] = 0x20
        VALUE: Final[int]       = 0x40

    class StructConvarSystem:
        CONVAR_SYSTEM_PATTERN: Final[str]            = "4C 8D 3D ?? ?? ?? ?? 0F 28"
        CONVAR_SYSTEM_PATTERN_RIP_OFFSET: Final[int] = 0x3
        CONVAR_SYSTEM_PATTERN_RIP_LENGTH: Final[int] = 0x7
        CONVAR_COUNT: Final[int]                     = 0x56
        CONVAR_BASE: Final[int]                      = 0x40
        CONVAR_BASE_INDEX: Final[int]                = 0x10