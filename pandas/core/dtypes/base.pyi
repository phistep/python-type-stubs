from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries
from pandas.errors import AbstractMethodError as AbstractMethodError
from typing import Any, List, Optional, Type

class ExtensionDtype:
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: Any) -> bool: ...
    @property
    def na_value(self): ...
    @property
    def type(self) -> Type: ...
    @property
    def kind(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def names(self) -> Optional[List[str]]: ...
    @classmethod
    def construct_array_type(cls) -> None: ...
    @classmethod
    def construct_from_string(cls: Any, string: str) -> Any: ...
    @classmethod
    def is_dtype(cls: Any, dtype: Any) -> bool: ...
