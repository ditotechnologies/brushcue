# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: faf5cf9085148c6b1d1772181252217140462ef28f6e9c3bdf1d3085cc1e5937
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class Fill(_GraphWrapper):
    """The fill for when drawing in a 2d object."""

    def execute(self, context):

        return self._inner.execute(context)


    @staticmethod
    def custom(function_body, helpers, inputs) -> Fill:
        """Fill Custom

        Creates a fill with a custom shader.
    
        Args:
            function_body: Graph of String
            helpers: Graph of String
            inputs: Graph of Dictionary
            
    
        Returns:
            Graph: A graph node producing a Fill.
        """
        function_body_parsed = input_parsers.parse_string_graph(function_body)
        helpers_parsed = input_parsers.parse_string_graph(helpers)
        inputs_parsed = input_parsers.parse_graph(inputs)
        result = _internal.fill_custom_internal(function_body_parsed, helpers_parsed, inputs_parsed)

        return Fill(result)

    @staticmethod
    def solid(color) -> Fill:
        """Fill Solid

        Creates a fill with a solid color-format.
    
        Args:
            color: Graph of ProfiledColor
            
    
        Returns:
            Graph: A graph node producing a Fill.
        """
        color_parsed = input_parsers.parse_graph(color)
        result = _internal.fill_solid_internal(color_parsed)

        return Fill(result)

