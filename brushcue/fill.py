# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 8e3b0671cfc07d701632dc3c86751be21ce689b58bfebe494c17b016df31bdb3
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class Fill(Object):
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

        Creates a fill with a solid color.

        Args:
            color: Graph of ProfiledColor

        Returns:
            Graph: A graph node producing a Fill.
        """
        color_parsed = input_parsers.parse_graph(color)
        result = _internal.fill_solid_internal(color_parsed)
        return Fill(result)
