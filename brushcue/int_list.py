# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 7cd9c01645e509e677f356a5099277f40a8ed06a31c21636f96d1328b0144478
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class IntList(List):
    """List of Ints"""

    def __init__(self, inner, resolved_type=None):
        from .int import Int
        super().__init__(inner, Int if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context).as_int_list()
