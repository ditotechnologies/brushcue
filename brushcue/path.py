# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: f6d8a6d29df4252679236276dee9ee83e1edb57bd48a00dc4758abe24fe913ba
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import path_command_list


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

    @staticmethod
    def from_commands(commands) -> Path:
        """Path From Commands

        Creates a path by applying a list of path commands in order. Each subpath must start with a move to command.

        Args:
            commands: Graph of PathCommandList

        Returns:
            Graph: A graph node producing a Path.
        """
        commands_parsed = input_parsers.parse_graph(commands)
        result = _internal.path_from_commands_internal(commands_parsed)
        return Path(result)

    @staticmethod
    def from_stylus(path, smooth_factor) -> Path:
        """Path From Stylus

        Creates a path from a stylus capture.

        Args:
            path: Graph of String
            smooth_factor: Graph of Float

        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_string_graph(path)
        smooth_factor_parsed = input_parsers.parse_float_graph(smooth_factor)
        result = _internal.path_from_stylus_internal(path_parsed, smooth_factor_parsed)
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

    def to_commands(self) -> path_command_list.PathCommandList:
        """Path To Commands

        Creates a list of path commands that rebuild this path.

        Returns:
            Graph: A graph node producing a PathCommandList.
        """
        path_parsed = input_parsers.parse_graph(self)
        result = _internal.path_to_commands_internal(path_parsed)
        from .path_command_list import PathCommandList
        return PathCommandList(result)
