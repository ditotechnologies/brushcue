# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 5be86f886e4712511073cbfb52149e04d955bb9905555cecebd1d7bdc5df3997
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import float


class XYZA(Object):
    """A CIE XYZ color with an alpha component."""

    def execute(self, context):
        return self._inner.execute(context)

    def alpha(self) -> float.Float:
        """XYZ Color Alpha

        Gets the alpha component of an XYZ color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        xyza_parsed = input_parsers.parse_graph(self)
        result = _internal.x_y_z_a_alpha_internal(xyza_parsed)
        from .float import Float
        return Float(result)

    @staticmethod
    def from_components(x, y, z, alpha) -> XYZA:
        """XYZ Color with Alpha from Components

        Creates an XYZ color with alpha from its components.

        Args:
            x: Graph of Float
            y: Graph of Float
            z: Graph of Float
            alpha: Graph of Float

        Returns:
            Graph: A graph node producing a XYZA.
        """
        x_parsed = input_parsers.parse_float_graph(x)
        y_parsed = input_parsers.parse_float_graph(y)
        z_parsed = input_parsers.parse_float_graph(z)
        alpha_parsed = input_parsers.parse_float_graph(alpha)
        result = _internal.x_y_z_a_from_components_internal(x_parsed, y_parsed, z_parsed, alpha_parsed)
        return XYZA(result)

    def x(self) -> float.Float:
        """XYZ Color X

        Gets the X tristimulus value of an XYZ color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        xyza_parsed = input_parsers.parse_graph(self)
        result = _internal.x_y_z_a_x_internal(xyza_parsed)
        from .float import Float
        return Float(result)

    def y(self) -> float.Float:
        """XYZ Color Y

        Gets the Y tristimulus value of an XYZ color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        xyza_parsed = input_parsers.parse_graph(self)
        result = _internal.x_y_z_a_y_internal(xyza_parsed)
        from .float import Float
        return Float(result)

    def z(self) -> float.Float:
        """XYZ Color Z

        Gets the Z tristimulus value of an XYZ color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        xyza_parsed = input_parsers.parse_graph(self)
        result = _internal.x_y_z_a_z_internal(xyza_parsed)
        from .float import Float
        return Float(result)
