# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 1d104e64601cb9f0e5073fa8a54a3497e48fd24c5a5335412bed58bbfbd19789
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import float


class Point2f(Object):
    """A point with an x and y as floats"""

    def execute(self, context):
        return self._inner.execute(context)

    def distance(self, rhs) -> float.Float:
        """Point 2 Float Distance

        The Euclidean distance between two Point 2 Floats.

        Args:
            rhs: Graph of Point2f

        Returns:
            Graph: A graph node producing a Float.
        """
        lhs_parsed = input_parsers.parse_graph(self)
        rhs_parsed = input_parsers.parse_graph(rhs)
        result = _internal.point2f_distance_internal(lhs_parsed, rhs_parsed)
        from .float import Float
        return Float(result)

    @staticmethod
    def from_components(x, y) -> Point2f:
        """Point 2 Float from Components

        Given an x and y creates a point

        Args:
            x: Graph of Float
            y: Graph of Float

        Returns:
            Graph: A graph node producing a Point2f.
        """
        x_parsed = input_parsers.parse_float_graph(x)
        y_parsed = input_parsers.parse_float_graph(y)
        result = _internal.point2f_from_components_internal(x_parsed, y_parsed)
        return Point2f(result)
