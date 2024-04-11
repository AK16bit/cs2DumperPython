from CS2 import cs2
from Schema.Offset import Offset


class StructMetadata:
    def __init__(self, metadataAddr: int):
        self.metadataAddr = metadataAddr

        self._name = None
        self._networkValue = None

    @property
    def name(self) -> str:
        if self._name is None:
            strAddr = cs2.u64(self.metadataAddr + Offset.StructMetadata.NAME)
            self._name = cs2.str(strAddr, 128)
        return self._name

    @property
    def networkValue(self) -> int:
        if self._networkValue is None:
            netVarAddr = cs2.u64(self.metadataAddr + Offset.StructMetadata.NETWORK_VALUE)
            self._networkValue = cs2.u64(netVarAddr)
        return self._networkValue



