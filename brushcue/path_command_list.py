# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: fa6d1fc204b2d8de53e5537e18110ca75ac746fcd19e0600d935f89077996a38
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class PathCommandList(List):
    """List of Path Commands"""

    def __init__(self, inner, resolved_type=None):
        from .path_command import PathCommand
        super().__init__(inner, PathCommand if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
