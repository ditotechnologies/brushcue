# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: b7e838a6d723a8484d4f14b9e5a51b6a3642836682038c951027deeba918a7d5
# generated from templates/py_type.jinja

from __future__ import annotations

from .object import Object


class String(Object):
    """a string"""

    def execute(self, context):
        return self._inner.execute(context).as_string()
