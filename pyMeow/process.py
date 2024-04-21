from pyMeow.pyMeow import r_ctype, process_running, enum_modules, open_process, process_exists, pid_exists, r_bytes, \
    r_string

from typing import Union, Generator, Any, Optional
from ctypes import c_int8, c_int16, c_int32, c_int64
from ctypes import c_uint8, c_uint16, c_uint32, c_uint64
from ctypes import c_bool, c_float

from pyMeow.module import Module
from pyMeow.pyMeowStruct import StructProcess


class ProcessMemory:
    process: StructProcess

    def _regularRead(self, address: int, ctype: Any, return_ctype: bool = False) -> Any:
        try: address = r_ctype(self.process, address, ctype())
        except Exception: return None

        if return_ctype: return address
        return address.value


    def i8(self, address: int, return_ctype: bool = False) -> Optional[Union[int, c_int8]]:
        return self._regularRead(address, c_int8, return_ctype)
    def i16(self, address: int, return_ctype: bool = False) -> Optional[Union[int, c_int16]]:
        return self._regularRead(address, c_int16, return_ctype)
    def i32(self, address: int, return_ctype: bool = False) -> Optional[Union[int, c_int32]]:
        return self._regularRead(address, c_int32, return_ctype)
    def i64(self, address: int, return_ctype: bool = False) -> Optional[Union[int, c_int64]]:
        return self._regularRead(address, c_int64, return_ctype)

    def u8(self, address: int, return_ctype: bool = False) -> Optional[Union[int, c_uint8]]:
        return self._regularRead(address, c_uint8, return_ctype)
    def u16(self, address: int, return_ctype: bool = False) -> Optional[Union[int, c_uint16]]:
        return self._regularRead(address, c_uint16, return_ctype)
    def u32(self, address: int, return_ctype: bool = False) -> Optional[Union[int, c_uint32]]:
        return self._regularRead(address, c_uint32, return_ctype)
    def u64(self, address: int, return_ctype: bool = False) -> Optional[Union[int, c_uint64]]:
        return self._regularRead(address, c_uint64, return_ctype)

    def f32(self, address: int, return_ctype: bool = False) -> Optional[Union[float, c_float]]:
        return self._regularRead(address, c_float, return_ctype)

    def bool(self, address: int, return_ctype: bool = False) -> Optional[Union[bool, c_bool]]:
        return self._regularRead(address, c_bool, return_ctype)

    def bytes(self, address: int, size: int = 50) -> Optional[Any]:
        try: bytes = r_bytes(self.process, address, size)
        except Exception: return None

        return bytes

    def str(self, address: int, size: int = 50) -> Optional[str]:
        try: string = r_string(self.process, address, size)
        except Exception: return None
        if not isinstance(string, str): return None

        return string




class Process(ProcessMemory):
    def __init__(self, process: Union[str, int, StructProcess]):
        if isinstance(process, str):
            if not process_exists(process):
                raise
            self.process = open_process(process)
        elif isinstance(process, int):
            if not pid_exists(process):
                raise
            self.process = open_process(process)
        else:
            self.process = process

    def __getitem__(self, item: str) -> Any: return self.process.get(item, None)
    def __repr__(self) -> str: return str(self.process)

    @property
    def name(self) -> str: return self.process.get("name")

    @property
    def pid(self) -> int: return self.process.get("pid")

    @property
    def handle(self) -> int: return self.process.get("handle")

    @property
    def running(self) -> bool: return process_running(self.process)

    def modules(self) -> Generator[Module, None, None]:
        modules = enum_modules(self.process)
        for moduleStruct in modules:
            yield Module(self.process, moduleStruct)