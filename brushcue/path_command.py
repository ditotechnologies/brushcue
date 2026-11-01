# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: fe6d5bfa73789fe31cb7fd4dfafb27e0ceec21814e2fb269963a72ede3d287b3
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import bool
    from . import float
    from . import point2f


class PathCommand(Object):
    """A command to modify a 2D path"""

    def execute(self, context):
        return self._inner.execute(context)

    def altitude_angle(self) -> float.Float:
        """Path Command Altitude Angle

        Gets the altitude angle of this path command's end point, in radians.

        Returns:
            Graph: A graph node producing a Float.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_altitude_angle_internal(command_parsed)
        from .float import Float
        return Float(result)

    def azimuth_angle(self) -> float.Float:
        """Path Command Azimuth Angle

        Gets the azimuth angle of this path command's end point, in radians.

        Returns:
            Graph: A graph node producing a Float.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_azimuth_angle_internal(command_parsed)
        from .float import Float
        return Float(result)

    @staticmethod
    def cardinal_cubic_to_point(coordinate, time, pressure, azimuth_angle, altitude_angle, tension) -> PathCommand:
        """Path Command Cardinal Cubic To

        A command for a path to draw a Cardinal Cubic spline to a point.

        Args:
            coordinate: Graph of Point2f
            time: Graph of Float
            pressure: Graph of Float
            azimuth_angle: Graph of Float
            altitude_angle: Graph of Float
            tension: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        coordinate_parsed = input_parsers.parse_graph(coordinate)
        time_parsed = input_parsers.parse_float_graph(time)
        pressure_parsed = input_parsers.parse_float_graph(pressure)
        azimuth_angle_parsed = input_parsers.parse_float_graph(azimuth_angle)
        altitude_angle_parsed = input_parsers.parse_float_graph(altitude_angle)
        tension_parsed = input_parsers.parse_float_graph(tension)
        result = _internal.path_command_cardinal_cubic_to_point_internal(coordinate_parsed, time_parsed, pressure_parsed, azimuth_angle_parsed, altitude_angle_parsed, tension_parsed)
        return PathCommand(result)

    @staticmethod
    def catmull_rom_to_point(coordinate, time, pressure, azimuth_angle, altitude_angle) -> PathCommand:
        """Path Command Catmull-Rom To

        A command for a path to draw a Catmull-Rom spline to a point.

        Args:
            coordinate: Graph of Point2f
            time: Graph of Float
            pressure: Graph of Float
            azimuth_angle: Graph of Float
            altitude_angle: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        coordinate_parsed = input_parsers.parse_graph(coordinate)
        time_parsed = input_parsers.parse_float_graph(time)
        pressure_parsed = input_parsers.parse_float_graph(pressure)
        azimuth_angle_parsed = input_parsers.parse_float_graph(azimuth_angle)
        altitude_angle_parsed = input_parsers.parse_float_graph(altitude_angle)
        result = _internal.path_command_catmull_rom_to_point_internal(coordinate_parsed, time_parsed, pressure_parsed, azimuth_angle_parsed, altitude_angle_parsed)
        return PathCommand(result)

    def control_point(self) -> point2f.Point2f:
        """Path Command Control Point

        Gets the control point of a quadratic Bézier command. Only works on quadratic Bézier commands and fails on any other type.

        Returns:
            Graph: A graph node producing a Point2f.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_control_point_internal(command_parsed)
        from .point2f import Point2f
        return Point2f(result)

    def control_point_1(self) -> point2f.Point2f:
        """Path Command Control Point 1

        Gets the first control point of a cubic Bézier command. Only works on cubic Bézier commands and fails on any other type.

        Returns:
            Graph: A graph node producing a Point2f.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_control_point1_internal(command_parsed)
        from .point2f import Point2f
        return Point2f(result)

    def control_point_2(self) -> point2f.Point2f:
        """Path Command Control Point 2

        Gets the second control point of a cubic Bézier command. Only works on cubic Bézier commands and fails on any other type.

        Returns:
            Graph: A graph node producing a Point2f.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_control_point2_internal(command_parsed)
        from .point2f import Point2f
        return Point2f(result)

    def coordinate(self) -> point2f.Point2f:
        """Path Command Coordinate

        Gets the coordinate of this path command's end point.

        Returns:
            Graph: A graph node producing a Point2f.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_coordinate_internal(command_parsed)
        from .point2f import Point2f
        return Point2f(result)

    @staticmethod
    def cubic_bezier_to_point(control_point_1, control_point_2, coordinate, time, pressure, azimuth_angle, altitude_angle) -> PathCommand:
        """Path Command Cubic Bézier To

        A command for a path to draw a cubic Bézier curve to a point, shaped by two control points.

        Args:
            control_point_1: Graph of Point2f
            control_point_2: Graph of Point2f
            coordinate: Graph of Point2f
            time: Graph of Float
            pressure: Graph of Float
            azimuth_angle: Graph of Float
            altitude_angle: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        control_point_1_parsed = input_parsers.parse_graph(control_point_1)
        control_point_2_parsed = input_parsers.parse_graph(control_point_2)
        coordinate_parsed = input_parsers.parse_graph(coordinate)
        time_parsed = input_parsers.parse_float_graph(time)
        pressure_parsed = input_parsers.parse_float_graph(pressure)
        azimuth_angle_parsed = input_parsers.parse_float_graph(azimuth_angle)
        altitude_angle_parsed = input_parsers.parse_float_graph(altitude_angle)
        result = _internal.path_command_cubic_bezier_to_point_internal(control_point_1_parsed, control_point_2_parsed, coordinate_parsed, time_parsed, pressure_parsed, azimuth_angle_parsed, altitude_angle_parsed)
        return PathCommand(result)

    def is_cardinal_cubic(self) -> bool.Bool:
        """Path Command Is Cardinal Cubic

        Returns whether this path command is a Cardinal Cubic command.

        Returns:
            Graph: A graph node producing a Bool.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_is_cardinal_cubic_internal(command_parsed)
        from .bool import Bool
        return Bool(result)

    def is_catmull_rom(self) -> bool.Bool:
        """Path Command Is Catmull-Rom

        Returns whether this path command is a Catmull-Rom command.

        Returns:
            Graph: A graph node producing a Bool.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_is_catmull_rom_internal(command_parsed)
        from .bool import Bool
        return Bool(result)

    def is_cubic_bezier(self) -> bool.Bool:
        """Path Command Is Cubic Bézier

        Returns whether this path command is a cubic Bézier command.

        Returns:
            Graph: A graph node producing a Bool.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_is_cubic_bezier_internal(command_parsed)
        from .bool import Bool
        return Bool(result)

    def is_line(self) -> bool.Bool:
        """Path Command Is Line

        Returns whether this path command is a line to command.

        Returns:
            Graph: A graph node producing a Bool.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_is_line_internal(command_parsed)
        from .bool import Bool
        return Bool(result)

    def is_move(self) -> bool.Bool:
        """Path Command Is Move

        Returns whether this path command is a move to command.

        Returns:
            Graph: A graph node producing a Bool.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_is_move_internal(command_parsed)
        from .bool import Bool
        return Bool(result)

    def is_quadratic_bezier(self) -> bool.Bool:
        """Path Command Is Quadratic Bézier

        Returns whether this path command is a quadratic Bézier command.

        Returns:
            Graph: A graph node producing a Bool.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_is_quadratic_bezier_internal(command_parsed)
        from .bool import Bool
        return Bool(result)

    @staticmethod
    def line_to_point(coordinate, time, pressure, azimuth_angle, altitude_angle) -> PathCommand:
        """Path Command Line To

        A command for a path to draw a line to a point.

        Args:
            coordinate: Graph of Point2f
            time: Graph of Float
            pressure: Graph of Float
            azimuth_angle: Graph of Float
            altitude_angle: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        coordinate_parsed = input_parsers.parse_graph(coordinate)
        time_parsed = input_parsers.parse_float_graph(time)
        pressure_parsed = input_parsers.parse_float_graph(pressure)
        azimuth_angle_parsed = input_parsers.parse_float_graph(azimuth_angle)
        altitude_angle_parsed = input_parsers.parse_float_graph(altitude_angle)
        result = _internal.path_command_line_to_point_internal(coordinate_parsed, time_parsed, pressure_parsed, azimuth_angle_parsed, altitude_angle_parsed)
        return PathCommand(result)

    @staticmethod
    def move_to_point(coordinate, time, pressure, azimuth_angle, altitude_angle) -> PathCommand:
        """Path Command Move To

        A command for a path to move to a point.

        Args:
            coordinate: Graph of Point2f
            time: Graph of Float
            pressure: Graph of Float
            azimuth_angle: Graph of Float
            altitude_angle: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        coordinate_parsed = input_parsers.parse_graph(coordinate)
        time_parsed = input_parsers.parse_float_graph(time)
        pressure_parsed = input_parsers.parse_float_graph(pressure)
        azimuth_angle_parsed = input_parsers.parse_float_graph(azimuth_angle)
        altitude_angle_parsed = input_parsers.parse_float_graph(altitude_angle)
        result = _internal.path_command_move_to_point_internal(coordinate_parsed, time_parsed, pressure_parsed, azimuth_angle_parsed, altitude_angle_parsed)
        return PathCommand(result)

    def pressure(self) -> float.Float:
        """Path Command Pressure

        Gets the pressure of this path command's end point, from 0 to 1.

        Returns:
            Graph: A graph node producing a Float.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_pressure_internal(command_parsed)
        from .float import Float
        return Float(result)

    @staticmethod
    def quadratic_bezier_to_point(control_point, coordinate, time, pressure, azimuth_angle, altitude_angle) -> PathCommand:
        """Path Command Quadratic Bézier To

        A command for a path to draw a quadratic Bézier curve to a point, bent toward a control point.

        Args:
            control_point: Graph of Point2f
            coordinate: Graph of Point2f
            time: Graph of Float
            pressure: Graph of Float
            azimuth_angle: Graph of Float
            altitude_angle: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        control_point_parsed = input_parsers.parse_graph(control_point)
        coordinate_parsed = input_parsers.parse_graph(coordinate)
        time_parsed = input_parsers.parse_float_graph(time)
        pressure_parsed = input_parsers.parse_float_graph(pressure)
        azimuth_angle_parsed = input_parsers.parse_float_graph(azimuth_angle)
        altitude_angle_parsed = input_parsers.parse_float_graph(altitude_angle)
        result = _internal.path_command_quadratic_bezier_to_point_internal(control_point_parsed, coordinate_parsed, time_parsed, pressure_parsed, azimuth_angle_parsed, altitude_angle_parsed)
        return PathCommand(result)

    def time(self) -> float.Float:
        """Path Command Time

        Gets the time of this path command's end point.

        Returns:
            Graph: A graph node producing a Float.
        """
        command_parsed = input_parsers.parse_graph(self)
        result = _internal.path_command_time_internal(command_parsed)
        from .float import Float
        return Float(result)

    def with_altitude_angle(self, altitude_angle) -> PathCommand:
        """Path Command With Altitude Angle

        Returns this path command with its end point's altitude angle replaced.

        Args:
            altitude_angle: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        command_parsed = input_parsers.parse_graph(self)
        altitude_angle_parsed = input_parsers.parse_float_graph(altitude_angle)
        result = _internal.path_command_with_altitude_angle_internal(command_parsed, altitude_angle_parsed)
        return PathCommand(result)

    def with_azimuth_angle(self, azimuth_angle) -> PathCommand:
        """Path Command With Azimuth Angle

        Returns this path command with its end point's azimuth angle replaced.

        Args:
            azimuth_angle: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        command_parsed = input_parsers.parse_graph(self)
        azimuth_angle_parsed = input_parsers.parse_float_graph(azimuth_angle)
        result = _internal.path_command_with_azimuth_angle_internal(command_parsed, azimuth_angle_parsed)
        return PathCommand(result)

    def with_control_point(self, control_point) -> PathCommand:
        """Path Command With Control Point

        Returns this quadratic Bézier command with its control point replaced. Only works on quadratic Bézier commands and fails on any other type.

        Args:
            control_point: Graph of Point2f

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        command_parsed = input_parsers.parse_graph(self)
        control_point_parsed = input_parsers.parse_graph(control_point)
        result = _internal.path_command_with_control_point_internal(command_parsed, control_point_parsed)
        return PathCommand(result)

    def with_control_point_1(self, control_point_1) -> PathCommand:
        """Path Command With Control Point 1

        Returns this cubic Bézier command with its first control point replaced. Only works on cubic Bézier commands and fails on any other type.

        Args:
            control_point_1: Graph of Point2f

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        command_parsed = input_parsers.parse_graph(self)
        control_point_1_parsed = input_parsers.parse_graph(control_point_1)
        result = _internal.path_command_with_control_point1_internal(command_parsed, control_point_1_parsed)
        return PathCommand(result)

    def with_control_point_2(self, control_point_2) -> PathCommand:
        """Path Command With Control Point 2

        Returns this cubic Bézier command with its second control point replaced. Only works on cubic Bézier commands and fails on any other type.

        Args:
            control_point_2: Graph of Point2f

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        command_parsed = input_parsers.parse_graph(self)
        control_point_2_parsed = input_parsers.parse_graph(control_point_2)
        result = _internal.path_command_with_control_point2_internal(command_parsed, control_point_2_parsed)
        return PathCommand(result)

    def with_coordinate(self, coordinate) -> PathCommand:
        """Path Command With Coordinate

        Returns this path command with its end point's coordinate replaced.

        Args:
            coordinate: Graph of Point2f

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        command_parsed = input_parsers.parse_graph(self)
        coordinate_parsed = input_parsers.parse_graph(coordinate)
        result = _internal.path_command_with_coordinate_internal(command_parsed, coordinate_parsed)
        return PathCommand(result)

    def with_pressure(self, pressure) -> PathCommand:
        """Path Command With Pressure

        Returns this path command with its end point's pressure replaced.

        Args:
            pressure: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        command_parsed = input_parsers.parse_graph(self)
        pressure_parsed = input_parsers.parse_float_graph(pressure)
        result = _internal.path_command_with_pressure_internal(command_parsed, pressure_parsed)
        return PathCommand(result)

    def with_time(self, time) -> PathCommand:
        """Path Command With Time

        Returns this path command with its end point's time replaced.

        Args:
            time: Graph of Float

        Returns:
            Graph: A graph node producing a PathCommand.
        """
        command_parsed = input_parsers.parse_graph(self)
        time_parsed = input_parsers.parse_float_graph(time)
        result = _internal.path_command_with_time_internal(command_parsed, time_parsed)
        return PathCommand(result)
