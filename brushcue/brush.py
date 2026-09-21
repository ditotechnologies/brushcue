# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: eee61e5042d9a6d1d7f2d36f361cacc078da78022d5535c1c47f7574df561089
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class Brush(Object):
    """A brush to stroke on 2D objects"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def custom(function_body, helpers, inputs, radius) -> Brush:
        """Brush Custom

        Creates a brush with a custom shader.

        Args:
            function_body: Graph of String
            helpers: Graph of String
            inputs: Graph of Dictionary
            radius: Graph of Float

        Returns:
            Graph: A graph node producing a Brush.
        """
        function_body_parsed = input_parsers.parse_string_graph(function_body)
        helpers_parsed = input_parsers.parse_string_graph(helpers)
        inputs_parsed = input_parsers.parse_graph(inputs)
        radius_parsed = input_parsers.parse_float_graph(radius)
        result = _internal.brush_custom_internal(function_body_parsed, helpers_parsed, inputs_parsed, radius_parsed)
        return Brush(result)

    @staticmethod
    def solid(color, radius) -> Brush:
        """Brush Solid

        Creates a brush with a color and radius. Will stroke with the solid color.

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
