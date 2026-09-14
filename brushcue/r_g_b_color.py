# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 5a8b038c368de4f29fd53a354b651faf516871ef696b2b507b1a4fb413407a78
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class RGBColor(Object):
    """A color with a red, green and blue component"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def from_components(r, g, b) -> RGBColor:
        """RGB Color from Components

        Given the r, g and b creates the color

        Args:
            r: Graph of Float
            g: Graph of Float
            b: Graph of Float

        Returns:
            Graph: A graph node producing a RGBColor.
        """
        r_parsed = input_parsers.parse_float_graph(r)
        g_parsed = input_parsers.parse_float_graph(g)
        b_parsed = input_parsers.parse_float_graph(b)
        result = _internal.r_g_b_color_from_components_internal(r_parsed, g_parsed, b_parsed)
        return RGBColor(result)
