from pandas.core.window.common import WindowGroupByMixin as WindowGroupByMixin
from pandas.core.window.rolling import _Rolling_and_Expanding
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from typing import Any, Optional

class Expanding(_Rolling_and_Expanding):
    def __init__(self, obj: Any, min_periods: int = ..., center: bool = ..., axis: int = ..., **kwargs: Any) -> None: ...
    def aggregate(self, func: Any, *args: Any, **kwargs: Any): ...
    agg: Any = ...
    def count(self, **kwargs: Any): ...
    def apply(self, func: Any, raw: bool = ..., args: Any = ..., kwargs: Any = ...): ...
    def sum(self, *args: Any, **kwargs: Any): ...
    def max(self, *args: Any, **kwargs: Any): ...
    def min(self, *args: Any, **kwargs: Any): ...
    def mean(self, *args: Any, **kwargs: Any): ...
    def median(self, **kwargs: Any): ...
    def std(self, ddof: int = ..., *args: Any, **kwargs: Any): ...
    def var(self, ddof: int = ..., *args: Any, **kwargs: Any): ...
    def skew(self, **kwargs: Any): ...
    def kurt(self, **kwargs: Any): ...
    def quantile(self, quantile: Any, interpolation: str = ..., **kwargs: Any): ...
    def cov(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., ddof: int = ..., **kwargs: Any): ...
    def corr(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., **kwargs: Any): ...

class ExpandingGroupby(WindowGroupByMixin, Expanding): ...
