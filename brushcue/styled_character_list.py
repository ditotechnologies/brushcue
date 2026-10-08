# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: bac177df508bcb09dfe15c6a885f286f896d8adae30bd9c6182f6098cec7b431
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class StyledCharacterList(List):
    """List of Styled Characters"""

    def __init__(self, inner, resolved_type=None):
        from .styled_character import StyledCharacter
        super().__init__(inner, StyledCharacter if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
