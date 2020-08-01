from pandas._libs import NaT as NaT, Timestamp as Timestamp, lib as lib, tslib as tslib, writers as writers
from pandas._libs.index import convert_scalar as convert_scalar
from pandas._libs.tslibs import Timedelta as Timedelta, conversion as conversion
from pandas._libs.tslibs.timezones import tz_compare as tz_compare
from pandas.core.arrays import Categorical as Categorical, DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, PandasArray as PandasArray, PandasDtype as PandasDtype, TimedeltaArray as TimedeltaArray
from pandas.core.base import PandasObject as PandasObject
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.cast import astype_nansafe as astype_nansafe, find_common_type as find_common_type, infer_dtype_from as infer_dtype_from, infer_dtype_from_scalar as infer_dtype_from_scalar, maybe_downcast_numeric as maybe_downcast_numeric, maybe_downcast_to_dtype as maybe_downcast_to_dtype, maybe_infer_dtype_type as maybe_infer_dtype_type, maybe_promote as maybe_promote, maybe_upcast as maybe_upcast, soft_convert_objects as soft_convert_objects
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_bool_dtype as is_bool_dtype, is_categorical as is_categorical, is_categorical_dtype as is_categorical_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_interval_dtype as is_interval_dtype, is_list_like as is_list_like, is_object_dtype as is_object_dtype, is_period_dtype as is_period_dtype, is_re as is_re, is_re_compilable as is_re_compilable, is_sparse as is_sparse, is_timedelta64_dtype as is_timedelta64_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.concat import concat_categorical as concat_categorical, concat_datetime as concat_datetime
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCExtensionArray as ABCExtensionArray, ABCPandasArray as ABCPandasArray, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import array_equivalent as array_equivalent, is_valid_nat_for_dtype as is_valid_nat_for_dtype, isna as isna
from pandas.core.indexers import check_setitem_lengths as check_setitem_lengths, is_empty_indexer as is_empty_indexer, is_scalar_indexer as is_scalar_indexer
from pandas.core.nanops import nanpercentile as nanpercentile
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Any, List, Optional

class Block(PandasObject):
    is_numeric: bool = ...
    is_float: bool = ...
    is_integer: bool = ...
    is_complex: bool = ...
    is_datetime: bool = ...
    is_datetimetz: bool = ...
    is_timedelta: bool = ...
    is_bool: bool = ...
    is_object: bool = ...
    is_categorical: bool = ...
    is_extension: bool = ...
    ndim: Any = ...
    values: Any = ...
    def __init__(self, values: Any, placement: Any, ndim: Optional[Any] = ...) -> None: ...
    @property
    def is_view(self): ...
    @property
    def is_datelike(self): ...
    def is_categorical_astype(self, dtype: Any): ...
    def external_values(self, dtype: Optional[Any] = ...): ...
    def internal_values(self, dtype: Optional[Any] = ...): ...
    def array_values(self) -> ExtensionArray: ...
    def get_values(self, dtype: Optional[Any] = ...): ...
    def get_block_values(self, dtype: Optional[Any] = ...): ...
    def to_dense(self): ...
    @property
    def fill_value(self): ...
    @property
    def mgr_locs(self): ...
    @mgr_locs.setter
    def mgr_locs(self, new_mgr_locs: Any) -> None: ...
    @property
    def array_dtype(self): ...
    def make_block(self, values: Any, placement: Any=...) -> Block: ...
    def make_block_same_class(self, values: Any, placement: Optional[Any] = ..., ndim: Optional[Any] = ...): ...
    def __len__(self) -> int: ...
    def getitem_block(self, slicer: Any, new_mgr_locs: Optional[Any] = ...): ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...
    @property
    def ftype(self): ...
    def merge(self, other: Any): ...
    def concat_same_type(self, to_concat: Any, placement: Optional[Any] = ...): ...
    def iget(self, i: Any): ...
    def set(self, locs: Any, values: Any) -> None: ...
    def delete(self, loc: Any) -> None: ...
    def apply(self, func: Any, **kwargs: Any): ...
    def fillna(self, value: Any, limit: Optional[Any] = ..., inplace: bool = ..., downcast: Optional[Any] = ...): ...
    def split_and_operate(self, mask: Any, f: Any, inplace: bool) -> Any: ...
    def downcast(self, dtypes: Optional[Any] = ...): ...
    def astype(self, dtype: Any, copy: bool=..., errors: str=...) -> Any: ...
    def convert(self, copy: bool=..., datetime: bool=..., numeric: bool=..., timedelta: bool=..., coerce: bool=...) -> Any: ...
    def to_native_types(self, slicer: Optional[Any] = ..., na_rep: str = ..., quoting: Optional[Any] = ..., **kwargs: Any): ...
    def copy(self, deep: bool = ...): ...
    def replace(self, to_replace: Any, value: Any, inplace: bool = ..., filter: Optional[Any] = ..., regex: bool = ..., convert: bool = ...): ...
    def setitem(self, indexer: Any, value: Any): ...
    def putmask(self, mask: Any, new: Any, align: bool = ..., inplace: bool = ..., axis: int = ..., transpose: bool = ...): ...
    def coerce_to_target_dtype(self, other: Any): ...
    def interpolate(self, method: str = ..., axis: int = ..., index: Optional[Any] = ..., values: Optional[Any] = ..., inplace: bool = ..., limit: Optional[Any] = ..., limit_direction: str = ..., limit_area: Optional[Any] = ..., fill_value: Optional[Any] = ..., coerce: bool = ..., downcast: Optional[Any] = ..., **kwargs: Any): ...
    def take_nd(self, indexer: Any, axis: Any, new_mgr_locs: Optional[Any] = ..., fill_tuple: Optional[Any] = ...): ...
    def diff(self, n: int, axis: int=...) -> List[Block]: ...
    def shift(self, periods: Any, axis: int = ..., fill_value: Optional[Any] = ...): ...
    def where(self, other: Any, cond: Any, align: Any=..., errors: Any=..., try_cast: bool=..., axis: int=...) -> List[Block]: ...
    def equals(self, other: Any) -> bool: ...
    def quantile(self, qs: Any, interpolation: str = ..., axis: int = ...): ...

