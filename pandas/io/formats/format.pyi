import numpy as np
from datetime import tzinfo as tzinfo
from pandas import Categorical as Categorical, DataFrame as DataFrame, Series as Series
from pandas._config.config import get_option as get_option, set_option as set_option
#from pandas._libs import lib as lib
#from pandas._libs.missing import NA as NA
#from pandas._libs.tslib import format_array_from_datetime as format_array_from_datetime
from pandas._libs.tslibs import NaT as NaT, Timedelta as Timedelta, Timestamp as Timestamp, iNaT as iNaT
#from pandas._libs.tslibs.nattype import NaTType as NaTType
from pandas._typing import FilePathOrBuffer as FilePathOrBuffer
from pandas.core.arrays.datetimes import DatetimeArray as DatetimeArray
from pandas.core.arrays.timedeltas import TimedeltaArray as TimedeltaArray
from pandas.core.base import PandasObject as PandasObject
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_complex_dtype as is_complex_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_extension_array_dtype as is_extension_array_dtype, is_float as is_float, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_scalar as is_scalar, is_timedelta64_dtype as is_timedelta64_dtype
from pandas.core.dtypes.generic import ABCIndexClass as ABCIndexClass, ABCMultiIndex as ABCMultiIndex, ABCSeries as ABCSeries, ABCSparseArray as ABCSparseArray
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.indexes.api import Index as Index
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.common import stringify_path as stringify_path
from pandas.io.formats.printing import adjoin as adjoin, justify as justify, pprint_thing as pprint_thing
from typing import Any, Callable, Dict, IO, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

formatters_type = Union[List[Callable], Tuple[Callable, ...], Mapping[Union[str, int], Callable]]
float_format_type: Any
common_docstring: str
return_docstring: str

class CategoricalFormatter:
    categorical: Any = ...
    buf: Any = ...
    na_rep: Any = ...
    length: Any = ...
    footer: Any = ...
    def __init__(self, categorical: Categorical, buf: Optional[IO[str]]=..., length: bool=..., na_rep: str=..., footer: bool=...) -> None: ...
    def to_string(self) -> str: ...

class SeriesFormatter:
    series: Any = ...
    buf: Any = ...
    name: Any = ...
    na_rep: Any = ...
    header: Any = ...
    length: Any = ...
    index: Any = ...
    max_rows: Any = ...
    min_rows: Any = ...
    float_format: Any = ...
    dtype: Any = ...
    adj: Any = ...
    def __init__(self, series: Series, buf: Optional[IO[str]]=..., length: Union[bool, str]=..., header: bool=..., index: bool=..., na_rep: str=..., name: bool=..., float_format: Optional[str]=..., dtype: bool=..., max_rows: Optional[int]=..., min_rows: Optional[int]=...) -> None: ...
    def to_string(self) -> str: ...

class TextAdjustment:
    encoding: Any = ...
    def __init__(self) -> None: ...
    def len(self, text: str) -> int: ...
    def justify(self, texts: Any, max_len: int, mode: str=...) -> List[str]: ...
    def adjoin(self, space: int, *lists: Any, **kwargs: Any) -> str: ...

class EastAsianTextAdjustment(TextAdjustment):
    ambiguous_width: int = ...
    def __init__(self) -> None: ...
    def len(self, text: str) -> int: ...
    def justify(self, texts: Iterable[str], max_len: int, mode: str=...) -> List[str]: ...

class TableFormatter:
    show_dimensions: Union[bool, str]
    is_truncated: bool
    formatters: formatters_type
    columns: Index
    @property
    def should_show_dimensions(self) -> bool: ...
    def get_buffer(self, buf: Optional[FilePathOrBuffer[str]], encoding: Optional[str]=...) -> Any: ...
    def write_result(self, buf: IO[str]) -> None: ...
    def get_result(self, buf: Optional[FilePathOrBuffer[str]]=..., encoding: Optional[str]=...) -> Optional[str]: ...

