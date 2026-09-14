# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: e2fd677ab4f03277a260d271deb8d9700a19e96accbfcec6dd8183d01e578279
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class Bounds2i(Object):
    """A 2D bounding box of Ints"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def from_x_y_width_height(x, y, width, height) -> Bounds2i:
        """Bounds 2D Int from X, Y, Width & Height

        Creates the bounds of a 2D array from its X, Y, Width and Height.

        Args:
            x: Graph of Int
            y: Graph of Int
            width: Graph of Int
            height: Graph of Int

        Returns:
            Graph: A graph node producing a Bounds2i.
        """
        x_parsed = input_parsers.parse_int_graph(x)
        y_parsed = input_parsers.parse_int_graph(y)
        width_parsed = input_parsers.parse_int_graph(width)
        height_parsed = input_parsers.parse_int_graph(height)
        result = _internal.bounds2i_from_x_y_width_height_internal(x_parsed, y_parsed, width_parsed, height_parsed)
        return Bounds2i(result)
