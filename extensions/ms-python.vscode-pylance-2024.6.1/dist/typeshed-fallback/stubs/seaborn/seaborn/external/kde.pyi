from collections.abc import Callable
from typing import Any, Literal, Protocol
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import ArrayLike, NDArray

__all__ = ["gaussian_kde"]

# define a "Gaussian KDE" protocol so that we can also pass `scipy.stats.gaussian_kde` to
# functions that expect it without adding a dependency on scipy
class _GaussianKDELike(Protocol):
    dataset: NDArray[np.float64]
    def __init__(self, dataset: ArrayLike, bw_method: Any | None = ..., weights: ArrayLike | None = ...) -> None: ...
    def evaluate(self, points: ArrayLike) -> NDArray[Any]: ...
    def __call__(self, points: ArrayLike) -> NDArray[Any]: ...
    def scotts_factor(self) -> float: ...
    def silverman_factor(self) -> float: ...
    def covariance_factor(self) -> float: ...
    def pdf(self, x: ArrayLike) -> NDArray[Any]: ...
    def set_bandwidth(self, bw_method: Any | None = ...) -> None: ...
    @property
    def weights(self) -> NDArray[Any]: ...
    @property
    def neff(self) -> NDArray[Any]: ...

_Scalar: TypeAlias = float | np.number[Any]
_BwMethodType: TypeAlias = Literal["scott", "silverman"] | Callable[[_GaussianKDELike], _Scalar] | _Scalar | None

class gaussian_kde:
    dataset: NDArray[np.float64]
    def __init__(self, dataset: ArrayLike, bw_method: _BwMethodType = None, weights: ArrayLike | None = None) -> None: ...
    def evaluate(self, points: ArrayLike) -> NDArray[np.float64]: ...
    __call__ = evaluate
    def scotts_factor(self) -> float: ...
    def silverman_factor(self) -> float: ...
    covariance_factor = scotts_factor
    def set_bandwidth(self, bw_method: _BwMethodType = None) -> None: ...
    def pdf(self, x: ArrayLike) -> NDArray[np.float64]: ...
    @property
    def weights(self) -> NDArray[np.float64]: ...
    @property
    def neff(self) -> NDArray[np.float64]: ...
