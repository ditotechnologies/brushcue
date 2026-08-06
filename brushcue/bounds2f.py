# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 9b3976b223cf6420f0980b74d97d8f9384fc80c61c898cbb4298e43d82d1c60a
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import float



class Bounds2f(_GraphWrapper):
    """A 2D bounding box of Floats"""

    def execute(self, context):

        return self._inner.execute(context).as_bounds2f()


    @staticmethod
    def from_x_y_width_height(x, y, width, height) -> Bounds2f:
        """Bounds 2D Float from X, Y, Width & Height

        Creates the bounds of a 2D float region from its X, Y, Width and Height.
    
        Args:
            x: Graph of Float
            y: Graph of Float
            width: Graph of Float
            height: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Bounds2f.
        """
        x_parsed = input_parsers.parse_float_graph(x)
        y_parsed = input_parsers.parse_float_graph(y)
        width_parsed = input_parsers.parse_float_graph(width)
        height_parsed = input_parsers.parse_float_graph(height)
        result = _internal.bounds2f_from_x_y_width_height_internal(x_parsed, y_parsed, width_parsed, height_parsed)

        return Bounds2f(result)

    def height(self) -> float.Float:
        """Bounds2f Height

        Gets the height of the bounds.
    
        Returns:
            Graph: A graph node producing a Float.
        """
        bounds_parsed = input_parsers.parse_graph(self)
        result = _internal.bounds2f_height_internal(bounds_parsed)

        from .float import Float
        return Float(result)

    def min_x(self) -> float.Float:
        """Bounds2f Min X

        Gets the minimum X coordinate (left edge) of the bounds.
    
        Returns:
            Graph: A graph node producing a Float.
        """
        bounds_parsed = input_parsers.parse_graph(self)
        result = _internal.bounds2f_min_x_internal(bounds_parsed)

        from .float import Float
        return Float(result)

    def min_y(self) -> float.Float:
        """Bounds2f Min Y

        Gets the minimum Y coordinate (top edge) of the bounds.
    
        Returns:
            Graph: A graph node producing a Float.
        """
        bounds_parsed = input_parsers.parse_graph(self)
        result = _internal.bounds2f_min_y_internal(bounds_parsed)

        from .float import Float
        return Float(result)

    def width(self) -> float.Float:
        """Bounds2f Width

        Gets the width of the bounds.
    
        Returns:
            Graph: A graph node producing a Float.
        """
        bounds_parsed = input_parsers.parse_graph(self)
        result = _internal.bounds2f_width_internal(bounds_parsed)

        from .float import Float
        return Float(result)

