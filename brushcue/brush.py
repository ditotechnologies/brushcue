# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: bc3d443d39786a862da078fcd49af3cb128b6414da9436844ed97baa5465dff5
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
    def dashed(color_1, color_1_length, color_2, color_2_length, radius) -> Brush:
        """Brush Dashed

        Creates a brush that alternates between two colors along the length of the path, for dashed/dotted strokes.

        Args:
            color_1: Graph of ProfiledColor
            color_1_length: Graph of Float
            color_2: Graph of ProfiledColor
            color_2_length: Graph of Float
            radius: Graph of Float

        Returns:
            Graph: A graph node producing a Brush.
        """
        color_1_parsed = input_parsers.parse_graph(color_1)
        color_1_length_parsed = input_parsers.parse_float_graph(color_1_length)
        color_2_parsed = input_parsers.parse_graph(color_2)
        color_2_length_parsed = input_parsers.parse_float_graph(color_2_length)
        radius_parsed = input_parsers.parse_float_graph(radius)
        result = _internal.brush_dashed_internal(color_1_parsed, color_1_length_parsed, color_2_parsed, color_2_length_parsed, radius_parsed)
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
