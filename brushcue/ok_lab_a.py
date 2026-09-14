# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 78d99d51f37cfd1d816a8cb061078f613aa145c6476f9051ccb2494ecdc3673e
# generated from templates/py_type.jinja

from __future__ import annotations

from .object import Object


class OkLabA(Object):
    """An OkLab color-format with an alpha component."""

    def execute(self, context):
        return self._inner.execute(context).as_ok_lab_a()
