# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 85feaabdce66225905f082793c404ec6b9a0013b6c762583d1a6e4ee72957d1e
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

    def set_eraser(self) -> RenderStyle:
        """Render Style Set Eraser

        Sets the render style to an eraser.

        Returns:
            Graph: A graph node producing a RenderStyle.
        """
        render_style_parsed = input_parsers.parse_graph(self)
        result = _internal.render_style_set_eraser_internal(render_style_parsed)
        return RenderStyle(result)
