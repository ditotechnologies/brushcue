# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 24d256b1465fbbdd8100409719c0e185f7d89ca723fe8c70e94a575304d1a795
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class RGBAColor(Object):
    """A color with a red, green, blue, and alpha component"""

    def execute(self, context):
        return self._inner.execute(context).as_rgba_color()

    @staticmethod
    def from_components(r, g, b, a) -> RGBAColor:
        """RGBA Color from Components

        Given the r, g, b and a creates the color

        Args:
            r: Graph of Float
            g: Graph of Float
            b: Graph of Float
            a: Graph of Float

        Returns:
            Graph: A graph node producing a RGBAColor.
        """
        r_parsed = input_parsers.parse_float_graph(r)
        g_parsed = input_parsers.parse_float_graph(g)
        b_parsed = input_parsers.parse_float_graph(b)
        a_parsed = input_parsers.parse_float_graph(a)
        result = _internal.r_g_b_a_color_from_components_internal(r_parsed, g_parsed, b_parsed, a_parsed)
        return RGBAColor(result)
