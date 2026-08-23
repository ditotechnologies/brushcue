# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 3c969a0a41917c9fc05254243cead9aab330b057ce3aa3edd1be197f4c80b6e6
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class ColorProfile(_GraphWrapper):
    """A Color Profile"""

    def execute(self, context):

        return self._inner.execute(context)


    @staticmethod
    def aces_cg() -> ColorProfile:
        """Color Profile ACEScg

        Creates an ACEScg Color Profile
    
        Returns:
            Graph: A graph node producing a ColorProfile.
        """
        result = _internal.color_profile_a_c_e_scg_internal()

        return ColorProfile(result)

    @staticmethod
    def bt709() -> ColorProfile:
        """Color Profile BT.709

        Creates a BT.709 Color Profile
    
        Returns:
            Graph: A graph node producing a ColorProfile.
        """
        result = _internal.color_profile_b_t709_internal()

        return ColorProfile(result)

    @staticmethod
    def ok_lab_a() -> ColorProfile:
        """Color Profile OkLabA

        Creates an OkLabA color-format profile. OkLab with also an alpha component.
    
        Returns:
            Graph: A graph node producing a ColorProfile.
        """
        result = _internal.color_profile_ok_lab_a_internal()

        return ColorProfile(result)

    @staticmethod
    def p3() -> ColorProfile:
        """Color Profile P3

        Creates a P3 Color Profile
    
        Returns:
            Graph: A graph node producing a ColorProfile.
        """
        result = _internal.color_profile_p3_internal()

        return ColorProfile(result)

    @staticmethod
    def png_srgb() -> ColorProfile:
        """Color Profile PNG sRGB

        Creates a color-format profile that is the same one as PNG sRGB.
    
        Returns:
            Graph: A graph node producing a ColorProfile.
        """
        result = _internal.color_profile_p_n_g_s_r_g_b_internal()

        return ColorProfile(result)

    @staticmethod
    def srgb() -> ColorProfile:
        """Color Profile sRGB

        Creates an sRGB Color Profile
    
        Returns:
            Graph: A graph node producing a ColorProfile.
        """
        result = _internal.color_profile_s_r_g_b_internal()

        return ColorProfile(result)

    @staticmethod
    def xyz() -> ColorProfile:
        """Color Profile XYZ

        Creates an XYZ Color Profile
    
        Returns:
            Graph: A graph node producing a ColorProfile.
        """
        result = _internal.color_profile_x_y_z_internal()

        return ColorProfile(result)

