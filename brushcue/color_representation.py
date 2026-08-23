# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 5ede1db42cfcabc08a2b7458c1a1b35b03f9932f93916e66a27564684ecfbd1c
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import color_profile



class ColorRepresentation(_GraphWrapper):
    """A color-format profile paired with a pixel encoding, describing how to interpret raw pixel values."""

    def execute(self, context):

        return self._inner.execute(context)


    @staticmethod
    def aces_cg() -> ColorRepresentation:
        """Color Representation ACEScg

        Creates a Color Representation using the ACEScg Color Profile with linear light, straight alpha pixel values.
    
        Returns:
            Graph: A graph node producing a ColorRepresentation.
        """
        result = _internal.color_representation_a_c_e_scg_internal()

        return ColorRepresentation(result)

    @staticmethod
    def from_color_profile_and_pixel_encoding(color_profile, pixel_encoding) -> ColorRepresentation:
        """Color Representation From Color Profile And Pixel Encoding

        Creates a Color Representation by pairing a Color Profile with a Pixel Encoding.
    
        Args:
            color_profile: Graph of ColorProfile
            pixel_encoding: Graph of PixelEncoding
            
    
        Returns:
            Graph: A graph node producing a ColorRepresentation.
        """
        color_profile_parsed = input_parsers.parse_graph(color_profile)
        pixel_encoding_parsed = input_parsers.parse_graph(pixel_encoding)
        result = _internal.color_representation_from_color_profile_and_pixel_encoding_internal(color_profile_parsed, pixel_encoding_parsed)

        return ColorRepresentation(result)

    @staticmethod
    def oklab_a() -> ColorRepresentation:
        """Color Representation OkLabA

        Creates a Color Representation using the OkLabA Color Profile with encoded pixel values.
    
        Returns:
            Graph: A graph node producing a ColorRepresentation.
        """
        result = _internal.color_representation_ok_lab_a_internal()

        return ColorRepresentation(result)

    def profile(self) -> color_profile.ColorProfile:
        """Color Profile of a Color Representation

        Given a color-format representation. Extracts the color-format profile of that color-format representation
    
        Returns:
            Graph: A graph node producing a ColorProfile.
        """
        color_representation_parsed = input_parsers.parse_graph(self)
        result = _internal.color_representation_profile_internal(color_representation_parsed)

        from .color_profile import ColorProfile
        return ColorProfile(result)

    @staticmethod
    def rgb_bt2020() -> ColorRepresentation:
        """Color Representation BT.2020

        Creates a Color Representation using the BT.2020 Color Profile with gamma-encoded pixel values.
    
        Returns:
            Graph: A graph node producing a ColorRepresentation.
        """
        result = _internal.color_representation_r_g_b_b_t2020_internal()

        return ColorRepresentation(result)

    @staticmethod
    def srgb() -> ColorRepresentation:
        """Color Representation sRGB

        Creates a Color Representation using the sRGB Color Profile with gamma-encoded pixel values.
    
        Returns:
            Graph: A graph node producing a ColorRepresentation.
        """
        result = _internal.color_representation_s_r_g_b_internal()

        return ColorRepresentation(result)

    @staticmethod
    def xyza() -> ColorRepresentation:
        """Color Representation XYZA

        Creates a Color Representation using the XYZA Color Profile with linear light, straight alpha pixel values.
    
        Returns:
            Graph: A graph node producing a ColorRepresentation.
        """
        result = _internal.color_representation_x_y_z_a_internal()

        return ColorRepresentation(result)

