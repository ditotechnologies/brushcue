# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 604ca028dca2a6659ec236e480e6802909a38d849995744567d6fc3ed22512c3
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import bool
    from . import float
    from . import path
    from . import point2f
    from . import render_style
    from . import transform2_list
    from . import vector2f


class PaintedIllustration(Object):
    """A single item drawn by a painter. A path, rectangle or ellipse together with the render style it is drawn with and its instance transforms."""

    def execute(self, context):
        return self._inner.execute(context)

    def center(self) -> point2f.Point2f:
        """Painted Illustration Center

        Gets the center point of a rectangle or ellipse. Fails on paths.

        Returns:
            Graph: A graph node producing a Point2f.
        """
        illustration_parsed = input_parsers.parse_graph(self)
        result = _internal.painted_illustration_center_internal(illustration_parsed)
        from .point2f import Point2f
        return Point2f(result)

    def dimensions(self) -> vector2f.Vector2f:
        """Painted Illustration Dimensions

        Gets the width and height of a rectangle, or the a and b radii of an ellipse. Fails on paths.

        Returns:
            Graph: A graph node producing a Vector2f.
        """
        illustration_parsed = input_parsers.parse_graph(self)
        result = _internal.painted_illustration_dimensions_internal(illustration_parsed)
        from .vector2f import Vector2f
        return Vector2f(result)

    def instances(self) -> transform2_list.Transform2List:
        """Painted Illustration Instances

        Gets the transforms this painted illustration is drawn with. It is drawn once for each transform.

        Returns:
            Graph: A graph node producing a Transform2List.
        """
        illustration_parsed = input_parsers.parse_graph(self)
        result = _internal.painted_illustration_instances_internal(illustration_parsed)
        from .transform2_list import Transform2List
        return Transform2List(result)

    def is_ellipse(self) -> bool.Bool:
        """Painted Illustration Is Ellipse

        Returns whether this painted illustration is an ellipse.

        Returns:
            Graph: A graph node producing a Bool.
        """
        illustration_parsed = input_parsers.parse_graph(self)
        result = _internal.painted_illustration_is_ellipse_internal(illustration_parsed)
        from .bool import Bool
        return Bool(result)

    def is_path(self) -> bool.Bool:
        """Painted Illustration Is Path

        Returns whether this painted illustration is a path.

        Returns:
            Graph: A graph node producing a Bool.
        """
        illustration_parsed = input_parsers.parse_graph(self)
        result = _internal.painted_illustration_is_path_internal(illustration_parsed)
        from .bool import Bool
        return Bool(result)

    def is_rectangle(self) -> bool.Bool:
        """Painted Illustration Is Rectangle

        Returns whether this painted illustration is a rectangle.

        Returns:
            Graph: A graph node producing a Bool.
        """
        illustration_parsed = input_parsers.parse_graph(self)
        result = _internal.painted_illustration_is_rectangle_internal(illustration_parsed)
        from .bool import Bool
        return Bool(result)

    def path(self) -> path.Path:
        """Painted Illustration Path

        Gets the path of this painted illustration. Only works on paths and fails on rectangles and ellipses.

        Returns:
            Graph: A graph node producing a Path.
        """
        illustration_parsed = input_parsers.parse_graph(self)
        result = _internal.painted_illustration_path_internal(illustration_parsed)
        from .path import Path
        return Path(result)

    def render_style(self) -> render_style.RenderStyle:
        """Painted Illustration Render Style

        Gets the render style this painted illustration is drawn with.

        Returns:
            Graph: A graph node producing a RenderStyle.
        """
        illustration_parsed = input_parsers.parse_graph(self)
        result = _internal.painted_illustration_render_style_internal(illustration_parsed)
        from .render_style import RenderStyle
        return RenderStyle(result)

    def rotation(self) -> float.Float:
        """Painted Illustration Rotation

        Gets the rotation in radians of a rectangle or ellipse. Fails on paths.

        Returns:
            Graph: A graph node producing a Float.
        """
        illustration_parsed = input_parsers.parse_graph(self)
        result = _internal.painted_illustration_rotation_internal(illustration_parsed)
        from .float import Float
        return Float(result)
