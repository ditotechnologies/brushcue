# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: b0ba8867d241da6046eddae306e68075c4dc60b251ff024a49a2a2a2d3de2320
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import float



class OkLabHist(_GraphWrapper):
    """A histogram in various dimensions over the OkLab color-format space."""

    def execute(self, context):

        return self._inner.execute(context)


    def lightness_percentile(self, quantile) -> float.Float:
        """OkLab Histogram Lightness Quantile

        Given an OkLab histogram and a quantile, returns the lightness value that corresponds to the quantile.
    
        Args:
            quantile: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Float.
        """
        hist_parsed = input_parsers.parse_graph(self)
        quantile_parsed = input_parsers.parse_float_graph(quantile)
        result = _internal.ok_lab_hist_lightness_quantile_internal(hist_parsed, quantile_parsed)

        from .float import Float
        return Float(result)