class DataFrameFormatter(TableFormatter):
    __doc__: Any = ...
    frame: Any = ...
    show_index_names: Any = ...
    sparsify: Any = ...
    float_format: Any = ...
    formatters: Any = ...
    na_rep: Any = ...
    decimal: Any = ...
    col_space: Any = ...
    header: Any = ...
    index: Any = ...
    line_width: Any = ...
    max_rows: Any = ...
    min_rows: Any = ...
    max_cols: Any = ...
    max_rows_displayed: Any = ...
    show_dimensions: Any = ...
    table_id: Any = ...
    render_links: Any = ...
    justify: Any = ...
    bold_rows: Any = ...
    escape: Any = ...
    columns: Any = ...
    adj: Any = ...
    def __init__(self, frame: DataFrame, columns: Optional[Sequence[str]]=..., col_space: Optional[Union[str, int]]=..., header: Union[bool, Sequence[str]]=..., index: bool=..., na_rep: str=..., formatters: Optional[formatters_type]=..., justify: Optional[str]=..., float_format: Optional[float_format_type]=..., sparsify: Optional[bool]=..., index_names: bool=..., line_width: Optional[int]=..., max_rows: Optional[int]=..., min_rows: Optional[int]=..., max_cols: Optional[int]=..., show_dimensions: Union[bool, str]=..., decimal: str=..., table_id: Optional[str]=..., render_links: bool=..., bold_rows: bool=..., escape: bool=...) -> None: ...
    max_cols_adj: Any = ...
    def write_result(self, buf: IO[str]) -> None: ...
    def to_string(self, buf: Optional[FilePathOrBuffer[str]]=..., encoding: Optional[str]=...) -> Optional[str]: ...
    def to_latex(self, buf: Optional[FilePathOrBuffer[str]]=..., column_format: Optional[str]=..., longtable: bool=..., encoding: Optional[str]=..., multicolumn: bool=..., multicolumn_format: Optional[str]=..., multirow: bool=..., caption: Optional[str]=..., label: Optional[str]=...) -> Optional[str]: ...
    def to_html(self, buf: Optional[FilePathOrBuffer[str]]=..., encoding: Optional[str]=..., classes: Optional[Union[str, List, Tuple]]=..., notebook: bool=..., border: Optional[int]=...) -> Optional[str]: ...
    @property
    def has_index_names(self) -> bool: ...
    @property
    def has_column_names(self) -> bool: ...
    @property
    def show_row_idx_names(self) -> bool: ...
    @property
    def show_col_idx_names(self) -> bool: ...

def format_array(values: Any, formatter: Optional[Callable], float_format: Optional[float_format_type]=..., na_rep: str=..., digits: Optional[int]=..., space: Optional[Union[str, int]]=..., justify: str=..., decimal: str=..., leading_space: Optional[bool]=...) -> List[str]: ...

class GenericArrayFormatter:
    values: Any = ...
    digits: Any = ...
    na_rep: Any = ...
    space: Any = ...
    formatter: Any = ...
    float_format: Any = ...
    justify: Any = ...
    decimal: Any = ...
    quoting: Any = ...
    fixed_width: Any = ...
    leading_space: Any = ...
    def __init__(self, values: Any, digits: int=..., formatter: Optional[Callable]=..., na_rep: str=..., space: Union[str, int]=..., float_format: Optional[float_format_type]=..., justify: str=..., decimal: str=..., quoting: Optional[int]=..., fixed_width: bool=..., leading_space: Optional[bool]=...) -> None: ...
    def get_result(self) -> List[str]: ...

class FloatArrayFormatter(GenericArrayFormatter):
    fixed_width: bool = ...
    formatter: Any = ...
    float_format: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_result_as_array(self) -> np.ndarray: ...

class IntArrayFormatter(GenericArrayFormatter): ...

class Datetime64Formatter(GenericArrayFormatter):
    nat_rep: Any = ...
    date_format: Any = ...
    def __init__(self, values: Union[np.ndarray, Series, DatetimeIndex, DatetimeArray], nat_rep: str=..., date_format: None=..., **kwargs: Any) -> None: ...

class ExtensionArrayFormatter(GenericArrayFormatter): ...

def format_percentiles(percentiles: Union[np.ndarray, List[Union[int, float]], List[float], List[Union[str, float]]]) -> List[str]: ...

class Datetime64TZFormatter(Datetime64Formatter): ...

class Timedelta64Formatter(GenericArrayFormatter):
    nat_rep: Any = ...
    box: Any = ...
    def __init__(self, values: Union[np.ndarray, TimedeltaIndex], nat_rep: str=..., box: bool=..., **kwargs: Any) -> None: ...

class EngFormatter:
    ENG_PREFIXES: Any = ...
    accuracy: Any = ...
    use_eng_prefix: Any = ...
    def __init__(self, accuracy: Optional[int]=..., use_eng_prefix: bool=...) -> None: ...
    def __call__(self, num: Union[int, float]) -> str: ...

def set_eng_float_format(accuracy: int=..., use_eng_prefix: bool=...) -> None: ...
def get_level_lengths(levels: Any, sentinel: Union[bool, object, str]=...) -> List[Dict[int, int]]: ...
def buffer_put_lines(buf: IO[str], lines: List[str]) -> None: ...
