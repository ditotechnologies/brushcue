# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: d3eaf16a4c1b21c3264926cb4a106c1629a01b8b1b939c484e58dcfa6a2681e5
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class PixelEncoding(_GraphWrapper):
    """How pixel values are encoded (gamma/other encoded, linear straight alpha, or linear premultiplied alpha)."""

    def execute(self, context):

        return self._inner.execute(context)


    @staticmethod
    def encoded() -> PixelEncoding:
        """Pixel Encoding Encoded

        Creates a Pixel Encoding representing gamma or other non-linear encoded values.
    
        Returns:
            Graph: A graph node producing a PixelEncoding.
        """
        result = _internal.pixel_encoding_encoded_internal()

        return PixelEncoding(result)

    @staticmethod
    def linear() -> PixelEncoding:
        """Pixel Encoding Linear

        Creates a Pixel Encoding representing linear light, straight alpha values.
    
        Returns:
            Graph: A graph node producing a PixelEncoding.
        """
        result = _internal.pixel_encoding_linear_internal()

        return PixelEncoding(result)

    @staticmethod
    def premultiplied_alpha() -> PixelEncoding:
        """Pixel Encoding Premultiplied Alpha

        Creates a Pixel Encoding representing linear light, premultiplied alpha values.
    
        Returns:
            Graph: A graph node producing a PixelEncoding.
        """
        result = _internal.pixel_encoding_premultiplied_alpha_internal()

        return PixelEncoding(result)

