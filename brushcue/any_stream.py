# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 7715307bbdbb651d71a7c0e094cf4a27e64849a927434ab06bf59f45c61ed6b7
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class AnyStream(_GraphWrapper):
    """Stream of Anys"""

    def execute(self, context):

        return self._inner.execute(context)


