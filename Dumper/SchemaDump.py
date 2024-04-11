from functools import lru_cache
from time import perf_counter
from typing import Generator, List, Iterable, Tuple, Optional, Dict, Any, Union

from CS2 import cs2
from Schema.Container import ContainerModule, ContainerClass, ContainerField, ContainerMember, ContainerEnum, ContainerMetadata
from Schema.Struct.StructClass import StructClass
from Schema.Struct.StructEnum import StructEnum
from Schema.Struct.StructField import StructField
from Schema.Struct.StructMember import StructMember
from Schema.Struct.StructMetadata import StructMetadata
from Schema.Struct.StructModule import StructModule
from Schema.Struct.StructSchemaSystem import StructSchemaSystem
from Schema.Struct.StructTSHash import StructHashBucket, StructUnAllocatedClassBase, StructAllocatedClassBase
from Schema.Offset import Offset
from utils import int2hex, logger, timeUseInfo, errorButDontCloseWindow


# def dumpSchemaUnused():
#     schemaSysAddr = getSchemaSysAddr()
#     schemaSysStruct = StructSchemaSystem(schemaSysAddr)
#
#     moduleCnt = schemaSysStruct.moduleCnt()
#     modulesAddr = [schemaSysStruct.moduleAddr(index) for index in range(moduleCnt)]
#
#
#     for moduleAddr in modulesAddr:
#         moduleStruct = StructModule(moduleAddr)
#         moduleName = moduleStruct.name
#
#         if moduleName != "client.dll": continue
#
#         classBindingsAddr = moduleStruct.classBindingsAddr()
#         print("classBindingsAddr: %s" % int2hex(classBindingsAddr))
#         classBindingStruct = StructRBTree(classBindingsAddr)
#         # print("entry Count: %s" % classBindingStruct.entryCount())
#
#
#         print("element: %s" % int2hex(cs2.u64(classBindingsAddr + 0x08)))
#         print("element: %s" % int2hex(classBindingStruct.elements()))
#
#         # 0x241EC4F09C8
#
#         # 0x241EC420000
#         print()
#         for elementIndex in range(0, 1 << 2):
#             # declared_classes.elements 0x241EC420000
#             # declared_class 2482159878144
#             # declared_class.value 0x7FFED86EB9CB
#             # declared_class.value.value 0x241EBF32AF0
#             # declared_class.value.value.cast 2482154711792 0x241EBF32AF0
#
#             print("elementIndex:", elementIndex)
#             ...
#
#             element = classBindingStruct.elements() + 0x18 * elementIndex
#             # elementValue1 = cs2.u64(element + 0x08)
#             elementValue2 = cs2.u64(element + 0x10)  # 0x08 + 0x08
#             binding_ptr = cs2.u64(elementValue2)
#             binding_ptr2 = cs2.u64(binding_ptr + 0x20)
#
#
#             print("element:", element, int2hex(element))
#             # print("elementValue1:", elementValue1, int2hex(elementValue1))
#             print("elementValue2:", elementValue2, int2hex(elementValue2))
#             print("binding_ptr:", binding_ptr, int2hex(binding_ptr))
#
#
#
#
#             print()

