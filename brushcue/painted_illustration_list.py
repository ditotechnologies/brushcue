# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: eb53e404f10b8cbca1dab4bbe46386091735153b2855f0dafd630034993ee62f
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class PaintedIllustrationList(List):
    """List of Painted Illustrations"""

    def __init__(self, inner, resolved_type=None):
        from .painted_illustration import PaintedIllustration
        super().__init__(inner, PaintedIllustration if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
