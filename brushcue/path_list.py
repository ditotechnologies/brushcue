# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 841de280a181bc432d9db1d0fdacc073a728d6c53debaf961b165330f3e64406
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class PathList(List):
    """List of Paths"""

    def __init__(self, inner, resolved_type=None):
        from .path import Path
        super().__init__(inner, Path if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
