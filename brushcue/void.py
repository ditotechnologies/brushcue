# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 927aee3be54605af804315c9e0e855ed3d1185c657d9dd38fa02af7de8c89101
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class Void(_GraphWrapper):
    """The absence of a value"""

    def execute(self, context):

        return self._inner.execute(context)


