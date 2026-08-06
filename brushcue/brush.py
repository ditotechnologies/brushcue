# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 60776055a5143c5682577933200e365b3788f8acfabea0e2d4e1f67d948bbb3c
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class Brush(_GraphWrapper):
    """A brush to stroke on 2D objects"""

    def execute(self, context):

        return self._inner.execute(context)


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

