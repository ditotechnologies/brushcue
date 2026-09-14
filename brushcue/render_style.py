# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: cdf9102b2cc259b9e8c86309dd6fbf1cc6c3220351076e2dfdd03d68c01ae4df
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class RenderStyle(Object):
    """Combining a fill and brush into a render style to create a 2D object."""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def brush_and_fill(brush, fill) -> RenderStyle:
        """Render Style Brush and Fill

        Creates a render style that will have a brush and a fill.

        Args:
            brush: Graph of Brush
            fill: Graph of Fill

        Returns:
            Graph: A graph node producing a RenderStyle.
        """
        brush_parsed = input_parsers.parse_graph(brush)
        fill_parsed = input_parsers.parse_graph(fill)
        result = _internal.render_style_brush_and_fill_internal(brush_parsed, fill_parsed)
        return RenderStyle(result)

    @staticmethod
    def brush_only(brush) -> RenderStyle:
        """Render Style Brush Only

        Creates a render style that will only have a brush.

        Args:
            brush: Graph of Brush

        Returns:
            Graph: A graph node producing a RenderStyle.
        """
        brush_parsed = input_parsers.parse_graph(brush)
        result = _internal.render_style_brush_only_internal(brush_parsed)
        return RenderStyle(result)

    @staticmethod
    def fill_only(fill) -> RenderStyle:
        """Render Style Fill Only

        Creates a render style that will only have a fill.

        Args:
            fill: Graph of Fill

        Returns:
            Graph: A graph node producing a RenderStyle.
        """
        fill_parsed = input_parsers.parse_graph(fill)
        result = _internal.render_style_fill_only_internal(fill_parsed)
        return RenderStyle(result)
