# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 54f69da2079bad7d4038c8c6957703742284de303468c8e07890cb8ee86c2a0a
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import point2f

    from . import point2f_stream



class Point2fList(_GraphWrapper):
    """List of Point 2 Floats"""

    def execute(self, context):

        return self._inner.execute(context)


    def first(self) -> point2f.Point2f:
        """Point 2 Float List First

        First Item of Point 2 Float List
    
        Returns:
            Graph: A graph node producing a Point2f.
        """
        list_parsed = input_parsers.parse_graph(self)
        result = _internal.point2f_list_first_internal(list_parsed)

        from .point2f import Point2f
        return Point2f(result)

    def to_stream(self) -> point2f_stream.Point2fStream:
        """Point 2 Float List to Stream

        Converts Point 2 Float list to a stream
    
        Returns:
            Graph: A graph node producing a Point2fStream.
        """
        list_parsed = input_parsers.parse_graph(self)
        result = _internal.point2f_list_to_stream_internal(list_parsed)

        from .point2f_stream import Point2fStream
        return Point2fStream(result)

