# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: b32c3a2eb2fc5e2b1306610a060d9a8d9831dbb3edc9a49486ceef47a857b880
# generated from templates/py_brushcue_init.jinja

from __future__ import annotations

"""Typed Python bindings for BrushCue graph construction."""

from . import _py as _internal
from ._graph import Project
from ._py import (
    Bounds,
    Context,
    ImageRecipe,
    MovieRecipe,
    TypeDefinition,
)
from . import input_parsers

def float_list_empty() -> FloatList:
    result = _internal.float_list_empty_internal()
    from .float_list import FloatList
    return FloatList(result)


def int_list_empty() -> IntList:
    result = _internal.int_list_empty_internal()
    from .int_list import IntList
    return IntList(result)


def null_value() -> Null:
    result = _internal.null_value_internal()
    from .null import Null
    return Null(result)


def point2f_list_empty() -> Point2fList:
    result = _internal.point2f_list_empty_internal()
    from .point2f_list import Point2fList
    return Point2fList(result)


def point2i_list_empty() -> Point2iList:
    result = _internal.point2i_list_empty_internal()
    from .point2i_list import Point2iList
    return Point2iList(result)


def string_list_empty() -> StringList:
    result = _internal.string_list_empty_internal()
    from .string_list import StringList
    return StringList(result)


from .bool import Bool

from .bounds2f import Bounds2f

from .bounds2i import Bounds2i

from .bounds2i_list import Bounds2iList

from .brush import Brush

from .bytes import Bytes

from .color_profile import ColorProfile

from .color_representation import ColorRepresentation

from .composition import Composition

from .curve import Curve

from .dictionary import Dictionary

from .fill import Fill

from .float import Float

from .float_list import FloatList

from .image import Image

from .int import Int

from .int_list import IntList

from .l_m_s_a import LMSA

from .null import Null

from .ok_lab_a import OkLabA

from .ok_lab_color import OkLabColor

from .ok_lab_hist import OkLabHist

from .painter import Painter

from .path import Path

from .pixel_encoding import PixelEncoding

from .point2f import Point2f

from .point2f_list import Point2fList

from .point2i import Point2i

from .point2i_list import Point2iList

from .profiled_color import ProfiledColor

from .profiled_color_list import ProfiledColorList

from .r_g_b_a_color import RGBAColor

from .r_g_b_color import RGBColor

from .render_style import RenderStyle

from .sequence import Sequence

from .string import String

from .string_list import StringList

from .transform2 import Transform2

from .transform2_list import Transform2List

from .vector2f import Vector2f

from .vector2i import Vector2i

from .vector3f import Vector3f

from .void import Void

from .x_y_z import XYZ

from .x_y_z_a import XYZA

from .any_graph import AnyGraph

from .stream import Stream

from .list import List

from .object import Object


from ._operators import setup_operators

setup_operators()

__all__ = [
    "Context", "Project", "ImageRecipe", "MovieRecipe", "Bounds", "TypeDefinition",

    "float_list_empty",

    "int_list_empty",

    "null_value",

    "point2f_list_empty",

    "point2i_list_empty",

    "string_list_empty",


    "Bool",

    "Bounds2f",

    "Bounds2i",

    "Bounds2iList",

    "Brush",

    "Bytes",

    "ColorProfile",

    "ColorRepresentation",

    "Composition",

    "Curve",

    "Dictionary",

    "Fill",

    "Float",

    "FloatList",

    "Image",

    "Int",

    "IntList",

    "LMSA",

    "Null",

    "OkLabA",

    "OkLabColor",

    "OkLabHist",

    "Painter",

    "Path",

    "PixelEncoding",

    "Point2f",

    "Point2fList",

    "Point2i",

    "Point2iList",

    "ProfiledColor",

    "ProfiledColorList",

    "RGBAColor",

    "RGBColor",

    "RenderStyle",

    "Sequence",

    "String",

    "StringList",

    "Transform2",

    "Transform2List",

    "Vector2f",

    "Vector2i",

    "Vector3f",

    "Void",

    "XYZ",

    "XYZA",

    "AnyGraph",

    "Stream",

    "List",

    "Object",

]
