from typing import Final


class Offset:
    class StructButton:
        NAME: Final[int]  = 0x8
        STATE: Final[int] = 0x30
    class StructButtonSystem:
        BUTTON_SYSTEM_PATTERN: Final[str] = "48 8B 15 ?? ?? ?? ?? 48 85 D2 74 ?? 0F 1F 40"
        BUTTON_SYSTEM_PATTERN_RIP_OFFSET: Final[int] = 0x3
        BUTTON_SYSTEM_PATTERN_RIP_LENGTH: Final[int] = 0x7

        BUTTON_NEXT: Final[int]                      = 0x88
