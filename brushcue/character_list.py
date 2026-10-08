# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 9c74d7c996595195e7a1ffaa291543081682d29241b06a67c49840e9adbeb76d
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class CharacterList(List):
    """List of Characters"""

    def __init__(self, inner, resolved_type=None):
        from .character import Character
        super().__init__(inner, Character if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