@timeUseInfo
@errorButDontCloseWindow
def dumpSchema() -> None:
    schemaSysAddr = readSchemaSysAddr()
    schemaSysStruct = StructSchemaSystem(schemaSysAddr)

    modulesCount = schemaSysStruct.modulesCount()
    modulesAddr: Generator[int, None, None] = (schemaSysStruct.moduleAddr(index) for index in range(modulesCount))

    modulesCtr: Generator[ContainerModule, None, None] = (readModule(moduleAddr) for moduleAddr in modulesAddr)

    for moduleCtr in modulesCtr:
        timeUseCounter = perf_counter()

        moduleStruct = moduleCtr.get("struct")
        classesAddr = moduleCtr.get("classes")
        enumsAddr = moduleCtr.get("enums")

        logger.debug("Module: %s (%s)" % (
            moduleStruct.name,
            int2hex(moduleStruct.moduleAddr)
        ))

        readClass.cache_clear()
        readClassAddrAndBaseClassAddr.cache_clear()

        # classesAddr = {
        #     classAddr for classesAddrList in
        #     [readClassAddrAndBaseClassAddr(classAddr) for classAddr in classesAddr]
        #     for classAddr in classesAddrList
        # }

        logger.debug(" · Classes (Count: %s) -> Binding: %s" % (
            len(classesAddr),
            int2hex(moduleStruct.classBindingsAddr())
        ))
        for classAddr in classesAddr:
            classCtr = readClass(classAddr)
            fields = classCtr.get("fields")
            metadata = classCtr.get("metadata")

            logger.debug(" ·  · %s -> Class: %s (Fields Count: %s) (Metadatas Count: %s)" % (
                int2hex(classCtr.get("struct").classAddr),
                classCtr.get("name"),
                len(fields),
                len(metadata)
            ))

            # print(fields)

        logger.debug(" · Enums (Count: %s) -> Binding: %s" % (
            len(enumsAddr),
            int2hex(moduleStruct.enumBindingAddr())
        ))
        for enumAddr in enumsAddr:
            enumCtr = readEnum(enumAddr)

            members = enumCtr.get("members")

            logger.debug(" ·  · %s -> Enum: %s (Members Count: %s)" % (
                int2hex(enumCtr.get("struct").enumAddr),
                enumCtr.get("name"),
                len(members)
            ))

        timeUse = (perf_counter() - timeUseCounter) * 1000
        logger.debug("Module: %s Dump Finished in %s ms" % (moduleStruct.name, timeUse))



def readSchemaSysAddr() -> Optional[int]:
    try:
        schemaSysAddr = cs2.schemaSystem.pattern(Offset.StructSchemaSystem.SCHEMA_SYSTEM_PATTERN)
        schemaSysAddr = schemaSysAddr + cs2.i32(schemaSysAddr + Offset.StructSchemaSystem.SCHEMA_SYSTEM_PATTERN_RIP_OFFSET) + Offset.StructSchemaSystem.SCHEMA_SYSTEM_PATTERN_RIP_LENGTH
    except Exception:
        logger.error("Schema: Schema System Pattern Invalid!")
        return None

    return schemaSysAddr


def readModule(moduleAddr: int) -> ContainerModule:
    moduleStruct = StructModule(moduleAddr)
    moduleName = moduleStruct.name.replace(".", "_")
    # if moduleName != "client_dll": return moduleName, list()

    classBindingAddr = moduleStruct.classBindingsAddr()
    allocClasses = readAllocAddrList(moduleStruct, classBindingAddr)
    unAllocClasses = readUnAllocAddrList(moduleStruct, classBindingAddr)
    curClasses = allocClasses if len(allocClasses) > len(unAllocClasses) else unAllocClasses

    enumBindingAddr = moduleStruct.enumBindingAddr()
    allocEnums = readAllocAddrList(moduleStruct, enumBindingAddr)
    unAllocEnums = readUnAllocAddrList(moduleStruct, enumBindingAddr)
    curEnums = allocEnums if len(allocEnums) > len(unAllocEnums) else unAllocEnums

    return ContainerModule(name=moduleName, classes=curClasses, enums=curEnums, struct=moduleStruct)




def readAllocAddrList(moduleStruct: StructModule, bindingAddr: int) -> List[int]:
    allocList: List[int] = list()

    memPoolStruct = moduleStruct.memPool(bindingAddr)
    allocAddr = memPoolStruct.freeListHead

    while allocAddr:
        allocAddrStruct = StructAllocatedClassBase(allocAddr)
        if allocAddrStruct.data:
            allocList.append(allocAddrStruct.data)

        allocAddr = allocAddrStruct.next
        if len(allocList) >= memPoolStruct.peakAlloc: break

    return allocList


