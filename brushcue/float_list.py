# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: f023b8bcb746f6359523a27feb1397caf118476beb447c81940a98b3d4b7653e
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class FloatList(_GraphWrapper):
    """List of Floats"""

    def execute(self, context):

        return self._inner.execute(context).as_float_list()