class NonConsolidatableMixIn:
    def __init__(self, values: Any, placement: Any, ndim: Optional[Any] = ...) -> None: ...
    @property
    def shape(self): ...
    def iget(self, col: Any): ...
    def should_store(self, value: Any): ...
    values: Any = ...
    def set(self, locs: Any, values: Any, check: bool = ...) -> None: ...
    def putmask(self, mask: Any, new: Any, align: bool = ..., inplace: bool = ..., axis: int = ..., transpose: bool = ...): ...

class ExtensionBlock(NonConsolidatableMixIn, Block):
    is_extension: bool = ...
    def __init__(self, values: Any, placement: Any, ndim: Optional[Any] = ...) -> None: ...
    @property
    def fill_value(self): ...
    @property
    def is_view(self): ...
    @property
    def is_numeric(self): ...
    def setitem(self, indexer: Any, value: Any): ...
    def get_values(self, dtype: Optional[Any] = ...): ...
    def array_values(self) -> ExtensionArray: ...
    def to_dense(self): ...
    def to_native_types(self, slicer: Optional[Any] = ..., na_rep: str = ..., quoting: Optional[Any] = ..., **kwargs: Any): ...
    def take_nd(self, indexer: Any, axis: int = ..., new_mgr_locs: Optional[Any] = ..., fill_tuple: Optional[Any] = ...): ...
    def concat_same_type(self, to_concat: Any, placement: Optional[Any] = ...): ...
    def fillna(self, value: Any, limit: Optional[Any] = ..., inplace: bool = ..., downcast: Optional[Any] = ...): ...
    def interpolate(self, method: str = ..., axis: int = ..., inplace: bool = ..., limit: Optional[Any] = ..., fill_value: Optional[Any] = ..., **kwargs: Any): ...
    def diff(self, n: int, axis: int=...) -> List[Block]: ...
    def shift(self, periods: int, axis: int=..., fill_value: Any=...) -> List[ExtensionBlock]: ...
    def where(self, other: Any, cond: Any, align: Any=..., errors: Any=..., try_cast: bool=..., axis: int=...) -> List[Block]: ...

class ObjectValuesExtensionBlock(ExtensionBlock):
    def external_values(self, dtype: Optional[Any] = ...): ...

class NumericBlock(Block):
    is_numeric: bool = ...

class FloatOrComplexBlock(NumericBlock):
    def equals(self, other: Any) -> bool: ...

class FloatBlock(FloatOrComplexBlock):
    is_float: bool = ...
    def to_native_types(self, slicer: Optional[Any] = ..., na_rep: str = ..., float_format: Optional[Any] = ..., decimal: str = ..., quoting: Optional[Any] = ..., **kwargs: Any): ...
    def should_store(self, value: Any): ...

