from typing import TypedDict, List



class ContainerSignature(TypedDict):
    name: str
    value: int

class ContainerModule(TypedDict):
    name: str
    signatures: List[ContainerSignature]