from typing import Optional

from CS2 import cs2
from Schema.Offset import Offset


class StructClass:
    def __init__(self, classAddr: int):
        self.classAddr = classAddr

        self._name = None
        self._moduleName = None

        self._fieldCount = None
        self._staticFieldCount = None
        self._staticMetaDataCount = None

        self._fields = None
        self._staticFields = None
        self._staticMetaData = None

        self._hasBaseClass = None
        self._baseClassAddr = None


    @property
    def name(self) -> str:
        if self._name is None:
            strAddr = cs2.u64(self.classAddr + Offset.StructClass.NAME)
            self._name = cs2.str(strAddr, 128)
        return self._name

    @property
    def moduleName(self) -> str:
        if self._moduleName is None:
            strAddr = cs2.u64(self.classAddr + Offset.StructClass.MODULE_NAME)
            self._moduleName = cs2.str(strAddr, 128)
        return self._moduleName


    @property
    def fieldsCount(self) -> int:
        if self._fieldCount is None:
            self._fieldCount = cs2.i16(self.classAddr + Offset.StructClass.FIELDS_COUNT)
        return self._fieldCount

    @property
    def staticFieldsCount(self) -> int:
        if self._staticFieldCount is None:
            self._staticFieldCount = cs2.i16(self.classAddr + Offset.StructClass.STATIC_FIELDS_COUNT)
        return self._staticFieldCount

    @property
    def staticMetaDataCount(self) -> int:
        if self._staticMetaDataCount is None:
            self._staticMetaDataCount = cs2.i16(self.classAddr + Offset.StructClass.STATIC_METADATA_COUNT)
        return self._staticMetaDataCount


    @property
    def fields(self) -> int:
        if self._fields is None:
            self._fields = cs2.u64(self.classAddr + Offset.StructClass.FIELDS)
        return self._fields

    @property
    def staticFields(self) -> int:
        if self._staticFields is None:
            self._staticFields = cs2.u64(self.classAddr + Offset.StructClass.STATIC_FIELDS)
        return self._staticFields

    @property
    def staticMetaData(self) -> int:
        if self._staticMetaData is None:
            self._staticMetaData = cs2.u64(self.classAddr + Offset.StructClass.STATIC_METADATA)
        return self._staticMetaData


    @property
    def hasBaseClass(self) -> bool:
        if self._hasBaseClass is None:
            self._hasBaseClass = cs2.bool(self.classAddr + Offset.StructClass.HAS_BASE_CLASS)
        return self._hasBaseClass

    @property
    def baseClassAddr(self) -> int:
        if self._baseClassAddr is None:
            baseClassAddr = cs2.u64(self.classAddr + Offset.StructClass.BASE_ADDRESS)
            baseClassAddr = cs2.u64(baseClassAddr + Offset.StructClass.FIELDS_INDEX)
            self._baseClassAddr = baseClassAddr
        return self._baseClassAddr










