import pickle as pkl
from pandas import DataFrame as DataFrame, Index as Index, Series as Series
from typing import Any, Optional

def load_reduce(self) -> None: ...

class _LoadSparseSeries:
    def __new__(cls: Any) -> Series: ...

class _LoadSparseFrame:
    def __new__(cls: Any) -> DataFrame: ...

class Unpickler(pkl._Unpickler):
    def find_class(self, module: Any, name: Any): ...

def load_newobj(self) -> None: ...
def load_newobj_ex(self) -> None: ...
def load(fh: Any, encoding: Optional[str]=..., is_verbose: bool=...) -> Any: ...
