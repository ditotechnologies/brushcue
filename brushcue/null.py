# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 247c4d43f8034972ad8ec898a164835c684b390b72d52a72cc5d1db886bf718b
# generated from templates/py_type.jinja

from __future__ import annotations

from .object import Object


class Null(Object):
    """An unconnected input"""

    def execute(self, context):
        return self._inner.execute(context)
