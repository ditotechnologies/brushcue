# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 0c4ae67c716a303b1d176b00a1674d18a96feaff877730a860a6ed078e200b60
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class Bounds2fList(List):
    """List of Bounds 2D Floats"""

    def __init__(self, inner, resolved_type=None):
        from .bounds2f import Bounds2f
        super().__init__(inner, Bounds2f if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
