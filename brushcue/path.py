# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 82ba4d517abc4830e2007cf4a5f238c59c8b4b7390342ff85851c10f2dd31467
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

    def drawing_move(self, point, time, pressure, azimuth_angle, altitude_angle, tension) -> Path:
        """Path Drawing Move

        Represents a move in a freehand drawing.

        Args:
            point: Graph of Point2f
            time: Graph of Float
            pressure: Graph of Float
            azimuth_angle: Graph of Float
            altitude_angle: Graph of Float
            tension: Graph of Float

        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_graph(self)
        point_parsed = input_parsers.parse_graph(point)
        time_parsed = input_parsers.parse_float_graph(time)
        pressure_parsed = input_parsers.parse_float_graph(pressure)
        azimuth_angle_parsed = input_parsers.parse_float_graph(azimuth_angle)
        altitude_angle_parsed = input_parsers.parse_float_graph(altitude_angle)
        tension_parsed = input_parsers.parse_float_graph(tension)
        result = _internal.path_drawing_move_internal(path_parsed, point_parsed, time_parsed, pressure_parsed, azimuth_angle_parsed, altitude_angle_parsed, tension_parsed)
        return Path(result)

    def drawing_start(self, time, point, pressure, azimuth_angle, altitude_angle) -> Path:
        """Path Drawing Start

        Represents the start of a freehand drawing.

        Args:
            time: Graph of Float
            point: Graph of Point2f
            pressure: Graph of Float
            azimuth_angle: Graph of Float
            altitude_angle: Graph of Float

        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_graph(self)
        time_parsed = input_parsers.parse_float_graph(time)
        point_parsed = input_parsers.parse_graph(point)
        pressure_parsed = input_parsers.parse_float_graph(pressure)
        azimuth_angle_parsed = input_parsers.parse_float_graph(azimuth_angle)
        altitude_angle_parsed = input_parsers.parse_float_graph(altitude_angle)
        result = _internal.path_drawing_start_internal(path_parsed, time_parsed, point_parsed, pressure_parsed, azimuth_angle_parsed, altitude_angle_parsed)
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

    def quadratic_bezier_to_point(self, control_point, point) -> Path:
        """Path Quadratic Bézier to Point

        Moves the path from it's current point to another with a quadratic Bézier curve bent toward a control point.

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
