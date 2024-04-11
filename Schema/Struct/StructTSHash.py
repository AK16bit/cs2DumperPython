from typing import Optional, Dict, List, Generator
from typing_extensions import deprecated

from CS2 import cs2
from Schema.Offset import Offset


# class StructTSHash:
#     def __init__(self, tsHashAddr):
#         self.tsHashAddr = tsHashAddr
#
#     def memoryPool(self) -> "StructMemoryPool":
#         return StructMemoryPool(self.tsHashAddr)
#
#     def hashBucket(self) -> "HashBucket":
#         return StructHashBucket(self.tsHashAddr)

class StructMemoryPool:
    def __init__(self, memPoolAddr):
        self.memPoolAddr = memPoolAddr

        self._blockSize = None
        self._blocksPerBlob = None
        self. _growMode = None
        self._blocksAllocated = None
        self._blockAllocatedSize = None
        self._peakAlloc = None
        self._alignment = None
        self._blobsCount = None
        self._freeListTail = None
        self._freeListHead = None
        self._blobHead = None

    @property
    def blockSize(self) -> Optional[int]:
        if self._blockSize is None:
            self._blockSize = cs2.i32(self.memPoolAddr + Offset.StructTSHash.StructMemoryPool.BLOCK_SIZE)
        return self._blockSize

    @property
    def blocksPerBlob(self) -> Optional[int]:
        if self._blocksPerBlob is None:
            self._blocksPerBlob = cs2.i32(self.memPoolAddr + Offset.StructTSHash.StructMemoryPool.BLOCKS_PER_BLOB)
        return self._blocksPerBlob

    @property
    def growMode(self) -> Optional[int]:
        if self._growMode is None:
            self._growMode = cs2.i32(self.memPoolAddr + Offset.StructTSHash.StructMemoryPool.GROW_MODE)
        return self._growMode

    @property
    def blocksAlloc(self) -> Optional[int]:
        if self._blocksAllocated is None:
            self._blocksAllocated = cs2.i32(self.memPoolAddr + Offset.StructTSHash.StructMemoryPool.BLOCKS_ALLOC)
        return self._blocksAllocated

    @property
    def peakAlloc(self) -> Optional[int]:
        if self._peakAlloc is None:
            self._peakAlloc = cs2.i32(self.memPoolAddr + Offset.StructTSHash.StructMemoryPool.PEAK_ALLOC)
        return self._peakAlloc

    @property
    def blobsCount(self) -> Optional[int]:
        if self._blobsCount is None:
            self._blobsCount = cs2.u16(self.memPoolAddr + Offset.StructTSHash.StructMemoryPool.BLOBS_COUNT)
        return self._blobsCount

    @property
    def freeListTail(self) -> Optional[int]:
        if self._freeListTail is None:
            self._freeListTail = cs2.u64(self.memPoolAddr + Offset.StructTSHash.StructMemoryPool.FREE_LIST_TAIL)
        return self._freeListTail

    @property
    def freeListHead(self) -> Optional[int]:
        if self._freeListHead is None:
            self._freeListHead = cs2.u64(self.memPoolAddr + Offset.StructTSHash.StructMemoryPool.FREE_LIST_HEAD)
        return self._freeListHead




class StructHashBucket:
    def __init__(self, hashBucketAddr):
        self.hashBucketAddr = hashBucketAddr

        self._first = None
        self._firstUncomm = None


    @property
    def first(self) -> Optional[int]:
        if self._first is None:
            self._first = cs2.u64(self.hashBucketAddr + Offset.StructTSHash.StructHashBucket.FIRST)
        return self._first

    @property
    def firstUncomm(self) -> Optional[int]:
        if self._firstUncomm is None:
            self._firstUncomm = cs2.u64(self.hashBucketAddr + Offset.StructTSHash.StructHashBucket.FIRST_UNCOMM)
        return self._firstUncomm



class StructAllocatedClassBase:
    def __init__(self, allocAddr):
        self.allocAddr = allocAddr

        self._next = None
        self._data = None

    @property
    def next(self) -> Optional[int]:
        if self._next is None:
            self._next = cs2.u64(self.allocAddr + Offset.StructTSHash.StructHashBucket.StructAllocateClassBase.NEXT)
        return self._next

    @property
    def data(self) -> Optional[int]:
        if self._data is None:
            self._data = cs2.u64(self.allocAddr + Offset.StructTSHash.StructHashBucket.StructAllocateClassBase.DATA)
        return self._data


class StructUnAllocatedClassBase:
    def __init__(self, unAllocAddr):
        self.unAllocAddr = unAllocAddr

        self._next = None
        self._data = None

    @property
    def next(self) -> Optional[int]:
        if self._next is None:
            self._next = cs2.u64(self.unAllocAddr + Offset.StructTSHash.StructHashBucket.StructUnAllocateClassBase.NEXT)
        return self._next

    @property
    def data(self) -> Optional[int]:
        if self._data is None:
            self._data = cs2.u64(self.unAllocAddr + Offset.StructTSHash.StructHashBucket.StructUnAllocateClassBase.DATA)
        return self._data



