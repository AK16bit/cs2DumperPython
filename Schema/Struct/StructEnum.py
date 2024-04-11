from CS2 import cs2
from Schema.Offset import Offset


class StructEnum:
    def __init__(self, enumAddr: int):
        self.enumAddr = enumAddr

        self._name = None
        self._moduleName = None

        self._enumeratorsCount = None
        self._staticMetaDataCount = None

        self._enumerators = None
        self._staticMetaData = None


    @property
    def name(self) -> str:
        if self._name is None:
            strAddr = cs2.u64(self.enumAddr + Offset.StructClass.NAME)
            self._name = cs2.str(strAddr, 128)
        return self._name

    @property
    def moduleName(self) -> str:
        if self._moduleName is None:
            strAddr = cs2.u64(self.enumAddr + Offset.StructClass.MODULE_NAME)
            self._moduleName = cs2.str(strAddr, 128)
        return self._moduleName


    @property
    def enumeratorsCount(self) -> int:
        if self._enumeratorsCount is None:
            self._enumeratorsCount = cs2.i32(self.enumAddr + Offset.StructEnum.ENUMERATORS_COUNT)
        return self._enumeratorsCount

    @property
    def staticMetaDataCount(self) -> int:
        if self._staticMetaDataCount is None:
            self._staticMetaDataCount = cs2.i32(self.enumAddr + Offset.StructEnum.STATIC_METADATA_COUNT)
        return self._staticMetaDataCount


    @property
    def enumerators(self) -> int:
        if self._enumerators is None:
            self._enumerators = cs2.u64(self.enumAddr + Offset.StructEnum.ENUMERATORS)
        return self._enumerators


    @property
    def staticMetaData(self) -> int:
        if self._staticMetaData is None:
            self._staticMetaData = cs2.u64(self.enumAddr + Offset.StructEnum.STATIC_METADATA)
        return self._staticMetaData



