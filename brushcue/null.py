# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: be75f93921a50c8ffe457832ef886367117c06df2b12c601efcf7ae67008d1be
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class Null(_GraphWrapper):
    """An unconnected input"""

    def execute(self, context):

        return self._inner.execute(context)


