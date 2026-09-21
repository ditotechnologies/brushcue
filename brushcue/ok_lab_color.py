# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 1a79ffbeef9ac6d01d1414d889e8ea9ce06b76a13dc4d99777ac0edf335af22f
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class OkLabColor(Object):
    """A color in the OkLab color space, which is designed to be perceptually uniform. L represents lightness. Negative "a" for green. Positive "a" for red. Negative "b" for blue. Positive "b" for yellow."""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def from_components(l, a, b) -> OkLabColor:
        """OkLab Color from Components

        Given the L, a and b creates the color

        Args:
            l: Graph of Float
            a: Graph of Float
            b: Graph of Float

        Returns:
            Graph: A graph node producing a OkLabColor.
        """
        l_parsed = input_parsers.parse_float_graph(l)
        a_parsed = input_parsers.parse_float_graph(a)
        b_parsed = input_parsers.parse_float_graph(b)
        result = _internal.ok_lab_color_from_components_internal(l_parsed, a_parsed, b_parsed)
        return OkLabColor(result)
