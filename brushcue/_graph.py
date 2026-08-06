"""Private graph-wrapper support for the generated typed API."""

from __future__ import annotations

from . import _py as _internal


def unwrap_graph(value: _GraphWrapper | _internal.Graph) -> _internal.Graph:
    if isinstance(value, _GraphWrapper):
        return value._inner
    if isinstance(value, _internal.Graph):
        return value
    raise TypeError(f"Expected Graph, got {type(value)}")


class _GraphWrapper:
    """Base class for generated graph types; not part of the public API."""

    def __init__(self, inner: _internal.Graph):
        self._inner = unwrap_graph(inner)

    def persistent_id(self) -> int:
        return self._inner.persistent_id()

    def execute(self, context: _internal.Context) -> _internal.Type:
        return self._inner.execute(context)


class Project:
    """A Python façade for a Rust graph project."""

    def __init__(self, inner: _internal.Project | None = None):
        self._inner = _internal.Project() if inner is None else inner

    def add_graph(self, graph: _GraphWrapper | _internal.Graph) -> Project:
        return Project(self._inner.add_graph(unwrap_graph(graph)))

    def serialize(self, context: _internal.Context) -> bytes:
        return self._inner.serialize(context)

    def execute(self, context: _internal.Context, graph_id: int) -> _internal.Type:
        return self._inner.execute(context, graph_id)

    @staticmethod
    def deserialize(context: _internal.Context, data: bytes) -> Project:
        return Project(_internal.Project.deserialize(context, data))
