# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: be5317e0639c7ec7a6493ae8056afec8bd73c8820fbf70744b8ad478fc3f03f9
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import byte_list



class Image(_GraphWrapper):
    """An Image"""

    def execute(self, context):

        return self._inner.execute(context)


    @staticmethod
    def from_byte_list(bytes) -> Image:
        """Image from Bytes

        Given some bytes, parses an image
    
        Args:
            bytes: Graph of ByteList
            
    
        Returns:
            Graph: A graph node producing a Image.
        """
        bytes_parsed = input_parsers.parse_graph(bytes)
        result = _internal.image_from_byte_list_internal(bytes_parsed)

        return Image(result)

    def to_byte_list(self) -> byte_list.ByteList:
        """Image to Byte List

        Given an image, converts it to a byte list
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        image_parsed = input_parsers.parse_graph(self)
        result = _internal.image_to_byte_list_internal(image_parsed)

        from .byte_list import ByteList
        return ByteList(result)

