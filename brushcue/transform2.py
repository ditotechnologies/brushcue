# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: c151b5aa9178dc11ac008d8ee89395ffd587454e35b656977d94ae6ce09f8779
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class Transform2(Object):
    """A 2D Transformation"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def identity() -> Transform2:
        """Transform 2D Identity

        Creates a 2D transform that is the identity transform.

        Returns:
            Graph: A graph node producing a Transform2.
        """
        result = _internal.transform2_identity_internal()
        return Transform2(result)

    def rotate(self, angle) -> Transform2:
        """Transform 2D Rotate

        Applies a rotation to a 2D transform. Rotation is in radians.

        Args:
            angle: Graph of Float

        Returns:
            Graph: A graph node producing a Transform2.
        """
        transform_parsed = input_parsers.parse_graph(self)
        angle_parsed = input_parsers.parse_float_graph(angle)
        result = _internal.transform2_rotate_internal(transform_parsed, angle_parsed)
        return Transform2(result)

    def scale(self, scale) -> Transform2:
        """Transform 2D Scale

        Applies a scale to a 2D transform.

        Args:
            scale: Graph of Vector2f

        Returns:
            Graph: A graph node producing a Transform2.
        """
        transform_parsed = input_parsers.parse_graph(self)
        scale_parsed = input_parsers.parse_graph(scale)
        result = _internal.transform2_scale_internal(transform_parsed, scale_parsed)
        return Transform2(result)

    def translation(self, translation) -> Transform2:
        """Transform 2D Translation

        Applies a translation to a 2D transform.

        Args:
            translation: Graph of Vector2f

        Returns:
            Graph: A graph node producing a Transform2.
        """
        transform_parsed = input_parsers.parse_graph(self)
        translation_parsed = input_parsers.parse_graph(translation)
        result = _internal.transform2_translation_internal(transform_parsed, translation_parsed)
        return Transform2(result)
