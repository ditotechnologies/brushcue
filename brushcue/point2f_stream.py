# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 012a182f0900cf024e6a23c5445f57592f18ca7886a5da35d20d2652adab6640
# generated from templates/py_type.jinja

from __future__ import annotations

from .stream import Stream


class Point2fStream(Stream):
    """Stream of Point 2 Floats"""

    def execute(self, context):
        return self._inner.execute(context)
