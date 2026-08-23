# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 3d385a7cafbb2b7bd88e430534ae3f2a586d5f53c454fe15fb349eda50c5fc9c
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class RGBAColor(_GraphWrapper):
    """A color-format with a red, green, blue, and alpha component"""

    def execute(self, context):

        return self._inner.execute(context).as_rgba_color()


    @staticmethod
    def from_components(r, g, b, a) -> RGBAColor:
        """RGBA Color from Components

        Given the r, g, b and a creates the color-format
    
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

    def passthrough(self) -> RGBAColor:
        """RGBA Color Passthrough

        Responds with the value provided. Doing nothing to it.
    
        Returns:
            Graph: A graph node producing a RGBAColor.
        """
        value_parsed = input_parsers.parse_graph(self)
        result = _internal.r_g_b_a_color_passthrough_internal(value_parsed)

        return RGBAColor(result)

