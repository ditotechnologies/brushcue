# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 46623315e554c1ff2447af61fa078724ec1a426454f6988023f523444ae8d0d8
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class Path(_GraphWrapper):
    """A 2D path that can be used to be rendered."""

    def execute(self, context):

        return self._inner.execute(context)


    def cardinal_cubic_to_point(self, point, tension) -> Path:
        """Path Cardinal Cubic to Point

        Moves the path from it's current point to another with a Cardinal Cubic spline.
    
        Args:
            point: Graph of Point2f
            tension: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_graph(self)
        point_parsed = input_parsers.parse_graph(point)
        tension_parsed = input_parsers.parse_float_graph(tension)
        result = _internal.path_cardinal_cubic_to_point_internal(path_parsed, point_parsed, tension_parsed)

        return Path(result)

    def catmull_rom_to_point(self, point) -> Path:
        """Path Catmull-Rom to Point

        Moves the path from it's current point to another with a Catmull-Rom spline.
    
        Args:
            point: Graph of Point2f
            
    
        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_graph(self)
        point_parsed = input_parsers.parse_graph(point)
        result = _internal.path_catmull_rom_to_point_internal(path_parsed, point_parsed)

        return Path(result)

    def line_to_point(self, point) -> Path:
        """Path Line to Point

        Moves the path from it's current point to another at another point with a line.
    
        Args:
            point: Graph of Point2f
            
    
        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_graph(self)
        point_parsed = input_parsers.parse_graph(point)
        result = _internal.path_line_to_point_internal(path_parsed, point_parsed)

        return Path(result)

    def move_to_point(self, point) -> Path:
        """Path Move to Point

        Moves the path to a specified point without drawing anything.
    
        Args:
            point: Graph of Point2f
            
    
        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_graph(self)
        point_parsed = input_parsers.parse_graph(point)
        result = _internal.path_move_to_point_internal(path_parsed, point_parsed)

        return Path(result)

    @staticmethod
    def new() -> Path:
        """Path New

        Creates a new empty path.
    
        Returns:
            Graph: A graph node producing a Path.
        """
        result = _internal.path_new_internal()

        return Path(result)

