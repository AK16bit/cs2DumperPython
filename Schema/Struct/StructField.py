from typing import Optional

from CS2 import cs2
from Schema.Offset import Offset

class StructField:
    def __init__(self, fieldAddr):
        self.fieldAddr = fieldAddr

        self._name = None
        self._schemaValue = None
        self._value = None

    @property
    def name(self) -> Optional[str]:
        if self._name is None:
            strAddr = cs2.u64(self.fieldAddr + Offset.StructField.NAME)
            self._name = cs2.str(strAddr, 128)
        return self._name

    @property
    def schemaType(self) -> Optional[int]:
        if self._schemaValue is None:
            self._schemaValue = cs2.u64(self.fieldAddr + Offset.StructField.SCHEMA_TYPE)
        return self._schemaValue

    @property
    def value(self) -> Optional[int]:
        if self._value is None:
            self._value = cs2.i32(self.fieldAddr + Offset.StructField.VALUE)
        return self._value
