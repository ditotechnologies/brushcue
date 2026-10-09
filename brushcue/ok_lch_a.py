# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 4fde7952e90f6abb29dbfef3d72c1847d1a5d9eb5ceedd4030ee3d58e9d07aaa
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import float
    from . import ok_lab_a


class OkLchA(Object):
    """An OkLch color with an alpha component."""

    def execute(self, context):
        return self._inner.execute(context).as_ok_lch_a()

    def alpha(self) -> float.Float:
        """OkLch Color Alpha

        Gets the alpha component of an OkLch color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        ok_lch_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lch_a_alpha_internal(ok_lch_a_parsed)
        from .float import Float
        return Float(result)

    def c(self) -> float.Float:
        """OkLch Color c

        Gets the c component of an OkLch color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        ok_lch_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lch_a_c_internal(ok_lch_a_parsed)
        from .float import Float
        return Float(result)

    @staticmethod
    def from_components(l, c, h, alpha) -> OkLchA:
        """OkLch Color with Alpha from Components

        Given the L, chroma, hue in radians and alpha creates the color

        Args:
            l: Graph of Float
            c: Graph of Float
            h: Graph of Float
            alpha: Graph of Float

        Returns:
            Graph: A graph node producing a OkLchA.
        """
        l_parsed = input_parsers.parse_float_graph(l)
        c_parsed = input_parsers.parse_float_graph(c)
        h_parsed = input_parsers.parse_float_graph(h)
        alpha_parsed = input_parsers.parse_float_graph(alpha)
        result = _internal.ok_lch_a_from_components_internal(l_parsed, c_parsed, h_parsed, alpha_parsed)
        return OkLchA(result)

    def h(self) -> float.Float:
        """OkLch Color h

        Gets the hue in radians of an OkLch color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        ok_lch_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lch_a_h_internal(ok_lch_a_parsed)
        from .float import Float
        return Float(result)

    def l(self) -> float.Float:
        """OkLch Color L

        Gets the L component of an OkLch color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        ok_lch_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lch_a_l_internal(ok_lch_a_parsed)
        from .float import Float
        return Float(result)

    def to_oklaba(self) -> ok_lab_a.OkLabA:
        """OkLch with Alpha to OkLab with Alpha

        Converts OkLch to OkLab, preserving lightness and alpha. Hue is in radians.

        Returns:
            Graph: A graph node producing a OkLabA.
        """
        ok_lch_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lch_a_to_ok_lab_a_internal(ok_lch_a_parsed)
        from .ok_lab_a import OkLabA
        return OkLabA(result)
