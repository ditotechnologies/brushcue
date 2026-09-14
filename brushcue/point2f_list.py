# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: ee38f04587993d7bf0a9a1f51fa57f70367fecf65c957b1b066256a4238160de
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class Point2fList(List):
    """List of Point 2 Floats"""

    def __init__(self, inner, resolved_type=None):
        from .point2f import Point2f
        super().__init__(inner, Point2f if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
