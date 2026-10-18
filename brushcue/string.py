# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 27e389156a319668abd23427d276c79a3b41bb53d198522681fcb5d6a9fd8a5f
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import character
    from . import character_list
    from . import path


class String(Object):
    """a string"""

    def execute(self, context):
        return self._inner.execute(context).as_string()

    def from_stylus(self, smooth_factor) -> path.Path:
        """Path From Stylus

        Creates a path from a stylus capture.

        Args:
            smooth_factor: Graph of Float

        Returns:
            Graph: A graph node producing a Path.
        """
        path_parsed = input_parsers.parse_string_graph(self)
        smooth_factor_parsed = input_parsers.parse_float_graph(smooth_factor)
        result = _internal.path_from_stylus_internal(path_parsed, smooth_factor_parsed)
        from .path import Path
        return Path(result)

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
