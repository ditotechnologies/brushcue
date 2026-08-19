# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 2bc56034810e874508bcaa350ef75b670eca4e04c86d9dce8a67a5df761d67eb
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class OkLabA(_GraphWrapper):
    """An OkLab color with an alpha component."""

    def execute(self, context):

        return self._inner.execute(context).as_ok_lab_a()


