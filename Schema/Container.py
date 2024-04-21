from typing import TypedDict, Any, Optional

from Schema.Struct.StructClass import StructClass
from Schema.Struct.StructEnum import StructEnum
from Schema.Struct.StructField import StructField
from Schema.Struct.StructMember import StructMember
from Schema.Struct.StructMetadata import StructMetadata
from Schema.Struct.StructModule import StructModule


class ContainerMetadata(TypedDict):
    name: str
    value: int
    struct: Optional[StructMetadata]

class ContainerMember(TypedDict):
    name: str
    value: int
    struct: Optional[StructMember]

class ContainerField(TypedDict):
    name: str
    value: int
    struct: Optional[StructField]


class ContainerEnum(TypedDict):
    name: str
    members: Any
    struct: Optional[StructEnum]

class ContainerClass(TypedDict):
    name: str
    fields: Any
    metadata: Any
    struct: Optional[StructClass]


class ContainerModule(TypedDict):
    name: str
    classes: Any
    enums: Any
    struct: Optional[StructModule]

class ContainerSchema:
    ...
    # client_dll: ContainerModule
    # engine2_dll: ContainerModule