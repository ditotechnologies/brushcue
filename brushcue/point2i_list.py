# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: b30436ecde335078af5f449ebe6782f63447de4828e38969e6cd44a9a4e3ce99
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class Point2iList(List):
    """List of Point 2 Ints"""

    def __init__(self, inner, resolved_type=None):
        from .point2i import Point2i
        super().__init__(inner, Point2i if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
