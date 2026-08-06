# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 80c64111f77793ccde0b6dc96ede6cc80e19659e2c04a96eeef256a3f9ac6e59
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class Any(_GraphWrapper):
    """Representing any type in the graph"""

    def execute(self, context):

        return self._inner.execute(context)


