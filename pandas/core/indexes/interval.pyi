import numpy as np
from pandas._config import get_option as get_option
from pandas._libs import Timedelta as Timedelta, Timestamp as Timestamp, lib as lib
from pandas._libs.interval import Interval as Interval, IntervalMixin as IntervalMixin, IntervalTree as IntervalTree
from pandas._typing import AnyArrayLike as AnyArrayLike
from pandas.core.algorithms import take_1d as take_1d
from pandas.core.arrays.interval import IntervalArray as IntervalArray
from pandas.core.dtypes.cast import find_common_type as find_common_type, infer_dtype_from_scalar as infer_dtype_from_scalar, maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_categorical as is_categorical, is_datetime64tz_dtype as is_datetime64tz_dtype, is_datetime_or_timedelta_dtype as is_datetime_or_timedelta_dtype, is_dtype_equal as is_dtype_equal, is_float as is_float, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_interval_dtype as is_interval_dtype, is_list_like as is_list_like, is_number as is_number, is_object_dtype as is_object_dtype, is_scalar as is_scalar
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna
from pandas.core.indexes.base import Index as Index, InvalidIndexError as InvalidIndexError, default_pprint as default_pprint, ensure_index as ensure_index, maybe_extract_name as maybe_extract_name
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex, date_range as date_range
from pandas.core.indexes.extension import ExtensionIndex as ExtensionIndex, inherit_names as inherit_names
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex, timedelta_range as timedelta_range
from pandas.core.ops import get_op_result_name as get_op_result_name
from pandas.tseries.frequencies import to_offset as to_offset
from pandas.tseries.offsets import DateOffset as DateOffset
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly
from pandas.util._exceptions import rewrite_exception as rewrite_exception
from typing import Any, Optional, Tuple, Union

class SetopCheck:
    op_name: Any = ...
    def __init__(self, op_name: Any) -> None: ...
    def __call__(self, setop: Any): ...

class IntervalIndex(IntervalMixin, ExtensionIndex):
    def __new__(cls: Any, data: Any, closed: Any=..., dtype: Any=..., copy: bool=..., name: Any=..., verify_integrity: bool=...) -> Any: ...
    @classmethod
    def from_breaks(cls: Any, breaks: Any, closed: str=..., name: Any=..., copy: bool=..., dtype: Any=...) -> Any: ...
    @classmethod
    def from_arrays(cls: Any, left: Any, right: Any, closed: str=..., name: Any=..., copy: bool=..., dtype: Any=...) -> Any: ...
    @classmethod
    def from_tuples(cls: Any, data: Any, closed: str=..., name: Any=..., copy: bool=..., dtype: Any=...) -> Any: ...
    def __contains__(self, key: Any) -> bool: ...
    def values(self): ...
    def __array_wrap__(self, result: Any, context: Optional[Any] = ...): ...
    def __reduce__(self): ...
    def astype(self, dtype: Any, copy: bool = ...): ...
    @property
    def inferred_type(self) -> str: ...
    def memory_usage(self, deep: bool=...) -> int: ...
    def is_monotonic(self) -> bool: ...
    def is_monotonic_increasing(self) -> bool: ...
    def is_monotonic_decreasing(self) -> bool: ...
    def is_unique(self): ...
    @property
    def is_overlapping(self): ...
    def get_loc(self, key: Any, method: Optional[str]=..., tolerance: Any=...) -> Union[int, slice, np.ndarray]: ...
    def get_indexer(self, target: AnyArrayLike, method: Optional[str]=..., limit: Optional[int]=..., tolerance: Optional[Any]=...) -> np.ndarray: ...
    def get_indexer_non_unique(self, target: AnyArrayLike) -> Tuple[np.ndarray, np.ndarray]: ...
    def get_indexer_for(self, target: AnyArrayLike, **kwargs: Any) -> np.ndarray: ...
    def get_value(self, series: ABCSeries, key: Any) -> Any: ...
    def where(self, cond: Any, other: Optional[Any] = ...): ...
    def delete(self, loc: Any): ...
    def insert(self, loc: Any, item: Any): ...
    def take(self, indices: Any, axis: int = ..., allow_fill: bool = ..., fill_value: Optional[Any] = ..., **kwargs: Any): ...
    def __getitem__(self, value: Any): ...
    def argsort(self, *args: Any, **kwargs: Any): ...
    def equals(self, other: Any) -> bool: ...
    def intersection(self, other: IntervalIndex, sort: bool=...) -> IntervalIndex: ...
    @property
    def is_all_dates(self) -> bool: ...
    union: Any = ...
    difference: Any = ...
    symmetric_difference: Any = ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

def interval_range(start: Optional[Any] = ..., end: Optional[Any] = ..., periods: Optional[Any] = ..., freq: Optional[Any] = ..., name: Optional[Any] = ..., closed: str = ...): ...
