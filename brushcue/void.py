# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 86650ab5251543b2e528175bbf8d832b0be86208f57acf761168e6e5b29b34cc
# generated from templates/py_type.jinja

from __future__ import annotations

from .object import Object


class Void(Object):
    """The absence of a value"""

    def execute(self, context):
        return self._inner.execute(context)
