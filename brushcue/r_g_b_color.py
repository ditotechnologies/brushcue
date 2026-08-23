# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 81df2bb4883341d3a9301663237093c6d2842341b7e1c8ee3fb78bd92970ba72
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class RGBColor(_GraphWrapper):
    """A color-format with a red, green and blue component"""

    def execute(self, context):

        return self._inner.execute(context)


    @staticmethod
    def from_components(r, g, b) -> RGBColor:
        """RGB Color from Components

        Given the r, g and b creates the color-format
    
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

    def passthrough(self) -> RGBColor:
        """RGB Color Passthrough

        Responds with the value provided. Doing nothing to it.
    
        Returns:
            Graph: A graph node producing a RGBColor.
        """
        value_parsed = input_parsers.parse_graph(self)
        result = _internal.r_g_b_color_passthrough_internal(value_parsed)

        return RGBColor(result)

