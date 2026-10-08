# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: d55fb8df2ecc9f502cb97ec4289d42dd88053b61e987bd995fd8bf40cf6ca55a
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import character
    from . import character_list


class String(Object):
    """a string"""

    def execute(self, context):
        return self._inner.execute(context).as_string()

    def to_character(self) -> character.Character:
        """String to Character

        Converts a string containing exactly one character to a character.

        Returns:
            Graph: A graph node producing a Character.
        """
        string_parsed = input_parsers.parse_string_graph(self)
        result = _internal.string_to_character_internal(string_parsed)
        from .character import Character
        return Character(result)

    def to_character_list(self) -> character_list.CharacterList:
        """String to Character List

        Splits a string into a list of its characters.

        Returns:
            Graph: A graph node producing a CharacterList.
        """
        string_parsed = input_parsers.parse_string_graph(self)
        result = _internal.string_to_character_list_internal(string_parsed)
        from .character_list import CharacterList
        return CharacterList(result)
