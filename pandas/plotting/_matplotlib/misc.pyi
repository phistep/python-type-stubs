from pandas.core.dtypes.missing import notna as notna
from pandas.io.formats.printing import pprint_thing as pprint_thing
from typing import Any, Optional

def scatter_matrix(frame: Any, alpha: float = ..., figsize: Optional[Any] = ..., ax: Optional[Any] = ..., grid: bool = ..., diagonal: str = ..., marker: str = ..., density_kwds: Optional[Any] = ..., hist_kwds: Optional[Any] = ..., range_padding: float = ..., **kwds: Any): ...
def radviz(frame: Any, class_column: Any, ax: Optional[Any] = ..., color: Optional[Any] = ..., colormap: Optional[Any] = ..., **kwds: Any): ...
def andrews_curves(frame: Any, class_column: Any, ax: Optional[Any] = ..., samples: int = ..., color: Optional[Any] = ..., colormap: Optional[Any] = ..., **kwds: Any): ...
def bootstrap_plot(series: Any, fig: Optional[Any] = ..., size: int = ..., samples: int = ..., **kwds: Any): ...
def parallel_coordinates(frame: Any, class_column: Any, cols: Optional[Any] = ..., ax: Optional[Any] = ..., color: Optional[Any] = ..., use_columns: bool = ..., xticks: Optional[Any] = ..., colormap: Optional[Any] = ..., axvlines: bool = ..., axvlines_kwds: Optional[Any] = ..., sort_labels: bool = ..., **kwds: Any): ...
def lag_plot(series: Any, lag: int = ..., ax: Optional[Any] = ..., **kwds: Any): ...
def autocorrelation_plot(series: Any, ax: Optional[Any] = ..., **kwds: Any): ...
