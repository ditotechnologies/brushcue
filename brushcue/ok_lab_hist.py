# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: bce013335cfa83157933645437ff720f8de1375d13ab7752ad9a8a17b6171699
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import float


class OkLabHist(Object):
    """A histogram in various dimensions over the OkLab color space."""

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
