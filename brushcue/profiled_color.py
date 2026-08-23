# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 3af29ba9cbd1acafd37c9707670b98007ea930f9d66d42a7dc910cf761134820
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import ok_lab_a

    from . import r_g_b_a_color

    from . import x_y_z_a



class ProfiledColor(_GraphWrapper):
    """A color-format with an associated color-format representation."""

    def execute(self, context):

        return self._inner.execute(context)


    @staticmethod
    def blackbody(kelvin) -> ProfiledColor:
        """Profiled Color Blackbody

        Creates a profiled color-format that is the color-format of a blackbody emitter at a given kelvin.

        Args:
            kelvin: Graph of Float


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        kelvin_parsed = input_parsers.parse_float_graph(kelvin)
        result = _internal.profiled_color_blackbody_internal(kelvin_parsed)

        return ProfiledColor(result)

    def brightness_adjust(self, offset) -> ProfiledColor:
        """Profiled Color Brightness Adjust

        Adjusts a profiled color-format's lightness in OkLab.

        Args:
            offset: Graph of Float


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        offset_parsed = input_parsers.parse_float_graph(offset)
        result = _internal.profiled_color_brightness_adjust_internal(profiled_color_parsed, offset_parsed)

        return ProfiledColor(result)

    def chroma_offset(self, offset) -> ProfiledColor:
        """Profiled Color Chroma Offset

        Applies an offset to the a and b chroma components of a profiled color-format in OkLab.

        Args:
            offset: Graph of Vector2f


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        offset_parsed = input_parsers.parse_graph(offset)
        result = _internal.profiled_color_chroma_offset_internal(profiled_color_parsed, offset_parsed)

        return ProfiledColor(result)

    def exposure_adjust(self, steps) -> ProfiledColor:
        """Profiled Color Exposure Adjust

        Updates a profiled color-format's exposure by multiplying linear RGB values by 2^steps.

        Args:
            steps: Graph of Float


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        steps_parsed = input_parsers.parse_float_graph(steps)
        result = _internal.profiled_color_exposure_adjust_internal(profiled_color_parsed, steps_parsed)

        return ProfiledColor(result)

    @staticmethod
    def from_ok_lab_a(ok_lab_a) -> ProfiledColor:
        """Profiled Color from OkLab with Alpha

        Creates a profiled color-format from OkLab channels and alpha.

        Args:
            ok_lab_a: Graph of OkLabA


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        ok_lab_a_parsed = input_parsers.parse_graph(ok_lab_a)
        result = _internal.profiled_color_from_ok_lab_a_internal(ok_lab_a_parsed)

        return ProfiledColor(result)

    @staticmethod
    def from_rgba_aces_cg(rgba) -> ProfiledColor:
        """Profiled Color from RGBA ACEScg

        Creates a profiled color-format from linear ACEScg RGBA channels.

        Args:
            rgba: Graph of RGBAColor


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        rgba_parsed = input_parsers.parse_graph(rgba)
        result = _internal.profiled_color_from_rgba_aces_cg_internal(rgba_parsed)

        return ProfiledColor(result)

    @staticmethod
    def from_rgba_srgb(rgba) -> ProfiledColor:
        """Profiled Color from RGBA sRGB

        Creates a profiled color-format from encoded sRGB RGBA channels.

        Args:
            rgba: Graph of RGBAColor


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        rgba_parsed = input_parsers.parse_graph(rgba)
        result = _internal.profiled_color_from_rgba_srgb_internal(rgba_parsed)

        return ProfiledColor(result)

    @staticmethod
    def from_rgba_srgb_linear(rgba) -> ProfiledColor:
        """Profiled Color from RGBA linear sRGB

        Creates a profiled color-format from linear sRGB RGBA channels.

        Args:
            rgba: Graph of RGBAColor


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        rgba_parsed = input_parsers.parse_graph(rgba)
        result = _internal.profiled_color_from_rgba_srgb_linear_internal(rgba_parsed)

        return ProfiledColor(result)

    @staticmethod
    def from_xyz_a(xyza) -> ProfiledColor:
        """Profiled Color from XYZ with Alpha

        Creates a profiled color-format from XYZ channels and alpha.

        Args:
            xyza: Graph of XYZA


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        xyza_parsed = input_parsers.parse_graph(xyza)
        result = _internal.profiled_color_from_xyz_a_internal(xyza_parsed)

        return ProfiledColor(result)

    def grayscale(self) -> ProfiledColor:
        """Profiled Color Grayscale

        Removes chroma from a profiled color-format.

        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        result = _internal.profiled_color_grayscale_internal(profiled_color_parsed)

        return ProfiledColor(result)

    def lightness_curve(self, l_curve) -> ProfiledColor:
        """Profiled Color Lightness Curve

        Applies a curve to the L component of a profiled color-format in OkLab.

        Args:
            l_curve: Graph of Curve


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        l_curve_parsed = input_parsers.parse_graph(l_curve)
        result = _internal.profiled_color_lightness_curve_internal(profiled_color_parsed, l_curve_parsed)

        return ProfiledColor(result)

    def saturation_adjust(self, scale) -> ProfiledColor:
        """Profiled Color Saturation Adjust

        Scales the chroma components of a profiled color-format in OkLab.

        Args:
            scale: Graph of Float


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        scale_parsed = input_parsers.parse_float_graph(scale)
        result = _internal.profiled_color_saturation_adjust_internal(profiled_color_parsed, scale_parsed)

        return ProfiledColor(result)

    def target_white(self, target_white) -> ProfiledColor:
        """Profiled Color Target White

        Adapts a profiled color-format to the specified XYZ white point.

        Args:
            target_white: Graph of XYZ


        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        target_white_parsed = input_parsers.parse_graph(target_white)
        result = _internal.profiled_color_target_white_internal(profiled_color_parsed, target_white_parsed)

        return ProfiledColor(result)

    def to_ok_lab_a(self) -> ok_lab_a.OkLabA:
        """Profiled Color to OkLab with Alpha

        Converts a profiled color-format to OkLab channels with alpha.

        Returns:
            Graph: A graph node producing a OkLabA.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        result = _internal.profiled_color_to_ok_lab_a_internal(profiled_color_parsed)

        from .ok_lab_a import OkLabA
        return OkLabA(result)

    def to_rgb_encoded_with_color_profile(self, color_profile) -> r_g_b_a_color.RGBAColor:
        """Profiled Color to Encoded RGB with Color Profile

        Converts a profiled color-format to encoded RGB channels using the specified RGB color-format profile.

        Args:
            color_profile: Graph of ColorProfile


        Returns:
            Graph: A graph node producing a RGBAColor.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        color_profile_parsed = input_parsers.parse_graph(color_profile)
        result = _internal.profiled_color_to_rgb_encoded_with_color_profile_internal(profiled_color_parsed, color_profile_parsed)

        from .r_g_b_a_color import RGBAColor
        return RGBAColor(result)

    def to_rgb_linear_with_color_profile(self, color_profile) -> r_g_b_a_color.RGBAColor:
        """Profiled Color to Linear RGB with Color Profile

        Converts a profiled color-format to linear RGB channels using the specified RGB color-format profile.

        Args:
            color_profile: Graph of ColorProfile


        Returns:
            Graph: A graph node producing a RGBAColor.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        color_profile_parsed = input_parsers.parse_graph(color_profile)
        result = _internal.profiled_color_to_rgb_linear_with_color_profile_internal(profiled_color_parsed, color_profile_parsed)

        from .r_g_b_a_color import RGBAColor
        return RGBAColor(result)

    def to_xyz_a(self) -> x_y_z_a.XYZA:
        """Profiled Color to XYZ with Alpha

        Converts a profiled color-format to XYZ channels with alpha.

        Returns:
            Graph: A graph node producing a XYZA.
        """
        profiled_color_parsed = input_parsers.parse_graph(self)
        result = _internal.profiled_color_to_xyz_a_internal(profiled_color_parsed)

        from .x_y_z_a import XYZA
        return XYZA(result)
