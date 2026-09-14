# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: f2b7564f8cea920dba48c018fdbea21202568572c2a21c615482fdbaa19e3937
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class StringList(List):
    """List of Strings"""

    def __init__(self, inner, resolved_type=None):
        from .string import String
        super().__init__(inner, String if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context)
