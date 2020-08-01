import numpy as np
from pandas._libs import lib as lib
from pandas._typing import Scalar as Scalar
from pandas.core.algorithms import take as take
from pandas.core.arrays import ExtensionArray as ExtensionArray, ExtensionOpsMixin as ExtensionOpsMixin
from pandas.core.dtypes.common import is_integer as is_integer, is_object_dtype as is_object_dtype, is_string_dtype as is_string_dtype
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.indexers import check_array_indexer as check_array_indexer
from typing import Any, Optional

class BaseMaskedArray(ExtensionArray, ExtensionOpsMixin):
    def __getitem__(self, item: Any): ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __invert__(self): ...
    def to_numpy(self, dtype: Any=..., copy: Any=..., na_value: Scalar=...) -> Any: ...
    __array_priority__: int = ...
    def __array__(self, dtype: Any=...) -> np.ndarray: ...
    def __arrow_array__(self, type: Optional[Any] = ...): ...
    def isna(self): ...
    @property
    def nbytes(self) -> int: ...
    def take(self, indexer: Any, allow_fill: bool = ..., fill_value: Optional[Any] = ...): ...
    def copy(self): ...
    def value_counts(self, dropna: bool = ...): ...
