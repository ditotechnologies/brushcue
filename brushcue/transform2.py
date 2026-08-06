# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 6e1ff6ce522aee5b7518e58365a3b64eb43b028770379ccf54603ea409c526c3
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import transform2_list



class Transform2(_GraphWrapper):
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

    @staticmethod
    def if_(bool, input_1, input_2) -> Transform2:
        """Transform 2D If

        If the boolean is true returns input 1, otherwise input 2. Type: Transform2
    
        Args:
            bool: Graph of Bool
            input_1: Graph of Transform2
            input_2: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Transform2.
        """
        bool_parsed = input_parsers.parse_bool_graph(bool)
        input_1_parsed = input_parsers.parse_graph(input_1)
        input_2_parsed = input_parsers.parse_graph(input_2)
        result = _internal.transform2_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

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

    def to_list(self) -> transform2_list.Transform2List:
        """Transform 2D to List

        Converts Transform 2D to a single item list
    
        Returns:
            Graph: A graph node producing a Transform2List.
        """
        item_parsed = input_parsers.parse_graph(self)
        result = _internal.transform2_to_list_internal(item_parsed)

        from .transform2_list import Transform2List
        return Transform2List(result)

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

