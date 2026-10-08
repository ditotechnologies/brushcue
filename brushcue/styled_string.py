# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 66ad6c5fdfeec4f2a02d8f46b330c52aaebb1f9b792443881365a946f92e02da
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import styled_character_list


class StyledString(Object):
    """a string with style"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def styled_string_from_characters_fixed(styled_character_list, bounds) -> StyledString:
        """Styled String from Characters (Fixed)

        Returns a styled string from a list of styled characters that wraps to and is placed within fixed bounds

        Args:
            styled_character_list: Graph of StyledCharacterList
            bounds: Graph of Bounds2f

        Returns:
            Graph: A graph node producing a StyledString.
        """
        styled_character_list_parsed = input_parsers.parse_graph(styled_character_list)
        bounds_parsed = input_parsers.parse_graph(bounds)
        result = _internal.styled_string_from_characters_fixed_internal(styled_character_list_parsed, bounds_parsed)
        return StyledString(result)

    @staticmethod
    def styled_string_from_characters_free(styled_character_list, origin) -> StyledString:
        """Styled String from Characters (Free)

        Returns a styled string from a list of styled characters that is not wrapped and starts at the origin

        Args:
            styled_character_list: Graph of StyledCharacterList
            origin: Graph of Point2f

        Returns:
            Graph: A graph node producing a StyledString.
        """
        styled_character_list_parsed = input_parsers.parse_graph(styled_character_list)
        origin_parsed = input_parsers.parse_graph(origin)
        result = _internal.styled_string_from_characters_free_internal(styled_character_list_parsed, origin_parsed)
        return StyledString(result)

    @staticmethod
    def styled_string_from_characters_max_width(styled_character_list, origin, max_width) -> StyledString:
        """Styled String from Characters (Max Width)

        Returns a styled string from a list of styled characters that wraps at a maximum width and starts at the origin

        Args:
            styled_character_list: Graph of StyledCharacterList
            origin: Graph of Point2f
            max_width: Graph of Float

        Returns:
            Graph: A graph node producing a StyledString.
        """
        styled_character_list_parsed = input_parsers.parse_graph(styled_character_list)
        origin_parsed = input_parsers.parse_graph(origin)
        max_width_parsed = input_parsers.parse_float_graph(max_width)
        result = _internal.styled_string_from_characters_max_width_internal(styled_character_list_parsed, origin_parsed, max_width_parsed)
        return StyledString(result)

    def styled_string_to_characters(self) -> styled_character_list.StyledCharacterList:
        """Styled String to Characters

        Returns a list of styled characters for a styled string

        Returns:
            Graph: A graph node producing a StyledCharacterList.
        """
        styled_string_parsed = input_parsers.parse_graph(self)
        result = _internal.styled_string_to_characters_internal(styled_string_parsed)
        from .styled_character_list import StyledCharacterList
        return StyledCharacterList(result)