def readUnAllocAddrList(moduleStruct: StructModule, bindingAddr: int) -> List[int]:
    unAllocList: List[int] = list()
    memPoolStruct = moduleStruct.memPool(bindingAddr)
    buckets: Generator[StructHashBucket, None, None] = (moduleStruct.hashBucket(bindingAddr, index) for index in range(Offset.StructTSHash.HASH_BUCKET_SIZE))

    for bucket in buckets:
        unAllocAddr = bucket.firstUncomm

        while unAllocAddr:
            unAllocAddrStruct = StructUnAllocatedClassBase(unAllocAddr)
            if unAllocAddrStruct.data:
                unAllocList.append(unAllocAddrStruct.data)

            unAllocAddr = unAllocAddrStruct.next
            if len(unAllocList) >= memPoolStruct.blocksAlloc: break
        if len(unAllocList) >= memPoolStruct.blocksAlloc: break

    return unAllocList


@lru_cache(maxsize=512)
def readClassAddrAndBaseClassAddr(classAddr: int) -> List[int]:
    classesAddr = list()
    classesAddr.append(classAddr)

    while classAddr:
        classStruct = StructClass(classAddr)

        if not classStruct.hasBaseClass: break
        if classStruct.baseClassAddr in classesAddr: break
        if not classStruct.name: break
        if not classStruct.moduleName: break

        classesAddr.append(classAddr)
        classAddr = classStruct.baseClassAddr

    return classesAddr


@lru_cache(maxsize=512)
def readClass(classAddr: Union[int, StructClass]) -> ContainerClass:
    classStruct = StructClass(classAddr)
    className = classStruct.name

    fields = readClassField(classStruct.fields, classStruct.fieldsCount)
    metadata = readClassMetadata(classStruct.staticMetaData, classStruct.staticMetaDataCount)

    return ContainerClass(name=className, fields=fields, metadata=metadata, struct=classStruct)


def readEnum(enumAddr: Union[int, StructEnum]) -> ContainerEnum:
    enumStruct = StructEnum(enumAddr)
    enumName = enumStruct.name

    members = readMember(enumStruct.enumerators, enumStruct.enumeratorsCount)

    return ContainerEnum(name=enumName, members=members, struct=enumStruct)



def readClassField(fieldsBaseAddr: int, fieldsCount: int) -> List[ContainerField]:
    fields = list()

    for index in range(fieldsCount):
        fieldAddr = fieldsBaseAddr + index * Offset.StructClass.FIELDS_INDEX
        fieldStruct = StructField(fieldAddr)

        if fieldStruct.name is None: break
        fields.append(ContainerField(name=fieldStruct.name, value=fieldStruct.value, struct=fieldStruct))
    return fields


def readMember(membersBaseAddr: int, membersCount: int) -> List[ContainerMember]:
    members = list()

    for index in range(membersCount):
        memberAddr = membersBaseAddr + index * Offset.StructEnum.ENUMERATORS_INDEX
        memberStruct = StructMember(memberAddr)

        if memberStruct.name is None: break
        members.append(ContainerMember(name=memberStruct.name, value=memberStruct.value, struct=memberStruct))
    return members


def readClassMetadata(metadataBaseAddr: int, metadataCount: int) -> List[ContainerMetadata]:
    metadata = list()
    return metadata

    for index in range(metadataCount):
        metadataAddr = metadataBaseAddr + index * Offset.StructClass.METADATA_INDEX
        metadataStruct = StructMetadata(metadataAddr)

        netVarAddr = metadataStruct.networkValue
        netVarStruct = cs2.u64(netVarAddr)
        match metadataStruct.name:
            case "MNetworkChangeCallback":
                nameAddr = cs2.u64(netVarStruct + Offset.StructMetadata.StructNetworkValue.NAME)
                name = cs2.str(nameAddr)

                metadata.append(dict(name=name))
            case "MNetworkVarNames":
                varValue = cs2.u64(netVarStruct + Offset.StructMetadata.StructNetworkValue.VAR_VALUE)

                nameAddr = cs2.u64(varValue + Offset.StructMetadata.StructNetworkValue.StructVarValue.NAME)
                name = cs2.str(nameAddr)

                typeNameAddr = cs2.u64(varValue + Offset.StructMetadata.StructNetworkValue.StructVarValue.TYPE_NAME)
                typeName = cs2.str(typeNameAddr)

                metadata.append(dict(name=name, typeName=typeName))
            case _:
                metadata.append(dict(name=metadataStruct.name))

    return metadata












