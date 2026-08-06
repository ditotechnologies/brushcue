# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: a9d092386366a1bd4e439d9f8a7aa85a7279e4b04826de24ff43dc7be3590dc5
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import void



class ByteList(_GraphWrapper):
    """List of Bytes"""

    def execute(self, context):

        return self._inner.execute(context)


    @staticmethod
    def from_url(url) -> ByteList:
        """Byte List from URL

        Given a URL. Performs a GET request and downloads the result as bytes.
    
        Args:
            url: Graph of String
            
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        url_parsed = input_parsers.parse_string_graph(url)
        result = _internal.byte_list_from_u_r_l_internal(url_parsed)

        return ByteList(result)

    def file_convert_image_to_bmp(self) -> ByteList:
        """File Convert Image to BMP

        Converts any image format (JPEG, PNG, WebP, TIFF, HEIC, etc.) to BMP. Returns BMP bytes.
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_image_to_bmp_internal(image_bytes_parsed)

        return ByteList(result)

    def file_convert_image_to_heic(self, quality) -> ByteList:
        """File Convert Image to HEIC

        Converts any image format (JPEG, PNG, WebP, TIFF, BMP, etc.) to HEIC. Returns HEIC bytes.
    
        Args:
            quality: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        quality_parsed = input_parsers.parse_int_graph(quality)
        result = _internal.file_convert_image_to_heic_internal(image_bytes_parsed, quality_parsed)

        return ByteList(result)

    def file_convert_image_to_jpeg(self, quality) -> ByteList:
        """File Convert Image to JPEG

        Converts any image format (PNG, WebP, TIFF, BMP, HEIC, etc.) to JPEG. Returns JPEG bytes.
    
        Args:
            quality: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        quality_parsed = input_parsers.parse_int_graph(quality)
        result = _internal.file_convert_image_to_jpeg_internal(image_bytes_parsed, quality_parsed)

        return ByteList(result)

    def file_convert_image_to_png(self) -> ByteList:
        """File Convert Image to PNG

        Converts any image format (JPEG, WebP, TIFF, BMP, HEIC, etc.) to PNG. Returns PNG bytes.
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_image_to_png_internal(image_bytes_parsed)

        return ByteList(result)

    def file_convert_image_to_tiff(self) -> ByteList:
        """File Convert Image to TIFF

        Converts any image format (JPEG, PNG, WebP, BMP, HEIC, etc.) to TIFF. Returns TIFF bytes.
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_image_to_tiff_internal(image_bytes_parsed)

        return ByteList(result)

    def file_convert_image_to_web_p(self, quality) -> ByteList:
        """File Convert Image to WebP

        Converts any image format (JPEG, PNG, TIFF, BMP, HEIC, etc.) to WebP. Returns WebP bytes.
    
        Args:
            quality: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        image_bytes_parsed = input_parsers.parse_graph(self)
        quality_parsed = input_parsers.parse_int_graph(quality)
        result = _internal.file_convert_image_to_web_p_internal(image_bytes_parsed, quality_parsed)

        return ByteList(result)

    def file_convert_video_to_animated_web_p(self) -> ByteList:
        """File Convert Video to Animated WebP

        Converts any video format (MP4, MOV, WebM, AVI, MKV) to an animated WebP. Returns animated WebP bytes.
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        video_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_video_to_animated_web_p_internal(video_bytes_parsed)

        return ByteList(result)

    def file_convert_video_to_gif(self, frame_rate) -> ByteList:
        """File Convert Video to GIF

        Converts any video format (MP4, MOV, WebM, AVI, MKV) to a GIF. Returns GIF bytes.
    
        Args:
            frame_rate: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        video_bytes_parsed = input_parsers.parse_graph(self)
        frame_rate_parsed = input_parsers.parse_int_graph(frame_rate)
        result = _internal.file_convert_video_to_gif_internal(video_bytes_parsed, frame_rate_parsed)

        return ByteList(result)

    def file_convert_video_to_mp4(self) -> ByteList:
        """File Convert Video to MP4

        Converts any video format (MOV, WebM, AVI, MKV) to MP4. Returns MP4 bytes.
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        video_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_video_to_m_p4_internal(video_bytes_parsed)

        return ByteList(result)

    def file_convert_video_to_web_m(self) -> ByteList:
        """File Convert Video to WebM

        Converts any video format (MP4, MOV, AVI, MKV) to WebM. Returns WebM bytes.
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        video_bytes_parsed = input_parsers.parse_graph(self)
        result = _internal.file_convert_video_to_web_m_internal(video_bytes_parsed)

        return ByteList(result)

    def upload_byte_list(self, url, content_type) -> void.Void:
        """Upload Byte List

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
        result = _internal.upload_byte_list_internal(bytes_parsed, url_parsed, content_type_parsed)

        from .void import Void
        return Void(result)

