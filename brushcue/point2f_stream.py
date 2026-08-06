# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 273ad81d0bbc21879ade4b236a42b4f38192b52b79ecec4a45a75fcc58ff21de
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import any_stream



class Point2fStream(_GraphWrapper):
    """Stream of Point 2 Floats"""

    def execute(self, context):

        return self._inner.execute(context)


    def filter(self, start, end) -> Point2fStream:
        """Point 2 Float Stream Filter

        Filters Point 2 Float Stream stream
    
        Args:
            start: Graph of Point2f
            end: Graph of Bool
            
    
        Returns:
            Graph: A graph node producing a Point2fStream.
        """
        stream_parsed = input_parsers.parse_graph(self)
        start_parsed = input_parsers.parse_graph(start)
        end_parsed = input_parsers.parse_bool_graph(end)
        result = _internal.point2f_stream_filter_internal(stream_parsed, start_parsed, end_parsed)

        return Point2fStream(result)

    def map(self, input_location, output_location) -> any_stream.AnyStream:
        """Point2fStream Map

        Point2fStream Maps Each Value of the Stream
    
        Args:
            input_location: Graph of Point2f
            output_location: Graph of Any
            
    
        Returns:
            Graph: A graph node producing a AnyStream.
        """
        stream_parsed = input_parsers.parse_graph(self)
        input_location_parsed = input_parsers.parse_graph(input_location)
        output_location_parsed = input_parsers.parse_graph(output_location)
        result = _internal.point2f_stream_map_internal(stream_parsed, input_location_parsed, output_location_parsed)

        from .any_stream import AnyStream
        return AnyStream(result)

