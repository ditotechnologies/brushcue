# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: d99e3359665249a02eccdcfadcfcb31f3a306f550c48c8a7e95e9c75ca8d910f
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class Painter(_GraphWrapper):
    """Can draw in 2D. Using paths, brushes, fills and transforms to create your artwork."""

    def execute(self, context):

        return self._inner.execute(context)


    def add_ellipse_with_render_style(self, center, dimensions, rotation, render_style, instances) -> Painter:
        """Painter Add Ellipse with Render Style

        Adds an ellipse to the painter and draws it with the render style. Set some transforms on the ellipse as well.
    
        Args:
            center: Graph of Point2f
            dimensions: Graph of Vector2f
            rotation: Graph of Float
            render_style: Graph of RenderStyle
            instances: Graph of Transform2List
            
    
        Returns:
            Graph: A graph node producing a Painter.
        """
        painter_parsed = input_parsers.parse_graph(self)
        center_parsed = input_parsers.parse_graph(center)
        dimensions_parsed = input_parsers.parse_graph(dimensions)
        rotation_parsed = input_parsers.parse_float_graph(rotation)
        render_style_parsed = input_parsers.parse_graph(render_style)
        instances_parsed = input_parsers.parse_graph(instances)
        result = _internal.painter_add_ellipse_with_render_style_internal(painter_parsed, center_parsed, dimensions_parsed, rotation_parsed, render_style_parsed, instances_parsed)

        return Painter(result)

    def add_path_with_render_style(self, path, render_style, instances) -> Painter:
        """Painter Add Path with Render Style

        Adds a path to the painter and draws it with the render style. Set some transforms on the path as well.
    
        Args:
            path: Graph of Path
            render_style: Graph of RenderStyle
            instances: Graph of Transform2List
            
    
        Returns:
            Graph: A graph node producing a Painter.
        """
        painter_parsed = input_parsers.parse_graph(self)
        path_parsed = input_parsers.parse_graph(path)
        render_style_parsed = input_parsers.parse_graph(render_style)
        instances_parsed = input_parsers.parse_graph(instances)
        result = _internal.painter_add_path_with_render_style_internal(painter_parsed, path_parsed, render_style_parsed, instances_parsed)

        return Painter(result)

    def add_rectangle_with_render_style(self, center, dimensions, rotation, render_style, instances) -> Painter:
        """Painter Add Rectangle with Render Style

        Adds a rectangle to the painter and draws it with the render style. Set some transforms on the rectangle as well.
    
        Args:
            center: Graph of Point2f
            dimensions: Graph of Vector2f
            rotation: Graph of Float
            render_style: Graph of RenderStyle
            instances: Graph of Transform2List
            
    
        Returns:
            Graph: A graph node producing a Painter.
        """
        painter_parsed = input_parsers.parse_graph(self)
        center_parsed = input_parsers.parse_graph(center)
        dimensions_parsed = input_parsers.parse_graph(dimensions)
        rotation_parsed = input_parsers.parse_float_graph(rotation)
        render_style_parsed = input_parsers.parse_graph(render_style)
        instances_parsed = input_parsers.parse_graph(instances)
        result = _internal.painter_add_rectangle_with_render_style_internal(painter_parsed, center_parsed, dimensions_parsed, rotation_parsed, render_style_parsed, instances_parsed)

        return Painter(result)

    @staticmethod
    def new() -> Painter:
        """Painter New

        Creates a new painter.
    
        Returns:
            Graph: A graph node producing a Painter.
        """
        result = _internal.painter_new_internal()

        return Painter(result)

