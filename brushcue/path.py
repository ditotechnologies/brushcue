# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 49165f864c3d0c4659035e4ff10c44cd1fd85ec7254087ebc2202d37d9473a90
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class Path(Object):
    """A 2D path that can be used to be rendered."""

    def execute(self, context):
        return self._inner.execute(context)

    def cardinal_cubic_to_point(self, point, tension) -> Path:
        """Path Cardinal Cubic to Point

        Moves the path from its current point to another with a Cardinal Cubic spline.

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

        Moves the path from its current point to another with a Catmull-Rom spline.

        Args:
            point: Graph of Point2f

        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_graph(self)
        point_parsed = input_parsers.parse_graph(point)
        result = _internal.path_catmull_rom_to_point_internal(path_parsed, point_parsed)
        return Path(result)

    def cubic_bezier_to_point(self, control_point_1, control_point_2, point) -> Path:
        """Path Cubic Bézier to Point

        Moves the path from its current point to another with a cubic Bézier curve shaped by two control points.

        Args:
            control_point_1: Graph of Point2f
            control_point_2: Graph of Point2f
            point: Graph of Point2f

        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_graph(self)
        control_point_1_parsed = input_parsers.parse_graph(control_point_1)
        control_point_2_parsed = input_parsers.parse_graph(control_point_2)
        point_parsed = input_parsers.parse_graph(point)
        result = _internal.path_cubic_bezier_to_point_internal(path_parsed, control_point_1_parsed, control_point_2_parsed, point_parsed)
        return Path(result)

    def line_to_point(self, point) -> Path:
        """Path Line to Point

        Moves the path from its current point to another at another point with a line.

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

    def quadratic_bezier_to_point(self, control_point, point) -> Path:
        """Path Quadratic Bézier to Point

        Moves the path from its current point to another with a quadratic Bézier curve bent toward a control point.

        Args:
            control_point: Graph of Point2f
            point: Graph of Point2f

        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_graph(self)
        control_point_parsed = input_parsers.parse_graph(control_point)
        point_parsed = input_parsers.parse_graph(point)
        result = _internal.path_quadratic_bezier_to_point_internal(path_parsed, control_point_parsed, point_parsed)
        return Path(result)
