from typing import Union, Any, Optional, List

from pyMeow.pyMeow import open_process, module_exists, get_module, aob_scan_module
from pyMeow.pyMeowStruct import StructProcess, StructModule


class Module:
    def __init__(self, process: Union[str, int, StructProcess], module: Union[str, StructModule]):
        if isinstance(process, str) or isinstance(process, int):
            self.process = open_process(process)
        else:
            self.process = process

        if isinstance(module, str):
            if not module_exists(self.process, module): raise
            self.module = get_module(self.process, module)
        else:
            self.module = module

    def __getitem__(self, item: str) -> Any: return self.module.get(item, None)
    def __repr__(self) -> str: return str(self.module)

    @property
    def name(self) -> str: return self.module.get("name")

    @property
    def base(self) -> int: return self.module.get("base")

    @property
    def end(self) -> int: return self.module.get("end")

    @property
    def size(self) -> int: return self.module.get("size")

    def pattern(self, pattern, relative: bool = False, single: bool = True) -> Optional[Union[int, List[int]]]:
        patterns = aob_scan_module(self.process, self.name, pattern, relative=relative, single=single)
        if len(patterns) == 0: return None

        if single: return patterns[0]
        return patterns
