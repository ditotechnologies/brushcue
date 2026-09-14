# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 7c30a70b82b7adf2f9698d5f4f2a813963cf0b4d4f0d620f8321c46df85a0e37
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class Brush(Object):
    """A brush to stroke on 2D objects"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def solid(color, radius) -> Brush:
        """Brush Solid

        Creates a brush with a color-format and radius. Will stroke with the solid color-format.

        Args:
            color: Graph of ProfiledColor
            radius: Graph of Float

        Returns:
            Graph: A graph node producing a Brush.
        """
        color_parsed = input_parsers.parse_graph(color)
        radius_parsed = input_parsers.parse_float_graph(radius)
        result = _internal.brush_solid_internal(color_parsed, radius_parsed)
        return Brush(result)
