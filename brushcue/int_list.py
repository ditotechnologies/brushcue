# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: c8b15a75feefe4ed6f4d8500c4795ae46b2a2ac02047dba8e21a0e2a46cf8a37
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import int



class IntList(_GraphWrapper):
    """List of Ints"""

    def execute(self, context):

        return self._inner.execute(context).as_int_list()


    def first(self) -> int.Int:
        """Int List First

        First Item of Int List
    
        Returns:
            Graph: A graph node producing a Int.
        """
        list_parsed = input_parsers.parse_graph(self)
        result = _internal.int_list_first_internal(list_parsed)

        from .int import Int
        return Int(result)

