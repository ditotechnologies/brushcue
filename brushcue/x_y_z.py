# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 03c8be696f34eca1fedfdeae1f1cde645fd4c7087c8cff8c32a6ce87ff802284
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class XYZ(Object):
    """A color in the CIE XYZ color space."""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def whitepoint_from_kelvin(kelvin) -> XYZ:
        """XYZ White Point from Kelvin

        The white point of a light at the given color temperature in Kelvin, with a luminance (Y) of 1. 5003K is D50, the profile connection white point.

        Args:
            kelvin: Graph of Float

        Returns:
            Graph: A graph node producing a XYZ.
        """
        kelvin_parsed = input_parsers.parse_float_graph(kelvin)
        result = _internal.x_y_z_whitepoint_from_kelvin_internal(kelvin_parsed)
        return XYZ(result)
