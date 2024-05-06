from typing import TypedDict, List, Dict, Union


class ContainerSignature(TypedDict):
    name: str
    value: int
    config: Dict[str, Union[str, int, List[Dict[str, Union[str, int]]]]]

class ContainerModule(TypedDict):
    name: str
    signatures: List[ContainerSignature]