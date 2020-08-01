import numpy as np
from pandas._libs import NaT as NaT, NaTType as NaTType, Timestamp as Timestamp, algos as algos, iNaT as iNaT, lib as lib
from pandas._libs.tslibs.c_timestamp import integer_op_not_supported as integer_op_not_supported
from pandas._libs.tslibs.period import DIFFERENT_FREQ as DIFFERENT_FREQ, IncompatibleFrequency as IncompatibleFrequency, Period as Period
from pandas._libs.tslibs.timedeltas import Timedelta as Timedelta, delta_to_nanoseconds as delta_to_nanoseconds
from pandas._libs.tslibs.timestamps import RoundTo as RoundTo, round_nsint64 as round_nsint64
from pandas._typing import DatetimeLikeScalar as DatetimeLikeScalar
from pandas.compat import set_function_name as set_function_name
from pandas.core import missing as missing, nanops as nanops, ops as ops
from pandas.core.algorithms import checked_add_with_arr as checked_add_with_arr, take as take, unique1d as unique1d, value_counts as value_counts
from pandas.core.arrays.base import ExtensionArray as ExtensionArray, ExtensionOpsMixin as ExtensionOpsMixin
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_datetime64_any_dtype as is_datetime64_any_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_datetime_or_timedelta_dtype as is_datetime_or_timedelta_dtype, is_dtype_equal as is_dtype_equal, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_object_dtype as is_object_dtype, is_period_dtype as is_period_dtype, is_string_dtype as is_string_dtype, is_timedelta64_dtype as is_timedelta64_dtype, is_unsigned_integer_dtype as is_unsigned_integer_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.dtypes.inference import is_array_like as is_array_like
from pandas.core.dtypes.missing import is_valid_nat_for_dtype as is_valid_nat_for_dtype, isna as isna
from pandas.core.indexers import check_array_indexer as check_array_indexer
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.core.ops.invalid import invalid_comparison as invalid_comparison, make_invalid_op as make_invalid_op
from pandas.errors import AbstractMethodError as AbstractMethodError, NullFrequencyError as NullFrequencyError, PerformanceWarning as PerformanceWarning
from pandas.tseries import frequencies as frequencies
from pandas.tseries.offsets import DateOffset as DateOffset, Tick as Tick
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from pandas.util._validators import validate_fillna_kwargs as validate_fillna_kwargs
from typing import Any, Optional, Sequence, Union

class AttributesMixin: ...

class DatelikeOps:
    def strftime(self, date_format: Any): ...

class TimelikeOps:
    def round(self, freq: Any, ambiguous: str = ..., nonexistent: str = ...): ...
    def floor(self, freq: Any, ambiguous: str = ..., nonexistent: str = ...): ...
    def ceil(self, freq: Any, ambiguous: str = ..., nonexistent: str = ...): ...

class DatetimeLikeArrayMixin(ExtensionOpsMixin, AttributesMixin, ExtensionArray):
    @property
    def ndim(self) -> int: ...
    @property
    def shape(self): ...
    def reshape(self, *args: Any, **kwargs: Any): ...
    def ravel(self, *args: Any, **kwargs: Any): ...
    def __iter__(self) -> Any: ...
    @property
    def asi8(self) -> np.ndarray: ...
    @property
    def nbytes(self): ...
    def __array__(self, dtype: Any=...) -> np.ndarray: ...
    @property
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Union[int, Sequence[int], Sequence[bool], slice], value: Union[NaTType, Any, Sequence[Any]]) -> None: ...
    def astype(self, dtype: Any, copy: bool = ...): ...
    def view(self, dtype: Optional[Any] = ...): ...
    def unique(self): ...
    def take(self, indices: Any, allow_fill: bool = ..., fill_value: Optional[Any] = ...): ...
    def copy(self): ...
    def shift(self, periods: int = ..., fill_value: Optional[Any] = ..., axis: int = ...): ...
    def searchsorted(self, value: Any, side: str = ..., sorter: Optional[Any] = ...): ...
    def repeat(self, repeats: Any, *args: Any, **kwargs: Any): ...
    def value_counts(self, dropna: bool = ...): ...
    def map(self, mapper: Any): ...
    def isna(self): ...
    def fillna(self, value: Optional[Any] = ..., method: Optional[Any] = ..., limit: Optional[Any] = ...): ...
    @property
    def freq(self): ...
    @freq.setter
    def freq(self, value: Any) -> None: ...
    @property
    def freqstr(self): ...
    @property
    def inferred_freq(self): ...
    @property
    def resolution(self): ...
    __pow__: Any = ...
    __rpow__: Any = ...
    __mul__: Any = ...
    __rmul__: Any = ...
    __truediv__: Any = ...
    __rtruediv__: Any = ...
    __floordiv__: Any = ...
    __rfloordiv__: Any = ...
    __mod__: Any = ...
    __rmod__: Any = ...
    __divmod__: Any = ...
    __rdivmod__: Any = ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __sub__(self, other: Any): ...
    def __rsub__(self, other: Any): ...
    def __iadd__(self, other: Any): ...
    def __isub__(self, other: Any): ...
    def min(self, axis: Optional[Any] = ..., skipna: bool = ..., *args: Any, **kwargs: Any): ...
    def max(self, axis: Optional[Any] = ..., skipna: bool = ..., *args: Any, **kwargs: Any): ...
    def mean(self, skipna: bool = ...): ...

def validate_periods(periods: Any): ...
def validate_endpoints(closed: Any): ...
def validate_inferred_freq(freq: Any, inferred_freq: Any, freq_infer: Any): ...
def maybe_infer_freq(freq: Any): ...
