from CS2 import cs2
from Schema.Struct.StructTSHash import StructMemoryPool, StructHashBucket
from Schema.Offset import Offset


class StructModule:
    def __init__(self, moduleAddr):
        self.moduleAddr = moduleAddr


    @property
    def name(self) -> str:
        return cs2.str(self.moduleAddr + Offset.StructModule.NAME)

    def classBindingsAddr(self) -> int:
        return self.moduleAddr + Offset.StructModule.CLASS_BINDINGS

    def enumBindingAddr(self) -> int:
        return self.moduleAddr + Offset.StructModule.ENUM_BINDINGS

    def memPool(self, bindingAddr: int) -> StructMemoryPool:
        return StructMemoryPool(bindingAddr + Offset.StructTSHash.MEMORY_POOL)

    def hashBucket(self, bindingAddr: int, index: int) -> StructHashBucket:
        return StructHashBucket(bindingAddr + Offset.StructTSHash.HASH_BUCKET + index * Offset.StructTSHash.HASH_BUCKET_INDEX)





