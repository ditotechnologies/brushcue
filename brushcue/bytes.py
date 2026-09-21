# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: a7da429ad62048fc064ff9bc1878d3b2d07d812e01a4a04cb79472830d20d626
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import string
    from . import void


class Bytes(Object):
    """A list of bytes"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def from_url(url) -> Bytes:
        """Bytes from URL

        Given a URL. Performs a GET request and downloads the result as bytes.

        Args:
            url: Graph of String

        Returns:
            Graph: A graph node producing a Bytes.
        """
        url_parsed = input_parsers.parse_string_graph(url)
        result = _internal.bytes_from_u_r_l_internal(url_parsed)
        return Bytes(result)

    def save_to_path(self, path) -> string.String:
        """Bytes Save to Path

        Writes a byte list to a specified file path on disk. Returns the path that was written to.

        Args:
            path: Graph of String

        Returns:
            Graph: A graph node producing a String.
        """
        bytes_parsed = input_parsers.parse_graph(self)
        path_parsed = input_parsers.parse_string_graph(path)
        result = _internal.bytes_save_to_path_internal(bytes_parsed, path_parsed)
        from .string import String
        return String(result)

    def file_convert_image_to_bmp(self) -> Bytes:
        """File Convert Image to BMP

        Converts any image format (JPEG, PNG, WebP, TIFF, HEIC, etc.) to BMP. Returns BMP bytes.

        Returns:
            Graph: A graph node producing a Bytes.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_image_to_bmp_internal(image_bytes_parsed)
        return Bytes(result)

    def file_convert_image_to_heic(self, quality) -> Bytes:
        """File Convert Image to HEIC

        Converts any image format (JPEG, PNG, WebP, TIFF, BMP, etc.) to HEIC. Returns HEIC bytes.

        Args:
            quality: Graph of Int

        Returns:
            Graph: A graph node producing a Bytes.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        quality_parsed = input_parsers.parse_int_graph(quality)
        result = _internal.file_convert_image_to_heic_internal(image_bytes_parsed, quality_parsed)
        return Bytes(result)

    def file_convert_image_to_jpeg(self, quality) -> Bytes:
        """File Convert Image to JPEG

        Converts any image format (PNG, WebP, TIFF, BMP, HEIC, etc.) to JPEG. Returns JPEG bytes.

        Args:
            quality: Graph of Int

        Returns:
            Graph: A graph node producing a Bytes.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        quality_parsed = input_parsers.parse_int_graph(quality)
        result = _internal.file_convert_image_to_jpeg_internal(image_bytes_parsed, quality_parsed)
        return Bytes(result)

    def file_convert_image_to_png(self) -> Bytes:
        """File Convert Image to PNG

        Converts any image format (JPEG, WebP, TIFF, BMP, HEIC, etc.) to PNG. Returns PNG bytes.

        Returns:
            Graph: A graph node producing a Bytes.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_image_to_png_internal(image_bytes_parsed)
        return Bytes(result)

    def file_convert_image_to_tiff(self) -> Bytes:
        """File Convert Image to TIFF

        Converts any image format (JPEG, PNG, WebP, BMP, HEIC, etc.) to TIFF. Returns TIFF bytes.

        Returns:
            Graph: A graph node producing a Bytes.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_image_to_tiff_internal(image_bytes_parsed)
        return Bytes(result)

    def file_convert_image_to_web_p(self, quality) -> Bytes:
        """File Convert Image to WebP

        Converts any image format (JPEG, PNG, TIFF, BMP, HEIC, etc.) to WebP. Returns WebP bytes.

        Args:
            quality: Graph of Int

        Returns:
            Graph: A graph node producing a Bytes.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        quality_parsed = input_parsers.parse_int_graph(quality)
        result = _internal.file_convert_image_to_web_p_internal(image_bytes_parsed, quality_parsed)
        return Bytes(result)

    def file_convert_video_to_gif(self, frame_rate) -> Bytes:
        """File Convert Video to GIF

        Converts any video format (MP4, MOV, WebM, AVI, MKV) to a GIF. Returns GIF bytes.

        Args:
            frame_rate: Graph of Int

        Returns:
            Graph: A graph node producing a Bytes.
        """
        video_bytes_parsed = input_parsers.parse_graph(self)
        frame_rate_parsed = input_parsers.parse_int_graph(frame_rate)
        result = _internal.file_convert_video_to_gif_internal(video_bytes_parsed, frame_rate_parsed)
        return Bytes(result)

    def file_convert_video_to_mp4(self) -> Bytes:
        """File Convert Video to MP4

        Converts any video format (MOV, WebM, AVI, MKV) to MP4. Returns MP4 bytes.

        Returns:
            Graph: A graph node producing a Bytes.
        """
        video_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_video_to_m_p4_internal(video_bytes_parsed)
        return Bytes(result)

    def file_convert_video_to_web_m(self) -> Bytes:
        """File Convert Video to WebM

        Converts any video format (MP4, MOV, AVI, MKV) to WebM. Returns WebM bytes.

        Returns:
            Graph: A graph node producing a Bytes.
        """
        video_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_video_to_web_m_internal(video_bytes_parsed)
        return Bytes(result)

    def upload_bytes(self, url, content_type) -> void.Void:
        """Upload Bytes

        Given bytes and a URL. Performs a PUT request and uploads the bytes

        Args:
            url: Graph of String
            content_type: Graph of String

        Returns:
            Graph: A graph node producing a Void.
        """
        bytes_parsed = input_parsers.parse_graph(self)
        url_parsed = input_parsers.parse_string_graph(url)
        content_type_parsed = input_parsers.parse_string_graph(content_type)
        result = _internal.upload_bytes_internal(bytes_parsed, url_parsed, content_type_parsed)
        from .void import Void
        return Void(result)
