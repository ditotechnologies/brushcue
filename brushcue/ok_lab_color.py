# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: d947fbf0043467aa4bec60167660624057933c4688e99ef84bfbdf210ff5c71c
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class OkLabColor(_GraphWrapper):
    """A color-format in the OkLab color-format space, which is designed to be perceptually uniform. L represents lightness. Negative "a" for green. Positive "a" for red. Negative "b" for blue. Positive "b" for yellow."""

    def execute(self, context):

        return self._inner.execute(context)


    @staticmethod
    def from_components(l, a, b) -> OkLabColor:
        """OkLab Color from Components

        Given the L, a and b creates the color-format
    
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

