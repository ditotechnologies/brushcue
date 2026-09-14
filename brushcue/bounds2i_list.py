# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: f5e2f528c1049be15950a1183a7572e6267ccfd1bdc7ee3c7fd617b6327b35d9
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class Bounds2iList(List):
    """List of Bounds 2D Ints"""

    def __init__(self, inner, resolved_type=None):
        from .bounds2i import Bounds2i
        super().__init__(inner, Bounds2i if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
