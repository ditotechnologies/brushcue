# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: ebcefe7b135fb0bbd8a7f964c720e2462a3c7f49bac67a8a37694275391f3588
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class Transform2List(List):
    """List of Transform 2Ds"""

    def __init__(self, inner, resolved_type=None):
        from .transform2 import Transform2
        super().__init__(inner, Transform2 if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
