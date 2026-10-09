# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: bf04200afe5cb64054f39cd5487602abf460cd8a64f8ab585b14aed6dfb69034
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import float
    from . import ok_lch_a


class OkLabA(Object):
    """An OkLab color with an alpha component."""

    def execute(self, context):
        return self._inner.execute(context).as_ok_lab_a()

    def a(self) -> float.Float:
        """OkLab Color a

        Gets the a component of an OkLab color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        ok_lab_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lab_a_a_internal(ok_lab_a_parsed)
        from .float import Float
        return Float(result)

    def alpha(self) -> float.Float:
        """OkLab Color Alpha

        Gets the alpha component of an OkLab color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        ok_lab_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lab_a_alpha_internal(ok_lab_a_parsed)
        from .float import Float
        return Float(result)

    def b(self) -> float.Float:
        """OkLab Color b

        Gets the b component of an OkLab color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        ok_lab_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lab_a_b_internal(ok_lab_a_parsed)
        from .float import Float
        return Float(result)

    @staticmethod
    def from_components(l, a, b, alpha) -> OkLabA:
        """OkLab Color with Alpha from Components

        Given the L, a, b and alpha creates the color

        Args:
            l: Graph of Float
            a: Graph of Float
            b: Graph of Float
            alpha: Graph of Float

        Returns:
            Graph: A graph node producing a OkLabA.
        """
        l_parsed = input_parsers.parse_float_graph(l)
        a_parsed = input_parsers.parse_float_graph(a)
        b_parsed = input_parsers.parse_float_graph(b)
        alpha_parsed = input_parsers.parse_float_graph(alpha)
        result = _internal.ok_lab_a_from_components_internal(l_parsed, a_parsed, b_parsed, alpha_parsed)
        return OkLabA(result)

    def l(self) -> float.Float:
        """OkLab Color L

        Gets the L component of an OkLab color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        ok_lab_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lab_a_l_internal(ok_lab_a_parsed)
        from .float import Float
        return Float(result)

    def to_oklcha(self) -> ok_lch_a.OkLchA:
        """OkLab with Alpha to OkLch with Alpha

        Converts OkLab to OkLch, preserving lightness and alpha. Hue is in radians.

        Returns:
            Graph: A graph node producing a OkLchA.
        """
        ok_lab_a_parsed = input_parsers.parse_graph(self)
        result = _internal.ok_lab_a_to_ok_lch_a_internal(ok_lab_a_parsed)
        from .ok_lch_a import OkLchA
        return OkLchA(result)
