# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 5101e0498bb22ce06d04f2981323381570e30862562030e30981d632536c0f35
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import bytes


class Image(Object):
    """An Image"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def from_bytes(bytes) -> Image:
        """Image from Bytes

        Given some bytes, parses an image

        Args:
            bytes: Graph of Bytes

        Returns:
            Graph: A graph node producing a Image.
        """
        bytes_parsed = input_parsers.parse_graph(bytes)
        result = _internal.image_from_bytes_internal(bytes_parsed)
        return Image(result)

    def to_bytes(self) -> bytes.Bytes:
        """Image to Bytes

        Given an image, converts it to bytes

        Returns:
            Graph: A graph node producing a Bytes.
        """
        image_parsed = input_parsers.parse_graph(self)
        result = _internal.image_to_bytes_internal(image_parsed)
        from .bytes import Bytes
        return Bytes(result)
