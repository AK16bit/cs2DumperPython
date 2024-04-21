from typing import Final


class Offset:
    class StructMetadata:
        NAME: Final[int]          = 0x0
        NETWORK_VALUE: Final[int] = 0x8
        class StructNetworkValue:
            NAME: Final[int]      = 0x0
            INT: Final[int]       = 0x8
            FLOAT: Final[int]     = 0x10
            VAR_VALUE: Final[int] = 0x20
            class StructVarValue:
                NAME: Final[int]      = 0x0
                TYPE_NAME: Final[int] = 0x8


    class StructMember:
        NAME: Final[int]           = 0x0
        VALUE: Final[int]          = 0x8
        METADATA_COUNT: Final[int] = 0x10
        METADATA: Final[int]       = 0x18

    class StructField:
        NAME: Final[int]           = 0x0
        SCHEMA_TYPE: Final[int]    = 0x8
        VALUE: Final[int]          = 0x10
        METADATA_COUNT: Final[int] = 0x14
        METADATA: Final[int]       = 0x18


    class StructEnum:
        BASE: Final[int]                  = 0x0
        NAME: Final[int]                  = 0x08
        MODULE_NAME: Final[int]           = 0x10
        SIZE: Final[int]                  = 0x18
        ENUMERATORS_COUNT: Final[int]     = 0x1C
        STATIC_METADATA_COUNT: Final[int] = 0x1E
        ENUMERATORS: Final[int]           = 0x20
        STATIC_METADATA: Final[int]       = 0x28
        TYPE_SCOPE: Final[int]            = 0x30

        ENUMERATORS_INDEX: Final[int]     = 0x20

    class StructClass:
        BASE: Final[int]                  = 0x0
        NAME: Final[int]                  = 0x08
        MODULE_NAME: Final[int]           = 0x10
        SIZE: Final[int]                  = 0x18
        FIELDS_COUNT: Final[int]          = 0x1C
        STATIC_FIELDS_COUNT: Final[int]   = 0x1E
        STATIC_METADATA_COUNT: Final[int] = 0x20
        ALIGNMENT: Final[int]             = 0x22
        HAS_BASE_CLASS: Final[int]        = 0x23
        TOTAL_CLASS_SIZE: Final[int]      = 0x24
        DERIVED_CLASS_SIZE: Final[int]    = 0x26
        FIELDS: Final[int]                = 0x28
        STATIC_FIELDS: Final[int]         = 0x30
        BASE_ADDRESS: Final[int]          = 0x38
        STATIC_METADATA: Final[int]       = 0x48
        TYPE_SCOPE: Final[int]            = 0x50
        SCHEMA_TYPE: Final[int]           = 0x58

        FIELDS_INDEX: Final[int]          = 0x20
        METADATA_INDEX: Final[int]        = 0x20


    class StructTSHash:
        MEMORY_POOL: Final[int] = 0x0
        class StructMemoryPool:
            BLOCK_SIZE: Final[int]      = 0x0
            BLOCKS_PER_BLOB: Final[int] = 0x4
            GROW_MODE: Final[int]       = 0x8
            BLOCKS_ALLOC: Final[int]    = 0xC
            PEAK_ALLOC: Final[int]      = 0x10
            ALIGNMENT: Final[int]       = 0x14
            BLOBS_COUNT: Final[int]     = 0x16
            FREE_LIST_TAIL: Final[int]  = 0x18
            FREE_LIST_HEAD: Final[int]  = 0x20
            BLOB_HEAD: Final[int]       = 0x70

        HASH_BUCKET: Final[int]       = 0x80
        HASH_BUCKET_INDEX: Final[int] = 0x28
        HASH_BUCKET_SIZE: Final[int]  = 0x100
        class StructHashBucket:
            FIRST: Final[int]        = 0x18
            FIRST_UNCOMM: Final[int] = 0x20

            class StructAllocateClassBase:
                NEXT: Final[int] = 0x0
                DATA: Final[int] = 0x10
            class StructUnAllocateClassBase:
                NEXT: Final[int] = 0x8
                DATA: Final[int] = 0x10

    class StructModule:
        NAME: Final[int]           = 0x08
        CLASS_BINDINGS: Final[int] = 0x5C0
        ENUM_BINDINGS: Final[int]  = 0x2E50


    class StructSchemaSystem:
        SCHEMA_SYSTEM_PATTERN: Final[str]            = "48 89 05 ?? ?? ?? ?? 4C 8D 45"
        SCHEMA_SYSTEM_PATTERN_RIP_OFFSET: Final[int] = 0x3
        SCHEMA_SYSTEM_PATTERN_RIP_LENGTH: Final[int] = 0x7
        MODULES_COUNT: Final[int]                    = 0x190
        MODULE_BASE: Final[int]                      = 0x198
        MODULE_BASE_INDEX: Final[int]                = 0x08