class ComplexBlock(FloatOrComplexBlock):
    is_complex: bool = ...
    def should_store(self, value: Any): ...

class IntBlock(NumericBlock):
    is_integer: bool = ...
    def should_store(self, value: Any): ...

class DatetimeLikeBlockMixin:
    @property
    def fill_value(self): ...
    def get_values(self, dtype: Optional[Any] = ...): ...
    def iget(self, key: Any): ...
    def shift(self, periods: Any, axis: int = ..., fill_value: Optional[Any] = ...): ...

class DatetimeBlock(DatetimeLikeBlockMixin, Block):
    is_datetime: bool = ...
    def __init__(self, values: Any, placement: Any, ndim: Optional[Any] = ...) -> None: ...
    def astype(self, dtype: Any, copy: bool=..., errors: str=...) -> Any: ...
    def to_native_types(self, slicer: Optional[Any] = ..., na_rep: Optional[Any] = ..., date_format: Optional[Any] = ..., quoting: Optional[Any] = ..., **kwargs: Any): ...
    def should_store(self, value: Any): ...
    def set(self, locs: Any, values: Any) -> None: ...
    def external_values(self): ...
    def array_values(self) -> ExtensionArray: ...

class DatetimeTZBlock(ExtensionBlock, DatetimeBlock):
    is_datetimetz: bool = ...
    is_extension: bool = ...
    to_native_types: Any = ...
    fill_value: Any = ...
    @property
    def is_view(self): ...
    def get_values(self, dtype: Optional[Any] = ...): ...
    def to_dense(self): ...
    def diff(self, n: int, axis: int=...) -> List[Block]: ...
    def concat_same_type(self, to_concat: Any, placement: Optional[Any] = ...): ...
    def fillna(self, value: Any, limit: Optional[Any] = ..., inplace: bool = ..., downcast: Optional[Any] = ...): ...
    def setitem(self, indexer: Any, value: Any): ...
    def equals(self, other: Any) -> bool: ...
    def quantile(self, qs: Any, interpolation: str = ..., axis: int = ...): ...

class TimeDeltaBlock(DatetimeLikeBlockMixin, IntBlock):
    is_timedelta: bool = ...
    is_numeric: bool = ...
    fill_value: Any = ...
    def __init__(self, values: Any, placement: Any, ndim: Optional[Any] = ...) -> None: ...
    def fillna(self, value: Any, **kwargs: Any): ...
    def should_store(self, value: Any): ...
    def to_native_types(self, slicer: Optional[Any] = ..., na_rep: Optional[Any] = ..., quoting: Optional[Any] = ..., **kwargs: Any): ...
    def external_values(self, dtype: Optional[Any] = ...): ...
    def array_values(self) -> ExtensionArray: ...

class BoolBlock(NumericBlock):
    is_bool: bool = ...
    def should_store(self, value: Any): ...
    def replace(self, to_replace: Any, value: Any, inplace: bool = ..., filter: Optional[Any] = ..., regex: bool = ..., convert: bool = ...): ...

class ObjectBlock(Block):
    is_object: bool = ...
    def __init__(self, values: Any, placement: Optional[Any] = ..., ndim: int = ...) -> None: ...
    @property
    def is_bool(self): ...
    def convert(self, copy: bool=..., datetime: bool=..., numeric: bool=..., timedelta: bool=..., coerce: bool=...) -> Any: ...
    def should_store(self, value: Any): ...
    def replace(self, to_replace: Any, value: Any, inplace: bool = ..., filter: Optional[Any] = ..., regex: bool = ..., convert: bool = ...): ...

class CategoricalBlock(ExtensionBlock):
    is_categorical: bool = ...
    def __init__(self, values: Any, placement: Any, ndim: Optional[Any] = ...) -> None: ...
    @property
    def array_dtype(self): ...
    def to_dense(self): ...
    def to_native_types(self, slicer: Optional[Any] = ..., na_rep: str = ..., quoting: Optional[Any] = ..., **kwargs: Any): ...
    def concat_same_type(self, to_concat: Any, placement: Optional[Any] = ...): ...
    def replace(self, to_replace: Any, value: Any, inplace: bool=..., filter: Any=..., regex: bool=..., convert: bool=...) -> Any: ...

def get_block_type(values: Any, dtype: Optional[Any] = ...): ...
def make_block(values: Any, placement: Any, klass: Optional[Any] = ..., ndim: Optional[Any] = ..., dtype: Optional[Any] = ...): ...
