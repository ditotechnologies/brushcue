"""Private graph-wrapper support for the generated typed API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, TypeVar, overload

from . import _py as _internal

if TYPE_CHECKING:
    from .list import List
    from .object import Object
    from .stream import Stream


def unwrap_graph(value: _GraphWrapper | _internal.Graph) -> _internal.Graph:
    if isinstance(value, _GraphWrapper):
        return value._inner
    if isinstance(value, _internal.Graph):
        return value
    raise TypeError(f"Expected Graph, got {type(value)}")


class _GraphWrapper:
    """Base class for generated graph types; not part of the public API."""

    def __init__(
        self,
        inner: _internal.Graph,
        resolved_type: type[_GraphWrapper] | None = None,
    ):
        self._inner = unwrap_graph(inner)
        self._resolved_type = type(self) if resolved_type is None else resolved_type

    def persistent_id(self) -> int:
        return self._inner.persistent_id()

    def execute(self, context: _internal.Context) -> _internal.Type:
        return self._inner.execute(context)


_ObjectT = TypeVar("_ObjectT", bound="Object")
_GraphT = TypeVar("_GraphT", bound="_GraphWrapper")


@overload
def resolve_output_graph(
    inner: _internal.Graph,
    source: _GraphT,
    output_type: Literal["Any"],
) -> _GraphT: ...


@overload
def resolve_output_graph(
    inner: _internal.Graph,
    source: Stream[_ObjectT],
    output_type: Literal["Object"],
) -> _ObjectT: ...


@overload
def resolve_output_graph(
    inner: _internal.Graph,
    source: List[_ObjectT],
    output_type: Literal["Object"],
) -> _ObjectT: ...


@overload
def resolve_output_graph(
    inner: _internal.Graph,
    source: _ObjectT,
    output_type: Literal["Object"],
) -> _ObjectT: ...


@overload
def resolve_output_graph(
    inner: _internal.Graph,
    source: Stream[_ObjectT] | List[_ObjectT],
    output_type: Literal["Stream"],
) -> Stream[_ObjectT]: ...


@overload
def resolve_output_graph(
    inner: _internal.Graph,
    source: _ObjectT,
    output_type: Literal["Stream"],
) -> Stream[_ObjectT]: ...


@overload
def resolve_output_graph(
    inner: _internal.Graph,
    source: Stream[_ObjectT] | List[_ObjectT],
    output_type: Literal["List"],
) -> List[_ObjectT]: ...


@overload
def resolve_output_graph(
    inner: _internal.Graph,
    source: _ObjectT,
    output_type: Literal["List"],
) -> List[_ObjectT]: ...


def resolve_output_graph(
    inner: _internal.Graph,
    source: _GraphWrapper,
    output_type: str,
) -> _GraphWrapper:
    if not isinstance(source, _GraphWrapper):
        raise TypeError(
            "A generic output can only be resolved from a typed graph wrapper"
        )

    resolved_type = source._resolved_type
    if output_type == "Any":
        return type(source)(inner, resolved_type)
    if output_type == "Object":
        return resolved_type(inner)
    if output_type == "Stream":
        from .stream import Stream

        return Stream(inner, resolved_type)
    if output_type == "List":
        from .list import List

        return List(inner, resolved_type)
    raise ValueError(f"Unsupported generic output type: {output_type}")


def ensure_same_graph_type(*values: _GraphWrapper) -> None:
    if not values:
        return
    for value in values:
        if not isinstance(value, _GraphWrapper):
            raise TypeError("Generic branches must be typed graph wrappers")
    expected = (type(values[0]), values[0]._resolved_type)
    for value in values[1:]:
        if (type(value), value._resolved_type) != expected:
            raise TypeError(
                "Generic branches must have the same graph type; "
                f"found {type(values[0]).__name__} and {type(value).__name__}"
            )


class Project:
    """A Python façade for a Rust graph project."""

    def __init__(self, inner: _internal.Project | None = None):
        self._inner = _internal.Project() if inner is None else inner

    def add_graph(self, graph: _GraphWrapper | _internal.Graph) -> Project:
        return Project(self._inner.add_graph(unwrap_graph(graph)))

    def execute(self, context: _internal.Context, graph_id: int) -> _internal.Type:
        return self._inner.execute(context, graph_id)
