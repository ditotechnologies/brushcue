# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: d36b841d4cf9b7b090564ef50d0e7520def68cacde055513ac6a9ecd0dd08070
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class StyledCharacter(Object):
    """a character with style"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def new(character, font, size, render_style) -> StyledCharacter:
        """Styled Character New

        Creates a new styled character

        Args:
            character: Graph of Character
            font: Graph of Font
            size: Graph of Float
            render_style: Graph of RenderStyle

        Returns:
            Graph: A graph node producing a StyledCharacter.
        """
        character_parsed = input_parsers.parse_graph(character)
        font_parsed = input_parsers.parse_graph(font)
        size_parsed = input_parsers.parse_float_graph(size)
        render_style_parsed = input_parsers.parse_graph(render_style)
        result = _internal.styled_character_new_internal(character_parsed, font_parsed, size_parsed, render_style_parsed)
        return StyledCharacter(result)
