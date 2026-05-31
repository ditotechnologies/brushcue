# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 3ca090243436f2df954c3e6ec977e7b2f254c4b16fa5cade6ef908ad2a360131
# generated from templates/py_brushcue_init.jinja

"""
Brushcue — Python bindings for the BrushCue image editing application.

Every function in this module returns a :class:`Graph` node. Nodes are
composable: pass the return value of one function as an argument to another
to build a computation graph.  Nothing is evaluated until you call
:meth:`Graph.execute`.

## Installation

```bash
pip install brushcue
```

## Quickstart

```python
import brushcue

ctx = brushcue.Context()

image = brushcue.load_composition("photo.png")
grayscale = brushcue.composition_grayscale(image)

result = grayscale.execute(ctx)
output_bytes = result.as_composition().to_image_bytes(ctx)

with open("output.png", "wb") as f:
    f.write(bytes(output_bytes))
```

## Core Types

- :class:`Context` — GPU/async execution context. Create one per process.
- :class:`Graph` — A node in the computation graph.
- :class:`Project` — A collection of graphs that can be serialized/deserialized.
- :class:`Type` — The result of executing a graph node.
"""

from ._py import *  # noqa: F401, F403
from .input_parsers import *

def byte_list_constant(value) -> Graph:
    return byte_list_constant_internal(value)

def int_constant(value) -> Graph:
    return int_constant_internal(int(value))

def float_constant(value) -> Graph:
    return float_constant_internal(float(value))

def string_constant(value: str) -> Graph:
    return string_constant_internal(value)

def bool_constant(value: bool) -> Graph:
    return bool_constant_internal(value)

def r_g_b_a_color_constant(r: float, g: float, b: float, a: float):
    return r_g_b_a_color_constant_internal(r, g, b, a)

def r_g_b_color_constant(r: float, g: float, b: float):
    return r_g_b_color_constant_internal(r, g, b)

def vector_2i_constant(x: int, y: int) -> Graph:
    return vector2i_constant_internal(x, y)

def vector2f_constant(x: float, y: float) -> Graph:
    return vector2f_constant_internal(x, y)


def abs(number) -> Graph:
    """Absolute Value

    Returns the absolute value of a float

    Args:
        number: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    number_parsed = parse_float_graph(number)
    return abs_internal(number_parsed)

def and_(bool1, bool2) -> Graph:
    """And

    Returns true if both inputs are true.

    Args:
        the first bool: Graph of Bool
        The second bool: Graph of Bool
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    bool1_parsed = parse_bool_graph(bool1)
    bool2_parsed = parse_bool_graph(bool2)
    return and_internal(bool1_parsed, bool2_parsed)

def bool_add_to_dictionary(dictionary, key, value) -> Graph:
    """Bool Add To Dictionary

    Adds a Bool to a Dictionary

    Args:
        dictionary: Graph of Dictionary
        key: Graph of String
        value: Graph of Bool
        

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    dictionary_parsed = parse_graph(dictionary)
    key_parsed = parse_string_graph(key)
    value_parsed = parse_bool_graph(value)
    return bool_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

def bool_if(bool, input_1, input_2) -> Graph:
    """Bool If

    If the boolean is true returns input 1, otherwise input 2. Type: Bool

    Args:
        bool: Graph of Bool
        input 1: Graph of Bool
        input 2: Graph of Bool
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    bool_parsed = parse_bool_graph(bool)
    input_1_parsed = parse_bool_graph(input_1)
    input_2_parsed = parse_bool_graph(input_2)
    return bool_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

def bounds2f_from_x_y_width_height(x, y, width, height) -> Graph:
    """Bounds 2D Float from X, Y, Width & Height

    Creates the bounds of a 2D float region from its X, Y, Width and Height.

    Args:
        x: Graph of Float
        y: Graph of Float
        width: Graph of Float
        height: Graph of Float
        

    Returns:
        Graph: A graph node producing a Bounds2f.
    """
    x_parsed = parse_float_graph(x)
    y_parsed = parse_float_graph(y)
    width_parsed = parse_float_graph(width)
    height_parsed = parse_float_graph(height)
    return bounds2f_from_x_y_width_height_internal(x_parsed, y_parsed, width_parsed, height_parsed)

def bounds2i_from_x_y_width_height(x, y, width, height) -> Graph:
    """Bounds 2D Int from X, Y, Width & Height

    Creates the bounds of a 2D array from its X, Y, Width and Height.

    Args:
        x: Graph of Int
        y: Graph of Int
        width: Graph of Int
        height: Graph of Int
        

    Returns:
        Graph: A graph node producing a Bounds2i.
    """
    x_parsed = parse_int_graph(x)
    y_parsed = parse_int_graph(y)
    width_parsed = parse_int_graph(width)
    height_parsed = parse_int_graph(height)
    return bounds2i_from_x_y_width_height_internal(x_parsed, y_parsed, width_parsed, height_parsed)

def brush_solid(color, radius) -> Graph:
    """Brush Solid

    Creates a brush with a color and radius. Will stroke with the solid color.

    Args:
        color: Graph of RGBAColor
        radius: Graph of Float
        

    Returns:
        Graph: A graph node producing a Brush.
    """
    color_parsed = parse_graph(color)
    radius_parsed = parse_float_graph(radius)
    return brush_solid_internal(color_parsed, radius_parsed)

def byte_list_from_u_r_l(url) -> Graph:
    """Byte List from URL

    Given a URL. Performs a GET request and downloads the result as bytes.

    Args:
        url: Graph of String
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    url_parsed = parse_string_graph(url)
    return byte_list_from_u_r_l_internal(url_parsed)

def color_profile_b_t709() -> Graph:
    """Color Profile BT.709

    Creates a BT.709 Color Profile

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return color_profile_b_t709_internal()

def color_profile_ok_lab_a() -> Graph:
    """Color Profile OkLabA

    Creates an OkLabA color profile. OkLab with also an alpha component.

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return color_profile_ok_lab_a_internal()

def color_profile_p3() -> Graph:
    """Color Profile P3

    Creates a P3 Color Profile

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return color_profile_p3_internal()

def color_profile_p_n_g_s_r_g_b() -> Graph:
    """Color Profile PNG sRGB

    Creates a color profile that is the same one as PNG sRGB.

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return color_profile_p_n_g_s_r_g_b_internal()

def color_profile_s_r_g_b() -> Graph:
    """Color Profile sRGB

    Creates an sRGB Color Profile

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return color_profile_s_r_g_b_internal()

def composition_absolute_value(image) -> Graph:
    """Composition Absolute Value

    Takes the absolute value of all the pixels in the image.

    Args:
        image: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    image_parsed = parse_graph(image)
    return composition_absolute_value_internal(image_parsed)

def composition_bilinear_interpolation(composition, size) -> Graph:
    """Composition Scale Bilinear Interpolation

    Uses the bilinear interpolation algorithm to scale an image recipe

    Args:
        composition: Graph of Composition
        size: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    size_parsed = parse_graph(size)
    return composition_bilinear_interpolation_internal(composition_parsed, size_parsed)

def composition_blend_add(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Add

    Adds the foreground and background images together using additive blending.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        foreground transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return composition_blend_add_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_alpha(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Alpha

    Blends between the foreground and background using the alpha component of the foreground. 1 is foreground. 0 is background.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        foreground transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return composition_blend_alpha_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_max(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Max

    Blends the foreground and background images using maximum value blending.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        foreground transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return composition_blend_max_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_min(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Min

    Blends the foreground and background images using minimum blending, taking the minimum value for each pixel.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        foreground transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return composition_blend_min_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_multiply(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Multiply

    Multiplies the foreground and background images together using multiply blending.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        foreground transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return composition_blend_multiply_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_stencil(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Stencil

    Blends the foreground and background images using stencil blending. When the foreground is over the background, the foreground's alpha and the background's r, g and b are used.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        foreground transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return composition_blend_stencil_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_subtract(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Subtract

    Subtracts the foreground image from the background image using subtractive blending.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        foreground transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return composition_blend_subtract_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_with_factor(foreground, background, factor) -> Graph:
    """Composition Blend with Factor

    Blends the foreground and background compositions together using a factor. Internally, this modifies the alpha of the foreground by multiplying by the factor on the alpha component and then performing an alpha blend.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        factor: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    factor_parsed = parse_graph(factor)
    return composition_blend_with_factor_internal(foreground_parsed, background_parsed, factor_parsed)

def composition_box_blur(composition, dimension) -> Graph:
    """Composition Box Blur

    Applies a box blur to an image. Dimension is the size. 1 corresponding to 3x3, 2 5x5 and so on.

    Args:
        composition: Graph of Composition
        dimension: Graph of Int
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    dimension_parsed = parse_int_graph(dimension)
    return composition_box_blur_internal(composition_parsed, dimension_parsed)

def composition_box_blur_with_ok_lab(composition, dimension) -> Graph:
    """Composition Box Blur with OkLab

    Applies a box blur to an image in OkLab color space. Dimension is the size. 1 corresponding to 3x3, 2 5x5 and so on.

    Args:
        composition: Graph of Composition
        dimension: Graph of Int
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    dimension_parsed = parse_int_graph(dimension)
    return composition_box_blur_with_ok_lab_internal(composition_parsed, dimension_parsed)

def composition_brightness_adjust(composition, scale) -> Graph:
    """Composition Brightness Adjust

    Adjusts the brightness of an image by a given factor. Internally, works by modifying the L component of OkLab by multiplying it by the scale.

    Args:
        composition: Graph of Composition
        scale: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    scale_parsed = parse_float_graph(scale)
    return composition_brightness_adjust_internal(composition_parsed, scale_parsed)

def composition_chroma_offset(composition, offset) -> Graph:
    """Composition Chroma Offset

    Applies a chroma offset to an image. This is done by modifying the a and b components of OkLab. For the vector, X applies to a, Y to to b.

    Args:
        composition: Graph of Composition
        offset: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    offset_parsed = parse_graph(offset)
    return composition_chroma_offset_internal(composition_parsed, offset_parsed)

def composition_color_convert(composition, color_profile) -> Graph:
    """Composition Color Convert

    Converts a Composition from one color space to another.

    Args:
        composition: Graph of Composition
        color profile: Graph of ColorProfile
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    color_profile_parsed = parse_graph(color_profile)
    return composition_color_convert_internal(composition_parsed, color_profile_parsed)

def composition_color_invert(composition) -> Graph:
    """Composition Color Invert

    Applies a color invert operation to a Composition. Taking 1 and subtracting each RGB operation against it.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return composition_color_invert_internal(composition_parsed)

def composition_color_profile(composition) -> Graph:
    """Composition Color Profile

    Gets the color profile associated with a Composition

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    composition_parsed = parse_graph(composition)
    return composition_color_profile_internal(composition_parsed)

def composition_color_rect(color, color_profile, size) -> Graph:
    """Composition Color Rect

    Given a color and it's color proile. Creates a rectangle Composition of that color.

    Args:
        color: Graph of RGBAColor
        color profile: Graph of ColorProfile
        size: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    color_parsed = parse_graph(color)
    color_profile_parsed = parse_graph(color_profile)
    size_parsed = parse_graph(size)
    return composition_color_rect_internal(color_parsed, color_profile_parsed, size_parsed)

def composition_color_threshold(composition, threshold) -> Graph:
    """Composition Color Threshold

    Applies a color threshold to a Composition

    Args:
        composition: Graph of Composition
        threshold: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    threshold_parsed = parse_float_graph(threshold)
    return composition_color_threshold_internal(composition_parsed, threshold_parsed)

def composition_contrast_adjustment(composition, contrast) -> Graph:
    """Composition Contrast Adjustment

    Adjusts the contrast of a Composition

    Args:
        composition: Graph of Composition
        contrast: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    contrast_parsed = parse_float_graph(contrast)
    return composition_contrast_adjustment_internal(composition_parsed, contrast_parsed)

def composition_convolution(composition, kernel, kernel_width, kernel_height) -> Graph:
    """Composition Convolution

    Performs a convolution on an composition

    Args:
        The image to perform the convolution on: Graph of Composition
        kernel: Graph of FloatList
        kernel width: Graph of Int
        kernel height: Graph of Int
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    kernel_parsed = parse_graph(kernel)
    kernel_width_parsed = parse_int_graph(kernel_width)
    kernel_height_parsed = parse_int_graph(kernel_height)
    return composition_convolution_internal(composition_parsed, kernel_parsed, kernel_width_parsed, kernel_height_parsed)

def composition_crop(composition, rect) -> Graph:
    """Composition Crop

    Applies a crop to a Composition

    Args:
        composition: Graph of Composition
        rect: Graph of Bounds2i
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    rect_parsed = parse_graph(rect)
    return composition_crop_internal(composition_parsed, rect_parsed)

def composition_custom_transformer_shader(composition, function_body, helpers, input_color_profile, output_color_profile, inputs, needs_sample_capability) -> Graph:
    """Composition Custom Transformer Shader

    Given an input, runs a custom defined shader over that input.

    Args:
        composition: Graph of Composition
        function body: Graph of String
        helpers: Graph of String
        input color profile: Graph of ColorProfile
        output color profile: Graph of ColorProfile
        inputs: Graph of Dictionary
        needs sample capability: Graph of Bool
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    function_body_parsed = parse_string_graph(function_body)
    helpers_parsed = parse_string_graph(helpers)
    input_color_profile_parsed = parse_graph(input_color_profile)
    output_color_profile_parsed = parse_graph(output_color_profile)
    inputs_parsed = parse_graph(inputs)
    needs_sample_capability_parsed = parse_bool_graph(needs_sample_capability)
    return composition_custom_transformer_shader_internal(composition_parsed, function_body_parsed, helpers_parsed, input_color_profile_parsed, output_color_profile_parsed, inputs_parsed, needs_sample_capability_parsed)

def composition_flip_horizontal(composition) -> Graph:
    """Composition Flip Horizontal

    Flips the image along the horizontal axis

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return composition_flip_horizontal_internal(composition_parsed)

def composition_flip_vertical(composition) -> Graph:
    """Composition Flip Vertical

    Flips the image vertically

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return composition_flip_vertical_internal(composition_parsed)

def composition_from_asset(asset_id) -> Graph:
    """Composition from Asset

    Creates a composition from an asset in your catalog.

    Args:
        asset id: Graph of Int
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    asset_id_parsed = parse_int_graph(asset_id)
    return composition_from_asset_internal(asset_id_parsed)

def composition_from_image(image) -> Graph:
    """Composition from Image

    Creates an composition out of an image

    Args:
        image: Graph of Image
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    image_parsed = parse_graph(image)
    return composition_from_image_internal(image_parsed)

def composition_gaussian_blur(composition, sigma) -> Graph:
    """Composition Gaussian Blur

    Applies a gaussian blur to an image. Sigma controls the blur intensity.

    Args:
        composition: Graph of Composition
        sigma: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    sigma_parsed = parse_float_graph(sigma)
    return composition_gaussian_blur_internal(composition_parsed, sigma_parsed)

def composition_gaussian_blur_with_ok_lab(composition, sigma) -> Graph:
    """Composition Gaussian Blur with OkLab

    Applies a gaussian blur to an image in OkLab color space. Sigma controls the blur intensity.

    Args:
        composition: Graph of Composition
        sigma: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    sigma_parsed = parse_float_graph(sigma)
    return composition_gaussian_blur_with_ok_lab_internal(composition_parsed, sigma_parsed)

def composition_grayscale(composition) -> Graph:
    """Composition Grayscale

    Applies grayscale to a Composition

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return composition_grayscale_internal(composition_parsed)

def composition_if(bool, input_1, input_2) -> Graph:
    """Composition If

    If the boolean is true returns input 1, otherwise input 2. Type: Composition

    Args:
        bool: Graph of Bool
        input 1: Graph of Composition
        input 2: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    bool_parsed = parse_bool_graph(bool)
    input_1_parsed = parse_graph(input_1)
    input_2_parsed = parse_graph(input_2)
    return composition_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

def composition_l_curve(composition, l_curve) -> Graph:
    """Composition Lightness Curve

    Applies a curve to the L component in an OkLab color. Adjusting the lightness of the image.

    Args:
        composition: Graph of Composition
        l curve: Graph of Curve
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    l_curve_parsed = parse_graph(l_curve)
    return composition_l_curve_internal(composition_parsed, l_curve_parsed)

def composition_linear_transform(composition, entry_0_0, entry_0_1, entry_0_2, entry_0_3, entry_1_0, entry_1_1, entry_1_2, entry_1_3, entry_2_0, entry_2_1, entry_2_2, entry_2_3, entry_3_0, entry_3_1, entry_3_2, entry_3_3) -> Graph:
    """Composition RGBA Linear Transform

    Applies a linear transform to a Composition's RGBA values. Before application, will convert to a linear version of the color profile and will convert to an RGB profile if needed.

    Args:
        composition: Graph of Composition
        entry 0,0: Graph of Float
        entry 0,1: Graph of Float
        entry 0,2: Graph of Float
        entry 0,3: Graph of Float
        entry 1,0: Graph of Float
        entry 1,1: Graph of Float
        entry 1,2: Graph of Float
        entry 1,3: Graph of Float
        entry 2,0: Graph of Float
        entry 2,1: Graph of Float
        entry 2,2: Graph of Float
        entry 2,3: Graph of Float
        entry 3,0: Graph of Float
        entry 3,1: Graph of Float
        entry 3,2: Graph of Float
        entry 3,3: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    entry_0_0_parsed = parse_float_graph(entry_0_0)
    entry_0_1_parsed = parse_float_graph(entry_0_1)
    entry_0_2_parsed = parse_float_graph(entry_0_2)
    entry_0_3_parsed = parse_float_graph(entry_0_3)
    entry_1_0_parsed = parse_float_graph(entry_1_0)
    entry_1_1_parsed = parse_float_graph(entry_1_1)
    entry_1_2_parsed = parse_float_graph(entry_1_2)
    entry_1_3_parsed = parse_float_graph(entry_1_3)
    entry_2_0_parsed = parse_float_graph(entry_2_0)
    entry_2_1_parsed = parse_float_graph(entry_2_1)
    entry_2_2_parsed = parse_float_graph(entry_2_2)
    entry_2_3_parsed = parse_float_graph(entry_2_3)
    entry_3_0_parsed = parse_float_graph(entry_3_0)
    entry_3_1_parsed = parse_float_graph(entry_3_1)
    entry_3_2_parsed = parse_float_graph(entry_3_2)
    entry_3_3_parsed = parse_float_graph(entry_3_3)
    return composition_linear_transform_internal(composition_parsed, entry_0_0_parsed, entry_0_1_parsed, entry_0_2_parsed, entry_0_3_parsed, entry_1_0_parsed, entry_1_1_parsed, entry_1_2_parsed, entry_1_3_parsed, entry_2_0_parsed, entry_2_1_parsed, entry_2_2_parsed, entry_2_3_parsed, entry_3_0_parsed, entry_3_1_parsed, entry_3_2_parsed, entry_3_3_parsed)

def composition_monet_women_with_parasol() -> Graph:
    """Monet's Women with a Parasol

    Creates a composition from Monet's "Women with a Parasol" painting. Used frequently as a test asset.

    Returns:
        Graph: A graph node producing a Composition.
    """
    return composition_monet_women_with_parasol_internal()

def composition_morphological_max(composition, dimension) -> Graph:
    """Composition Morphological Max

    Apples a morphological max operation.

    Args:
        composition: Graph of Composition
        dimension: Graph of Int
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    dimension_parsed = parse_int_graph(dimension)
    return composition_morphological_max_internal(composition_parsed, dimension_parsed)

def composition_morphological_min(composition, dimension) -> Graph:
    """Composition Morphological Min

    Apples a morphological min operation.

    Args:
        composition: Graph of Composition
        dimension: Graph of Int
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    dimension_parsed = parse_int_graph(dimension)
    return composition_morphological_min_internal(composition_parsed, dimension_parsed)

def composition_painter(painter) -> Graph:
    """Composition Painter

    Creates a composition from a painter.

    Args:
        painter: Graph of Painter
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    painter_parsed = parse_graph(painter)
    return composition_painter_internal(painter_parsed)

def composition_passthrough(value) -> Graph:
    """Composition Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    value_parsed = parse_graph(value)
    return composition_passthrough_internal(value_parsed)

def composition_pixelate(composition, pixel_size) -> Graph:
    """Composition Pixelate

    Applies a pixelation effect to a composition.

    Args:
        composition: Graph of Composition
        pixel size: Graph of Int
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    pixel_size_parsed = parse_int_graph(pixel_size)
    return composition_pixelate_internal(composition_parsed, pixel_size_parsed)

def composition_r_g_b_curve(composition, r_curve, g_curve, b_curve) -> Graph:
    """Composition RGB Curve

    Applies a curve to the R, G, and B components

    Args:
        composition: Graph of Composition
        r curve: Graph of Curve
        g curve: Graph of Curve
        b curve: Graph of Curve
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    r_curve_parsed = parse_graph(r_curve)
    g_curve_parsed = parse_graph(g_curve)
    b_curve_parsed = parse_graph(b_curve)
    return composition_r_g_b_curve_internal(composition_parsed, r_curve_parsed, g_curve_parsed, b_curve_parsed)

def composition_render_to_image(composition) -> Graph:
    """Composition Render to Image

    Renders a Composition to an Image

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Image.
    """
    composition_parsed = parse_graph(composition)
    return composition_render_to_image_internal(composition_parsed)

def composition_rotate180(composition) -> Graph:
    """Composition Rotate 180

    Rotates the image 180 degrees

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return composition_rotate180_internal(composition_parsed)

def composition_rotate90_clockwise(composition) -> Graph:
    """Composition Rotate 90 Clockwise

    Rotates the image 90 degrees clockwise

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return composition_rotate90_clockwise_internal(composition_parsed)

def composition_rotate90_counter_clockwise(composition) -> Graph:
    """Composition Rotate 90 Counter Clockwise

    Rotates the image 90 degrees counter-clockwise

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return composition_rotate90_counter_clockwise_internal(composition_parsed)

def composition_s_a_m3_image(composition, prompt, positive_points, negative_points) -> Graph:
    """Composition SAM3 Image

    Runs the SAM3 model on an image

    Args:
        composition: Graph of Composition
        prompt: Graph of String
        positive points: Graph of Point2iList
        negative points: Graph of Point2iList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    composition_parsed = parse_graph(composition)
    prompt_parsed = parse_string_graph(prompt)
    positive_points_parsed = parse_graph(positive_points)
    negative_points_parsed = parse_graph(negative_points)
    return composition_s_a_m3_image_internal(composition_parsed, prompt_parsed, positive_points_parsed, negative_points_parsed)

def composition_saturation_adjust(composition, scale) -> Graph:
    """Composition Saturation Adjust

    Adjusts the saturation of an image by a given factor. Internally, scales the chroma components in OkLab color space.

    Args:
        composition: Graph of Composition
        scale: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    scale_parsed = parse_float_graph(scale)
    return composition_saturation_adjust_internal(composition_parsed, scale_parsed)

def composition_scale_nearest_neighbor(composition, size) -> Graph:
    """Composition Scale Nearest Neighbor

    Uses the nearest neighbor algorithm to scale an image recipe

    Args:
        composition: Graph of Composition
        size: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    size_parsed = parse_graph(size)
    return composition_scale_nearest_neighbor_internal(composition_parsed, size_parsed)

def composition_segment(composition, prompt, positive_points, negative_points) -> Graph:
    """Composition Segment

    Segments objects in a composition using SAM3. Accepts a text prompt and lists of positive/negative click points.

    Args:
        composition: Graph of Composition
        prompt: Graph of String
        positive points: Graph of Point2iList
        negative points: Graph of Point2iList
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    prompt_parsed = parse_string_graph(prompt)
    positive_points_parsed = parse_graph(positive_points)
    negative_points_parsed = parse_graph(negative_points)
    return composition_segment_internal(composition_parsed, prompt_parsed, positive_points_parsed, negative_points_parsed)

def composition_sharpen(composition, radius, strength) -> Graph:
    """Composition Sharpen

    Applies a sharpen filter to the composition.

    Args:
        composition: Graph of Composition
        radius: Graph of Float
        strength: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    radius_parsed = parse_float_graph(radius)
    strength_parsed = parse_float_graph(strength)
    return composition_sharpen_internal(composition_parsed, radius_parsed, strength_parsed)

def composition_size(composition) -> Graph:
    """Composition Size

    Gets the resulting size of a Composition

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Vector2i.
    """
    composition_parsed = parse_graph(composition)
    return composition_size_internal(composition_parsed)

def composition_sobel_edge_detection(composition) -> Graph:
    """Composition Sobel Edge Detection

    Applies Sobel edge detection to an image.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return composition_sobel_edge_detection_internal(composition_parsed)

def composition_swirl(composition, center, radius, amount) -> Graph:
    """Composition Swirl

    Applies a swirl distortion to this composition

    Args:
        composition: Graph of Composition
        center: Graph of Vector2f
        radius: Graph of Float
        amount: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    center_parsed = parse_graph(center)
    radius_parsed = parse_float_graph(radius)
    amount_parsed = parse_float_graph(amount)
    return composition_swirl_internal(composition_parsed, center_parsed, radius_parsed, amount_parsed)

def composition_target_white_kelvin(composition, kelvin) -> Graph:
    """Composition Target White Kelvin

    Sets the image white point to the value specified in Kelvin. The profile connection white point is D50, so you will only see changes as you move away from that.

    Args:
        composition: Graph of Composition
        kelvin: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    kelvin_parsed = parse_float_graph(kelvin)
    return composition_target_white_kelvin_internal(composition_parsed, kelvin_parsed)

def composition_to_ok_lab_hist(composition) -> Graph:
    """Composition to OkLab Histogram

    Creates an OkLab Histogram from the colors in a Composition.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a OkLabHist.
    """
    composition_parsed = parse_graph(composition)
    return composition_to_ok_lab_hist_internal(composition_parsed)

def composition_vignette(composition, radius, softness, strength) -> Graph:
    """Composition Vignette

    darkens the outer edges - radius (0-1, measured relative to the image's smaller dimension) sets how far the bright center extends, Softness (typically 0.05-0.5) controls the width of the fade-out band, and Strength (0–1) defines how dark the edges become at maximum.

    Args:
        composition: Graph of Composition
        radius: Graph of Float
        softness: Graph of Float
        strength: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    radius_parsed = parse_float_graph(radius)
    softness_parsed = parse_float_graph(softness)
    strength_parsed = parse_float_graph(strength)
    return composition_vignette_internal(composition_parsed, radius_parsed, softness_parsed, strength_parsed)

def composition_zoom_blur(composition, center, strength) -> Graph:
    """Composition Zoom Blur

    Performs a zoom blur on this composition

    Args:
        composition: Graph of Composition
        center: Graph of Vector2f
        strength: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    center_parsed = parse_graph(center)
    strength_parsed = parse_float_graph(strength)
    return composition_zoom_blur_internal(composition_parsed, center_parsed, strength_parsed)

def curve_evaluate(curve, input) -> Graph:
    """Curve Evaluate

    Evaluates a curve at a given input value.

    Args:
        curve: Graph of Curve
        input: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    curve_parsed = parse_graph(curve)
    input_parsed = parse_float_graph(input)
    return curve_evaluate_internal(curve_parsed, input_parsed)

def curve_gamma(gamma) -> Graph:
    """Curve Gamma

    A gamma curve. The gamma parameter corresponding to y=x^gamma.

    Args:
        gamma: Graph of Float
        

    Returns:
        Graph: A graph node producing a Curve.
    """
    gamma_parsed = parse_float_graph(gamma)
    return curve_gamma_internal(gamma_parsed)

def curve_identity() -> Graph:
    """Curve Identity

    An identity curve, y=x

    Returns:
        Graph: A graph node producing a Curve.
    """
    return curve_identity_internal()

def curve_pivoted_sigmoid(pivot, slope) -> Graph:
    """Curve Pivoted Sigmoid

    A pivoted sigmoid contrast curve that anchors at the pivot and smoothly compresses shadows and highlights, with a slope parameter controlling midtone contrast.

    Args:
        pivot: Graph of Float
        slope: Graph of Float
        

    Returns:
        Graph: A graph node producing a Curve.
    """
    pivot_parsed = parse_float_graph(pivot)
    slope_parsed = parse_float_graph(slope)
    return curve_pivoted_sigmoid_internal(pivot_parsed, slope_parsed)

def curve_s_curve(pivot, slope, toe, shoulder) -> Graph:
    """Curve S

    An S-curve remaps values by anchoring contrast at a chosen pivot, increasing or decreasing midtone separation via slope, gently flattening the curve near black with toe to compress or lift shadows, and softly flattening near white with shoulder to roll off highlights, while keeping black and white fixed.

    Args:
        pivot: Graph of Float
        slope: Graph of Float
        toe: Graph of Float
        shoulder: Graph of Float
        

    Returns:
        Graph: A graph node producing a Curve.
    """
    pivot_parsed = parse_float_graph(pivot)
    slope_parsed = parse_float_graph(slope)
    toe_parsed = parse_float_graph(toe)
    shoulder_parsed = parse_float_graph(shoulder)
    return curve_s_curve_internal(pivot_parsed, slope_parsed, toe_parsed, shoulder_parsed)

def dictionary_create() -> Graph:
    """Dictionary Create

    Creates a new dictionary

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    return dictionary_create_internal()

def file_convert_image_to_bmp(image_bytes) -> Graph:
    """File Convert Image to BMP

    Converts any image format (JPEG, PNG, WebP, TIFF, HEIC, etc.) to BMP. Returns BMP bytes.

    Args:
        image bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_bytes_parsed = parse_graph(image_bytes)
    return file_convert_image_to_bmp_internal(image_bytes_parsed)

def file_convert_image_to_heic(image_bytes, quality) -> Graph:
    """File Convert Image to HEIC

    Converts any image format (JPEG, PNG, WebP, TIFF, BMP, etc.) to HEIC. Returns HEIC bytes.

    Args:
        image bytes (any format): Graph of ByteList
        HEIC quality (1-100): Graph of Int
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_bytes_parsed = parse_graph(image_bytes)
    quality_parsed = parse_int_graph(quality)
    return file_convert_image_to_heic_internal(image_bytes_parsed, quality_parsed)

def file_convert_image_to_jpeg(image_bytes, quality) -> Graph:
    """File Convert Image to JPEG

    Converts any image format (PNG, WebP, TIFF, BMP, HEIC, etc.) to JPEG. Returns JPEG bytes.

    Args:
        image bytes (any format): Graph of ByteList
        JPEG quality (1-100): Graph of Int
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_bytes_parsed = parse_graph(image_bytes)
    quality_parsed = parse_int_graph(quality)
    return file_convert_image_to_jpeg_internal(image_bytes_parsed, quality_parsed)

def file_convert_image_to_png(image_bytes) -> Graph:
    """File Convert Image to PNG

    Converts any image format (JPEG, WebP, TIFF, BMP, HEIC, etc.) to PNG. Returns PNG bytes.

    Args:
        image bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_bytes_parsed = parse_graph(image_bytes)
    return file_convert_image_to_png_internal(image_bytes_parsed)

def file_convert_image_to_tiff(image_bytes) -> Graph:
    """File Convert Image to TIFF

    Converts any image format (JPEG, PNG, WebP, BMP, HEIC, etc.) to TIFF. Returns TIFF bytes.

    Args:
        image bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_bytes_parsed = parse_graph(image_bytes)
    return file_convert_image_to_tiff_internal(image_bytes_parsed)

def file_convert_image_to_web_p(image_bytes, quality) -> Graph:
    """File Convert Image to WebP

    Converts any image format (JPEG, PNG, TIFF, BMP, HEIC, etc.) to WebP. Returns WebP bytes.

    Args:
        image bytes (any format): Graph of ByteList
        WebP quality (1-100): Graph of Int
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_bytes_parsed = parse_graph(image_bytes)
    quality_parsed = parse_int_graph(quality)
    return file_convert_image_to_web_p_internal(image_bytes_parsed, quality_parsed)

def file_convert_video_to_animated_web_p(video_bytes) -> Graph:
    """File Convert Video to Animated WebP

    Converts any video format (MP4, MOV, WebM, AVI, MKV) to an animated WebP. Returns animated WebP bytes.

    Args:
        video bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    video_bytes_parsed = parse_graph(video_bytes)
    return file_convert_video_to_animated_web_p_internal(video_bytes_parsed)

def file_convert_video_to_gif(video_bytes, frame_rate) -> Graph:
    """File Convert Video to GIF

    Converts any video format (MP4, MOV, WebM, AVI, MKV) to a GIF. Returns GIF bytes.

    Args:
        video bytes (any format): Graph of ByteList
        frame rate: Graph of Int
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    video_bytes_parsed = parse_graph(video_bytes)
    frame_rate_parsed = parse_int_graph(frame_rate)
    return file_convert_video_to_gif_internal(video_bytes_parsed, frame_rate_parsed)

def file_convert_video_to_m_p4(video_bytes) -> Graph:
    """File Convert Video to MP4

    Converts any video format (MOV, WebM, AVI, MKV) to MP4. Returns MP4 bytes.

    Args:
        video bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    video_bytes_parsed = parse_graph(video_bytes)
    return file_convert_video_to_m_p4_internal(video_bytes_parsed)

def file_convert_video_to_web_m(video_bytes) -> Graph:
    """File Convert Video to WebM

    Converts any video format (MP4, MOV, AVI, MKV) to WebM. Returns WebM bytes.

    Args:
        video bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    video_bytes_parsed = parse_graph(video_bytes)
    return file_convert_video_to_web_m_internal(video_bytes_parsed)

def fill_custom(function_body, helpers, inputs) -> Graph:
    """Fill Custom

    Creates a fill with a custom shader.

    Args:
        function body: Graph of String
        helpers: Graph of String
        inputs: Graph of Dictionary
        

    Returns:
        Graph: A graph node producing a Fill.
    """
    function_body_parsed = parse_string_graph(function_body)
    helpers_parsed = parse_string_graph(helpers)
    inputs_parsed = parse_graph(inputs)
    return fill_custom_internal(function_body_parsed, helpers_parsed, inputs_parsed)

def fill_solid(color) -> Graph:
    """Fill Solid

    Creates a fill with a solid color.

    Args:
        color: Graph of RGBAColor
        

    Returns:
        Graph: A graph node producing a Fill.
    """
    color_parsed = parse_graph(color)
    return fill_solid_internal(color_parsed)

def float_add(float1, float2) -> Graph:
    """Float Add

    Adds two floats together.

    Args:
        float1: Graph of Float
        float2: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    float1_parsed = parse_float_graph(float1)
    float2_parsed = parse_float_graph(float2)
    return float_add_internal(float1_parsed, float2_parsed)

def float_add_to_dictionary(dictionary, key, value) -> Graph:
    """Float Add To Dictionary

    Adds a Float to a Dictionary

    Args:
        dictionary: Graph of Dictionary
        key: Graph of String
        value: Graph of Float
        

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    dictionary_parsed = parse_graph(dictionary)
    key_parsed = parse_string_graph(key)
    value_parsed = parse_float_graph(value)
    return float_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

def float_cos(angle) -> Graph:
    """Float Cosine

    Computes the cosine of a float (in radians).

    Args:
        Angle in radians: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    angle_parsed = parse_float_graph(angle)
    return float_cos_internal(angle_parsed)

def float_divide(float1, float2) -> Graph:
    """Float Divide

    Adds two floats together.

    Args:
        float1: Graph of Float
        float2: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    float1_parsed = parse_float_graph(float1)
    float2_parsed = parse_float_graph(float2)
    return float_divide_internal(float1_parsed, float2_parsed)

def float_equals(float_1, float_2) -> Graph:
    """Float Equals

    Checks if two floats are equal

    Args:
        First Float: Graph of Float
        Second Float: Graph of Float
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    float_1_parsed = parse_float_graph(float_1)
    float_2_parsed = parse_float_graph(float_2)
    return float_equals_internal(float_1_parsed, float_2_parsed)

def float_greater_than(float_1, float_2) -> Graph:
    """Float Greater Than

    Checks if the first float is greater than the second float

    Args:
        First Float: Graph of Float
        Second Float: Graph of Float
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    float_1_parsed = parse_float_graph(float_1)
    float_2_parsed = parse_float_graph(float_2)
    return float_greater_than_internal(float_1_parsed, float_2_parsed)

def float_greater_than_or_equal(float_1, float_2) -> Graph:
    """Float Greater Than Or Equal

    Checks if the first float is greater than or equal to the second float

    Args:
        First Float: Graph of Float
        Second Float: Graph of Float
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    float_1_parsed = parse_float_graph(float_1)
    float_2_parsed = parse_float_graph(float_2)
    return float_greater_than_or_equal_internal(float_1_parsed, float_2_parsed)

def float_if(bool, input_1, input_2) -> Graph:
    """Float If

    If the boolean is true returns input 1, otherwise input 2. Type: Float

    Args:
        bool: Graph of Bool
        input 1: Graph of Float
        input 2: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    bool_parsed = parse_bool_graph(bool)
    input_1_parsed = parse_float_graph(input_1)
    input_2_parsed = parse_float_graph(input_2)
    return float_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

def float_lerp(x, float1, float2) -> Graph:
    """Float Lerp

    Lerps between two floats using the x parameter

    Args:
        x: Graph of Float
        float1: Graph of Float
        float2: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    x_parsed = parse_float_graph(x)
    float1_parsed = parse_float_graph(float1)
    float2_parsed = parse_float_graph(float2)
    return float_lerp_internal(x_parsed, float1_parsed, float2_parsed)

def float_less_than(float_1, float_2) -> Graph:
    """Float Less Than

    Checks if the first float is less than the second float

    Args:
        First Float: Graph of Float
        Second Float: Graph of Float
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    float_1_parsed = parse_float_graph(float_1)
    float_2_parsed = parse_float_graph(float_2)
    return float_less_than_internal(float_1_parsed, float_2_parsed)

def float_less_than_or_equal(float_1, float_2) -> Graph:
    """Float Less Than Or Equal

    Checks if the first float is less than or equal to the second float

    Args:
        First Float: Graph of Float
        Second Float: Graph of Float
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    float_1_parsed = parse_float_graph(float_1)
    float_2_parsed = parse_float_graph(float_2)
    return float_less_than_or_equal_internal(float_1_parsed, float_2_parsed)

def float_max(float1, float2) -> Graph:
    """Float Max

    Returns the maximum float.

    Args:
        float1: Graph of Float
        float2: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    float1_parsed = parse_float_graph(float1)
    float2_parsed = parse_float_graph(float2)
    return float_max_internal(float1_parsed, float2_parsed)

def float_min(float1, float2) -> Graph:
    """Float Min

    Returns the minimum float.

    Args:
        float1: Graph of Float
        float2: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    float1_parsed = parse_float_graph(float1)
    float2_parsed = parse_float_graph(float2)
    return float_min_internal(float1_parsed, float2_parsed)

def float_multiply(float1, float2) -> Graph:
    """Float Multiply

    Multiplies two floats together.

    Args:
        float1: Graph of Float
        float2: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    float1_parsed = parse_float_graph(float1)
    float2_parsed = parse_float_graph(float2)
    return float_multiply_internal(float1_parsed, float2_parsed)

def float_passthrough(value) -> Graph:
    """Float Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    value_parsed = parse_float_graph(value)
    return float_passthrough_internal(value_parsed)

def float_pow(float1, float2) -> Graph:
    """Float Power

    Raises float 1 to the power of float 2

    Args:
        float 1: Graph of Float
        float 2: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    float1_parsed = parse_float_graph(float1)
    float2_parsed = parse_float_graph(float2)
    return float_pow_internal(float1_parsed, float2_parsed)

def float_round_to_int(float) -> Graph:
    """Float Round to Int

    Rounds the float to the nearest int

    Args:
        float: Graph of Float
        

    Returns:
        Graph: A graph node producing a Int.
    """
    float_parsed = parse_float_graph(float)
    return float_round_to_int_internal(float_parsed)

def float_sin(angle) -> Graph:
    """Float Sine

    Computes the sine of a float (in radians).

    Args:
        Angle in radians: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    angle_parsed = parse_float_graph(angle)
    return float_sin_internal(angle_parsed)

def float_square_root(number) -> Graph:
    """Float Square Root

    Compares the square root of a number

    Args:
        Number: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    number_parsed = parse_float_graph(number)
    return float_square_root_internal(number_parsed)

def float_squared(number) -> Graph:
    """Float Squared

    Raises a float to the power of 2.

    Args:
        Number: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    number_parsed = parse_float_graph(number)
    return float_squared_internal(number_parsed)

def float_subtract(float1, float2) -> Graph:
    """Float Subtract

    Adds two floats together.

    Args:
        float1: Graph of Float
        float2: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    float1_parsed = parse_float_graph(float1)
    float2_parsed = parse_float_graph(float2)
    return float_subtract_internal(float1_parsed, float2_parsed)

def image_from_byte_list(bytes) -> Graph:
    """Image from Bytes

    Given some bytes, parses an image

    Args:
        bytes: Graph of ByteList
        

    Returns:
        Graph: A graph node producing a Image.
    """
    bytes_parsed = parse_graph(bytes)
    return image_from_byte_list_internal(bytes_parsed)

def image_to_byte_list(image) -> Graph:
    """Image to Byte List

    Given an image, converts it to a byte list

    Args:
        image: Graph of Image
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_parsed = parse_graph(image)
    return image_to_byte_list_internal(image_parsed)

def int_abs(number) -> Graph:
    """Int Absolute Value

    Returns the absolute value of an int

    Args:
        number: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    number_parsed = parse_int_graph(number)
    return int_abs_internal(number_parsed)

def int_add(int_1, int_2) -> Graph:
    """Int Add

    Adds to ints together

    Args:
        First Int: Graph of Int
        Second Int: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    int_1_parsed = parse_int_graph(int_1)
    int_2_parsed = parse_int_graph(int_2)
    return int_add_internal(int_1_parsed, int_2_parsed)

def int_add_to_dictionary(dictionary, key, value) -> Graph:
    """Int Add To Dictionary

    Adds a Int to a Dictionary

    Args:
        dictionary: Graph of Dictionary
        key: Graph of String
        value: Graph of Int
        

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    dictionary_parsed = parse_graph(dictionary)
    key_parsed = parse_string_graph(key)
    value_parsed = parse_int_graph(value)
    return int_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

def int_equals(int_1, int_2) -> Graph:
    """Int Equals

    Checks if two ints are equal

    Args:
        First Int: Graph of Int
        Second Int: Graph of Int
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    int_1_parsed = parse_int_graph(int_1)
    int_2_parsed = parse_int_graph(int_2)
    return int_equals_internal(int_1_parsed, int_2_parsed)

def int_greater_than(int_1, int_2) -> Graph:
    """Int Greater Than

    Checks if the first int is greater than the second int

    Args:
        First Int: Graph of Int
        Second Int: Graph of Int
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    int_1_parsed = parse_int_graph(int_1)
    int_2_parsed = parse_int_graph(int_2)
    return int_greater_than_internal(int_1_parsed, int_2_parsed)

def int_greater_than_or_equal(int_1, int_2) -> Graph:
    """Int Greater Than Or Equal

    Checks if the first int is greater than or equal to the second int

    Args:
        First Int: Graph of Int
        Second Int: Graph of Int
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    int_1_parsed = parse_int_graph(int_1)
    int_2_parsed = parse_int_graph(int_2)
    return int_greater_than_or_equal_internal(int_1_parsed, int_2_parsed)

def int_if(bool, input_1, input_2) -> Graph:
    """Int If

    If the boolean is true returns input 1, otherwise input 2. Type: Int

    Args:
        bool: Graph of Bool
        input 1: Graph of Int
        input 2: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    bool_parsed = parse_bool_graph(bool)
    input_1_parsed = parse_int_graph(input_1)
    input_2_parsed = parse_int_graph(input_2)
    return int_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

def int_less_than(int_1, int_2) -> Graph:
    """Int Less Than

    Checks if the first int is less than the second int

    Args:
        First Int: Graph of Int
        Second Int: Graph of Int
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    int_1_parsed = parse_int_graph(int_1)
    int_2_parsed = parse_int_graph(int_2)
    return int_less_than_internal(int_1_parsed, int_2_parsed)

def int_less_than_or_equal(int_1, int_2) -> Graph:
    """Int Less Than Or Equal

    Checks if the first int is less than or equal to the second int

    Args:
        First Int: Graph of Int
        Second Int: Graph of Int
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    int_1_parsed = parse_int_graph(int_1)
    int_2_parsed = parse_int_graph(int_2)
    return int_less_than_or_equal_internal(int_1_parsed, int_2_parsed)

def int_max(int1, int2) -> Graph:
    """Int Max

    Returns the maximum int.

    Args:
        int1: Graph of Int
        int2: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    int1_parsed = parse_int_graph(int1)
    int2_parsed = parse_int_graph(int2)
    return int_max_internal(int1_parsed, int2_parsed)

def int_min(int1, int2) -> Graph:
    """Int Min

    Returns the minimum int.

    Args:
        int1: Graph of Int
        int2: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    int1_parsed = parse_int_graph(int1)
    int2_parsed = parse_int_graph(int2)
    return int_min_internal(int1_parsed, int2_parsed)

def int_multiply(int_1, int_2) -> Graph:
    """Int Multiply

    Multiplies two integers together

    Args:
        First Int: Graph of Int
        Second Int: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    int_1_parsed = parse_int_graph(int_1)
    int_2_parsed = parse_int_graph(int_2)
    return int_multiply_internal(int_1_parsed, int_2_parsed)

def int_passthrough(value) -> Graph:
    """Int Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    value_parsed = parse_int_graph(value)
    return int_passthrough_internal(value_parsed)

def int_subtract(int_1, int_2) -> Graph:
    """Int Subtract

    Subtracts one int from another

    Args:
        int 1: Graph of Int
        int 2: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    int_1_parsed = parse_int_graph(int_1)
    int_2_parsed = parse_int_graph(int_2)
    return int_subtract_internal(int_1_parsed, int_2_parsed)

def int_to_float(int) -> Graph:
    """Int To Float

    Converts an Int to a Float

    Args:
        int: Graph of Int
        

    Returns:
        Graph: A graph node producing a Float.
    """
    int_parsed = parse_int_graph(int)
    return int_to_float_internal(int_parsed)

def monet_network_download_u_r_l_from_asset_i_d(asset_id) -> Graph:
    """Monet Network Download URL from Asset ID

    Creates a Download URL from asset ID in the Monet Network

    Args:
        asset id: Graph of Int
        

    Returns:
        Graph: A graph node producing a String.
    """
    asset_id_parsed = parse_int_graph(asset_id)
    return monet_network_download_u_r_l_from_asset_i_d_internal(asset_id_parsed)

def not_(bool) -> Graph:
    """Not

    Returns the opposite of a boolean

    Args:
        Bool: Graph of Bool
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    bool_parsed = parse_bool_graph(bool)
    return not_internal(bool_parsed)

def null_value() -> Graph:
    """Null Value

    Returns a null value

    Returns:
        Graph: A graph node producing a Null.
    """
    return null_value_internal()

def ok_lab_color_from_components(l, a, b) -> Graph:
    """OkLab Color from Components

    Given the L, a and b creates the color

    Args:
        l: Graph of Float
        a: Graph of Float
        b: Graph of Float
        

    Returns:
        Graph: A graph node producing a OkLabColor.
    """
    l_parsed = parse_float_graph(l)
    a_parsed = parse_float_graph(a)
    b_parsed = parse_float_graph(b)
    return ok_lab_color_from_components_internal(l_parsed, a_parsed, b_parsed)

def ok_lab_hist_lightness_quantile(hist, quantile) -> Graph:
    """OkLab Histogram Lightness Quantile

    Given an OkLab histogram and a quantile, returns the lightness value that corresponds to the quantile.

    Args:
        hist: Graph of OkLabHist
        quantile: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    hist_parsed = parse_graph(hist)
    quantile_parsed = parse_float_graph(quantile)
    return ok_lab_hist_lightness_quantile_internal(hist_parsed, quantile_parsed)

def ok_lab_to_r_g_b(ok_lab, color_profile) -> Graph:
    """OkLab to RGB

    Converts an OkLab color to an RGB color

    Args:
        OkLab: Graph of OkLabColor
        color profile: Graph of ColorProfile
        

    Returns:
        Graph: A graph node producing a RGBColor.
    """
    ok_lab_parsed = parse_graph(ok_lab)
    color_profile_parsed = parse_graph(color_profile)
    return ok_lab_to_r_g_b_internal(ok_lab_parsed, color_profile_parsed)

def or_(bool1, bool2) -> Graph:
    """Or

    Returns true if either inputs are true.

    Args:
        bool1: Graph of Bool
        bool2: Graph of Bool
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    bool1_parsed = parse_bool_graph(bool1)
    bool2_parsed = parse_bool_graph(bool2)
    return or_internal(bool1_parsed, bool2_parsed)

def painter_add_ellipse_with_render_style(painter, center, dimensions, rotation, render_style, instances) -> Graph:
    """Painter Add Ellipse with Render Style

    Adds an ellipse to the painter and draws it with the render style. Set some transforms on the ellipse as well.

    Args:
        painter: Graph of Painter
        center point of the ellipse: Graph of Point2f
        width (a) and height (b) of the ellipse: Graph of Vector2f
        rotation angle in radians: Graph of Float
        render style: Graph of RenderStyle
        instances: Graph of Transform2List
        

    Returns:
        Graph: A graph node producing a Painter.
    """
    painter_parsed = parse_graph(painter)
    center_parsed = parse_graph(center)
    dimensions_parsed = parse_graph(dimensions)
    rotation_parsed = parse_float_graph(rotation)
    render_style_parsed = parse_graph(render_style)
    instances_parsed = parse_graph(instances)
    return painter_add_ellipse_with_render_style_internal(painter_parsed, center_parsed, dimensions_parsed, rotation_parsed, render_style_parsed, instances_parsed)

def painter_add_path_with_render_style(painter, path, render_style, instances) -> Graph:
    """Painter Add Path with Render Style

    Adds a path to the painter and draws it with the render style. Set some transforms on the path as well.

    Args:
        painter: Graph of Painter
        path: Graph of Path
        render style: Graph of RenderStyle
        instances: Graph of Transform2List
        

    Returns:
        Graph: A graph node producing a Painter.
    """
    painter_parsed = parse_graph(painter)
    path_parsed = parse_graph(path)
    render_style_parsed = parse_graph(render_style)
    instances_parsed = parse_graph(instances)
    return painter_add_path_with_render_style_internal(painter_parsed, path_parsed, render_style_parsed, instances_parsed)

def painter_add_rectangle_with_render_style(painter, center, dimensions, rotation, render_style, instances) -> Graph:
    """Painter Add Rectangle with Render Style

    Adds a rectangle to the painter and draws it with the render style. Set some transforms on the rectangle as well.

    Args:
        painter: Graph of Painter
        center point of the rectangle: Graph of Point2f
        width and height of the rectangle: Graph of Vector2f
        rotation angle in radians: Graph of Float
        render style: Graph of RenderStyle
        instances: Graph of Transform2List
        

    Returns:
        Graph: A graph node producing a Painter.
    """
    painter_parsed = parse_graph(painter)
    center_parsed = parse_graph(center)
    dimensions_parsed = parse_graph(dimensions)
    rotation_parsed = parse_float_graph(rotation)
    render_style_parsed = parse_graph(render_style)
    instances_parsed = parse_graph(instances)
    return painter_add_rectangle_with_render_style_internal(painter_parsed, center_parsed, dimensions_parsed, rotation_parsed, render_style_parsed, instances_parsed)

def painter_new(color_profile) -> Graph:
    """Painter New

    Creates a new painter.

    Args:
        color profile: Graph of ColorProfile
        

    Returns:
        Graph: A graph node producing a Painter.
    """
    color_profile_parsed = parse_graph(color_profile)
    return painter_new_internal(color_profile_parsed)

def path_line_to_point(path, point) -> Graph:
    """Path Line to Point

    Moves the path from it's current point to another at another point with a line.

    Args:
        path: Graph of Path
        point: Graph of Point2f
        

    Returns:
        Graph: A graph node producing a Path.
    """
    path_parsed = parse_graph(path)
    point_parsed = parse_graph(point)
    return path_line_to_point_internal(path_parsed, point_parsed)

def path_move_to_point(path, point) -> Graph:
    """Path Move to Point

    Moves the path to a specified point without drawing anything.

    Args:
        path: Graph of Path
        point: Graph of Point2f
        

    Returns:
        Graph: A graph node producing a Path.
    """
    path_parsed = parse_graph(path)
    point_parsed = parse_graph(point)
    return path_move_to_point_internal(path_parsed, point_parsed)

def path_new() -> Graph:
    """Path New

    Creates a new empty path.

    Returns:
        Graph: A graph node producing a Path.
    """
    return path_new_internal()

def pi() -> Graph:
    """Pi

    Returns π as a float

    Returns:
        Graph: A graph node producing a Float.
    """
    return pi_internal()

def point2f_from_components(x, y) -> Graph:
    """Point 2 Float from Components

    Given an x and y creates a point

    Args:
        x: Graph of Float
        y: Graph of Float
        

    Returns:
        Graph: A graph node producing a Point2f.
    """
    x_parsed = parse_float_graph(x)
    y_parsed = parse_float_graph(y)
    return point2f_from_components_internal(x_parsed, y_parsed)

def r_g_b_a_color_add_to_dictionary(dictionary, key, value) -> Graph:
    """RGBA Color Add To Dictionary

    Adds a RGBA Color to a Dictionary

    Args:
        dictionary: Graph of Dictionary
        key: Graph of String
        value: Graph of RGBAColor
        

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    dictionary_parsed = parse_graph(dictionary)
    key_parsed = parse_string_graph(key)
    value_parsed = parse_graph(value)
    return r_g_b_a_color_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

def r_g_b_a_color_from_components(r, g, b, a) -> Graph:
    """RGBA Color from Components

    Given the r, g, b and a creates the color

    Args:
        red: Graph of Float
        green: Graph of Float
        blue: Graph of Float
        alpha: Graph of Float
        

    Returns:
        Graph: A graph node producing a RGBAColor.
    """
    r_parsed = parse_float_graph(r)
    g_parsed = parse_float_graph(g)
    b_parsed = parse_float_graph(b)
    a_parsed = parse_float_graph(a)
    return r_g_b_a_color_from_components_internal(r_parsed, g_parsed, b_parsed, a_parsed)

def r_g_b_a_color_passthrough(value) -> Graph:
    """RGBA Color Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of RGBAColor
        

    Returns:
        Graph: A graph node producing a RGBAColor.
    """
    value_parsed = parse_graph(value)
    return r_g_b_a_color_passthrough_internal(value_parsed)

def r_g_b_color_add_to_dictionary(dictionary, key, value) -> Graph:
    """RGB Color Add To Dictionary

    Adds a RGB Color to a Dictionary

    Args:
        dictionary: Graph of Dictionary
        key: Graph of String
        value: Graph of RGBColor
        

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    dictionary_parsed = parse_graph(dictionary)
    key_parsed = parse_string_graph(key)
    value_parsed = parse_graph(value)
    return r_g_b_color_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

def r_g_b_color_from_components(r, g, b) -> Graph:
    """RGB Color from Components

    Given the r, g and b creates the color

    Args:
        red: Graph of Float
        green: Graph of Float
        blue: Graph of Float
        

    Returns:
        Graph: A graph node producing a RGBColor.
    """
    r_parsed = parse_float_graph(r)
    g_parsed = parse_float_graph(g)
    b_parsed = parse_float_graph(b)
    return r_g_b_color_from_components_internal(r_parsed, g_parsed, b_parsed)

def r_g_b_color_passthrough(value) -> Graph:
    """RGB Color Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of RGBColor
        

    Returns:
        Graph: A graph node producing a RGBColor.
    """
    value_parsed = parse_graph(value)
    return r_g_b_color_passthrough_internal(value_parsed)

def r_g_b_to_ok_lab(rgb, color_profile) -> Graph:
    """RGB to OkLab

    Converts an RGB color to an OkLab color

    Args:
        RGB: Graph of RGBColor
        color profile: Graph of ColorProfile
        

    Returns:
        Graph: A graph node producing a OkLabColor.
    """
    rgb_parsed = parse_graph(rgb)
    color_profile_parsed = parse_graph(color_profile)
    return r_g_b_to_ok_lab_internal(rgb_parsed, color_profile_parsed)

def render_style_brush_and_fill(brush, fill) -> Graph:
    """Render Style Brush and Fill

    Creates a render style that will have a brush and a fill.

    Args:
        brush: Graph of Brush
        fill: Graph of Fill
        

    Returns:
        Graph: A graph node producing a RenderStyle.
    """
    brush_parsed = parse_graph(brush)
    fill_parsed = parse_graph(fill)
    return render_style_brush_and_fill_internal(brush_parsed, fill_parsed)

def render_style_brush_only(brush) -> Graph:
    """Render Style Brush Only

    Creates a render style that will only have a brush.

    Args:
        brush: Graph of Brush
        

    Returns:
        Graph: A graph node producing a RenderStyle.
    """
    brush_parsed = parse_graph(brush)
    return render_style_brush_only_internal(brush_parsed)

def render_style_fill_only(fill) -> Graph:
    """Render Style Fill Only

    Creates a render style that will only have a fill.

    Args:
        fill: Graph of Fill
        

    Returns:
        Graph: A graph node producing a RenderStyle.
    """
    fill_parsed = parse_graph(fill)
    return render_style_fill_only_internal(fill_parsed)

def sequence_adjust_speed(sequence, factor) -> Graph:
    """Sequence Adjust Speed

    Adjusts the speed of a sequence by a speed factor.

    Args:
        sequence: Graph of Sequence
        factor: Graph of Float
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    sequence_parsed = parse_graph(sequence)
    factor_parsed = parse_float_graph(factor)
    return sequence_adjust_speed_internal(sequence_parsed, factor_parsed)

def sequence_composition_at_time(sequence, time) -> Graph:
    """Sequence Composition at Time

    Extracts an composition from a sequence at a particular time

    Args:
        sequence: Graph of Sequence
        time: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    sequence_parsed = parse_graph(sequence)
    time_parsed = parse_float_graph(time)
    return sequence_composition_at_time_internal(sequence_parsed, time_parsed)

def sequence_concatenate(sequence_1, sequence_2) -> Graph:
    """Sequence Concatenate

    Given two sequences, combines them into one by playing the first one and then the second one.

    Args:
        sequence 1: Graph of Sequence
        sequence 2: Graph of Sequence
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    sequence_1_parsed = parse_graph(sequence_1)
    sequence_2_parsed = parse_graph(sequence_2)
    return sequence_concatenate_internal(sequence_1_parsed, sequence_2_parsed)

def sequence_duration(sequence) -> Graph:
    """Sequence Duration

    Gets the duration from a sequence

    Args:
        sequence: Graph of Sequence
        

    Returns:
        Graph: A graph node producing a Float.
    """
    sequence_parsed = parse_graph(sequence)
    return sequence_duration_internal(sequence_parsed)

def sequence_from_composition_and_duration(composition, duration) -> Graph:
    """Sequence from Composition and Duration

    Give a Composition and a Duration. Returns a Sequence.

    Args:
        composition: Graph of Composition
        duration: Graph of Float
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    composition_parsed = parse_graph(composition)
    duration_parsed = parse_float_graph(duration)
    return sequence_from_composition_and_duration_internal(composition_parsed, duration_parsed)

def sequence_from_u_r_l(url) -> Graph:
    """Sequence from URL

    Creates a sequence from URL

    Args:
        url: Graph of String
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    url_parsed = parse_string_graph(url)
    return sequence_from_u_r_l_internal(url_parsed)

def sequence_graph(duration, time, frame) -> Graph:
    """Sequence Graph

    Creates a sequence that runs the graph to get the duration and the frame for each time.

    Args:
        duration: Graph of Float
        time: Graph of Float
        frame: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    duration_parsed = parse_float_graph(duration)
    time_parsed = parse_float_graph(time)
    frame_parsed = parse_graph(frame)
    return sequence_graph_internal(duration_parsed, time_parsed, frame_parsed)

def sequence_grayscale(sequence) -> Graph:
    """Sequence Grayscale

    Creates a sequence that converts the video to grayscale

    Args:
        sequence: Graph of Sequence
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    sequence_parsed = parse_graph(sequence)
    return sequence_grayscale_internal(sequence_parsed)

def sequence_passthrough(value) -> Graph:
    """Sequence Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Sequence
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    value_parsed = parse_graph(value)
    return sequence_passthrough_internal(value_parsed)

def sequence_reverse(sequence) -> Graph:
    """Sequence Reverse

    Given a sequence. Reverses it.

    Args:
        sequence: Graph of Sequence
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    sequence_parsed = parse_graph(sequence)
    return sequence_reverse_internal(sequence_parsed)

def sequence_to_mp4(sequence, frame_rate) -> Graph:
    """Sequence To MP4

    Given a sequence. Converts it to MP4 return a local file to where that MP4 is stored.

    Args:
        sequence: Graph of Sequence
        frame rate: Graph of Int
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    sequence_parsed = parse_graph(sequence)
    frame_rate_parsed = parse_int_graph(frame_rate)
    return sequence_to_mp4_internal(sequence_parsed, frame_rate_parsed)

def sequence_trim_back(sequence, amount) -> Graph:
    """Sequence Trim Back

    Given a sequence. Trims from the back.

    Args:
        sequence: Graph of Sequence
        amount: Graph of Float
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    sequence_parsed = parse_graph(sequence)
    amount_parsed = parse_float_graph(amount)
    return sequence_trim_back_internal(sequence_parsed, amount_parsed)

def sequence_trim_front(sequence, amount) -> Graph:
    """Sequence Trim Front

    Given a sequence. Trims from the front.

    Args:
        sequence: Graph of Sequence
        amount: Graph of Float
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    sequence_parsed = parse_graph(sequence)
    amount_parsed = parse_float_graph(amount)
    return sequence_trim_front_internal(sequence_parsed, amount_parsed)

def string_if(bool, input_1, input_2) -> Graph:
    """String If

    If the boolean is true returns input 1, otherwise input 2. Type: String

    Args:
        bool: Graph of Bool
        input 1: Graph of String
        input 2: Graph of String
        

    Returns:
        Graph: A graph node producing a String.
    """
    bool_parsed = parse_bool_graph(bool)
    input_1_parsed = parse_string_graph(input_1)
    input_2_parsed = parse_string_graph(input_2)
    return string_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

def transform2_identity() -> Graph:
    """Transform 2D Identity

    Creates a 2D transform that is the identity transform.

    Returns:
        Graph: A graph node producing a Transform2.
    """
    return transform2_identity_internal()

def transform2_if(bool, input_1, input_2) -> Graph:
    """Transform 2D If

    If the boolean is true returns input 1, otherwise input 2. Type: Transform2

    Args:
        bool: Graph of Bool
        input 1: Graph of Transform2
        input 2: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Transform2.
    """
    bool_parsed = parse_bool_graph(bool)
    input_1_parsed = parse_graph(input_1)
    input_2_parsed = parse_graph(input_2)
    return transform2_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

def transform2_rotate(transform, angle) -> Graph:
    """Transform 2D Rotate

    Applies a rotation to a 2D transform. Rotation is in radians.

    Args:
        transform: Graph of Transform2
        angle in radians: Graph of Float
        

    Returns:
        Graph: A graph node producing a Transform2.
    """
    transform_parsed = parse_graph(transform)
    angle_parsed = parse_float_graph(angle)
    return transform2_rotate_internal(transform_parsed, angle_parsed)

def transform2_scale(transform, scale) -> Graph:
    """Transform 2D Scale

    Applies a scale to a 2D transform.

    Args:
        transform: Graph of Transform2
        scale: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Transform2.
    """
    transform_parsed = parse_graph(transform)
    scale_parsed = parse_graph(scale)
    return transform2_scale_internal(transform_parsed, scale_parsed)

def transform2_to_list(item) -> Graph:
    """Transform 2D to List

    Converts Transform 2D to a single item list

    Args:
        item: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Transform2List.
    """
    item_parsed = parse_graph(item)
    return transform2_to_list_internal(item_parsed)

def transform2_translation(transform, translation) -> Graph:
    """Transform 2D Translation

    Applies a translation to a 2D transform.

    Args:
        transform: Graph of Transform2
        translation: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Transform2.
    """
    transform_parsed = parse_graph(transform)
    translation_parsed = parse_graph(translation)
    return transform2_translation_internal(transform_parsed, translation_parsed)

def upload_byte_list(bytes, url, content_type) -> Graph:
    """Upload Byte List

    Given bytes and a URL. Performs a PUT request and uploads the bytes

    Args:
        bytes: Graph of ByteList
        url: Graph of String
        content type: Graph of String
        

    Returns:
        Graph: A graph node producing a Void.
    """
    bytes_parsed = parse_graph(bytes)
    url_parsed = parse_string_graph(url)
    content_type_parsed = parse_string_graph(content_type)
    return upload_byte_list_internal(bytes_parsed, url_parsed, content_type_parsed)

def upload_file_path(path, url, content_type) -> Graph:
    """Upload File Path

    Reads a file from a local path on disk and uploads its contents to a URL via PUT request

    Args:
        local file path to read: Graph of String
        url: Graph of String
        content type: Graph of String
        

    Returns:
        Graph: A graph node producing a Void.
    """
    path_parsed = parse_string_graph(path)
    url_parsed = parse_string_graph(url)
    content_type_parsed = parse_string_graph(content_type)
    return upload_file_path_internal(path_parsed, url_parsed, content_type_parsed)

def vector2_int_to_vector2_float(vector) -> Graph:
    """Vector 2 Int to Vector 2 Float

    Given a Vector 2 Int. Creates a Vector 2 Float.

    Args:
        vector: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    vector_parsed = parse_graph(vector)
    return vector2_int_to_vector2_float_internal(vector_parsed)

def vector2f_add(lhs, rhs) -> Graph:
    """Vector 2 Float Add

    Add two Vector 2s of Floats

    Args:
        The vector on the left hand side of the add: Graph of Vector2f
        The vector on the right hand side of the add: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    lhs_parsed = parse_graph(lhs)
    rhs_parsed = parse_graph(rhs)
    return vector2f_add_internal(lhs_parsed, rhs_parsed)

def vector2f_add_to_dictionary(dictionary, key, value) -> Graph:
    """Vector 2 Float Add To Dictionary

    Adds a Vector 2 Float to a Dictionary

    Args:
        dictionary: Graph of Dictionary
        key: Graph of String
        value: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    dictionary_parsed = parse_graph(dictionary)
    key_parsed = parse_string_graph(key)
    value_parsed = parse_graph(value)
    return vector2f_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

def vector2f_from_components(x, y) -> Graph:
    """Vector 2 Float from Components

    Given an x and y creates a vector.

    Args:
        x: Graph of Float
        y: Graph of Float
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    x_parsed = parse_float_graph(x)
    y_parsed = parse_float_graph(y)
    return vector2f_from_components_internal(x_parsed, y_parsed)

def vector2f_normalize(vector) -> Graph:
    """Vector 2 Float Normalize

    Normalizes a Vector. Converting it's length to 1.

    Args:
        Vector: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    vector_parsed = parse_graph(vector)
    return vector2f_normalize_internal(vector_parsed)

def vector2f_passthrough(value) -> Graph:
    """Vector 2 Float Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    value_parsed = parse_graph(value)
    return vector2f_passthrough_internal(value_parsed)

def vector2f_scalar_multiply(vector, scalar) -> Graph:
    """Vector 2 Float Scalar Multiply

    Multiplies each element of the Vector as a scalar

    Args:
        Vector: Graph of Vector2f
        Scalar: Graph of Float
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    vector_parsed = parse_graph(vector)
    scalar_parsed = parse_float_graph(scalar)
    return vector2f_scalar_multiply_internal(vector_parsed, scalar_parsed)

def vector2f_x(vector) -> Graph:
    """Vector 2 Float get X

    Retrieves the X component of a Vector 2 Float.

    Args:
        vector: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return vector2f_x_internal(vector_parsed)

def vector2f_y(vector) -> Graph:
    """Vector 2 Float get Y

    Retrieves the Y component of a Vector 2 Float.

    Args:
        vector: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return vector2f_y_internal(vector_parsed)

def vector2i_add(lhs, rhs) -> Graph:
    """Vector 2 Int Add

    Add two Vector 2s of Ints

    Args:
        The vector on the left hand side of the add: Graph of Vector2i
        The vector on the right hand side of the add: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Vector2i.
    """
    lhs_parsed = parse_graph(lhs)
    rhs_parsed = parse_graph(rhs)
    return vector2i_add_internal(lhs_parsed, rhs_parsed)

def vector2i_add_to_dictionary(dictionary, key, value) -> Graph:
    """Vector 2 Int Add To Dictionary

    Adds a Vector 2 Int to a Dictionary

    Args:
        dictionary: Graph of Dictionary
        key: Graph of String
        value: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    dictionary_parsed = parse_graph(dictionary)
    key_parsed = parse_string_graph(key)
    value_parsed = parse_graph(value)
    return vector2i_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

def vector2i_from_components(x, y) -> Graph:
    """Vector 2 Int from Components

    Given an x and y creates a vector.

    Args:
        x: Graph of Int
        y: Graph of Int
        

    Returns:
        Graph: A graph node producing a Vector2i.
    """
    x_parsed = parse_int_graph(x)
    y_parsed = parse_int_graph(y)
    return vector2i_from_components_internal(x_parsed, y_parsed)

def vector2i_passthrough(value) -> Graph:
    """Vector 2 Int Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Vector2i.
    """
    value_parsed = parse_graph(value)
    return vector2i_passthrough_internal(value_parsed)

def vector2i_to_vector2f(vector) -> Graph:
    """Vector 2 Int to Vector 2 Float

    Given a Vector 2 Int. Creates a Vector 2 Float.

    Args:
        vector: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    vector_parsed = parse_graph(vector)
    return vector2i_to_vector2f_internal(vector_parsed)

def vector2i_x(vector) -> Graph:
    """Vector 2 Int get X

    Retrieves the X component of a Vector 2 Int.

    Args:
        vector: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Int.
    """
    vector_parsed = parse_graph(vector)
    return vector2i_x_internal(vector_parsed)

def vector2i_y(vector) -> Graph:
    """Vector 2 Int get Y

    Retrieves the Y component of a Vector 2 Int.

    Args:
        vector: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Int.
    """
    vector_parsed = parse_graph(vector)
    return vector2i_y_internal(vector_parsed)

def vector3f_add(lhs, rhs) -> Graph:
    """Vector 3 Float Add

    Add two Vector 3s of Floats

    Args:
        The vector on the left hand side of the add: Graph of Vector3f
        The vector on the right hand side of the add: Graph of Vector3f
        

    Returns:
        Graph: A graph node producing a Vector3f.
    """
    lhs_parsed = parse_graph(lhs)
    rhs_parsed = parse_graph(rhs)
    return vector3f_add_internal(lhs_parsed, rhs_parsed)

def vector3f_from_components(x, y, z) -> Graph:
    """Vector 3 Float from Components

    Given an x, y and z creates a vector floats.

    Args:
        x: Graph of Float
        y: Graph of Float
        z: Graph of Float
        

    Returns:
        Graph: A graph node producing a Vector3f.
    """
    x_parsed = parse_float_graph(x)
    y_parsed = parse_float_graph(y)
    z_parsed = parse_float_graph(z)
    return vector3f_from_components_internal(x_parsed, y_parsed, z_parsed)

def vector3f_normalize(vector) -> Graph:
    """Vector 3 Normalize

    Normalizes a Vector 3 Float. Converting it's length to 1.

    Args:
        Vector: Graph of Vector3f
        

    Returns:
        Graph: A graph node producing a Vector3f.
    """
    vector_parsed = parse_graph(vector)
    return vector3f_normalize_internal(vector_parsed)

def vector3f_x(vector) -> Graph:
    """Vector 3D Float X

    Gets the value in the x component for the provided vector

    Args:
        vector: Graph of Vector3f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return vector3f_x_internal(vector_parsed)

def vector3f_y(vector) -> Graph:
    """Vector 3D Y Float

    Gets the value in the y component for the provided vector

    Args:
        vector: Graph of Vector3f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return vector3f_y_internal(vector_parsed)

def vector3f_z(vector) -> Graph:
    """Vector 3D Float Z

    Gets the value in the z component for the provided vector

    Args:
        vector: Graph of Vector3f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return vector3f_z_internal(vector_parsed)

def xor(bool1, bool2) -> Graph:
    """Exclusive Or

    Returns true if either the inputs are true. But false if both are true.

    Args:
        the first bool: Graph of Bool
        The second bool: Graph of Bool
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    bool1_parsed = parse_bool_graph(bool1)
    bool2_parsed = parse_bool_graph(bool2)
    return xor_internal(bool1_parsed, bool2_parsed)


__all__ = [
    # Core classes
    "Context", "Graph", "Project", "Type",
    "TypeDefinition", "NodeDefinition", "NodeDefinitionInput", "ImageRecipe",
    # Constant functions
    "int_constant", "float_constant", "string_constant", "bool_constant",
    # Node functions
    "abs",
    "and_",
    "bool_add_to_dictionary",
    "bool_if",
    "bounds2f_from_x_y_width_height",
    "bounds2i_from_x_y_width_height",
    "brush_solid",
    "byte_list_from_u_r_l",
    "color_profile_b_t709",
    "color_profile_ok_lab_a",
    "color_profile_p3",
    "color_profile_p_n_g_s_r_g_b",
    "color_profile_s_r_g_b",
    "composition_absolute_value",
    "composition_bilinear_interpolation",
    "composition_blend_add",
    "composition_blend_alpha",
    "composition_blend_max",
    "composition_blend_min",
    "composition_blend_multiply",
    "composition_blend_stencil",
    "composition_blend_subtract",
    "composition_blend_with_factor",
    "composition_box_blur",
    "composition_box_blur_with_ok_lab",
    "composition_brightness_adjust",
    "composition_chroma_offset",
    "composition_color_convert",
    "composition_color_invert",
    "composition_color_profile",
    "composition_color_rect",
    "composition_color_threshold",
    "composition_contrast_adjustment",
    "composition_convolution",
    "composition_crop",
    "composition_custom_transformer_shader",
    "composition_flip_horizontal",
    "composition_flip_vertical",
    "composition_from_asset",
    "composition_from_image",
    "composition_gaussian_blur",
    "composition_gaussian_blur_with_ok_lab",
    "composition_grayscale",
    "composition_if",
    "composition_l_curve",
    "composition_linear_transform",
    "composition_monet_women_with_parasol",
    "composition_morphological_max",
    "composition_morphological_min",
    "composition_painter",
    "composition_passthrough",
    "composition_pixelate",
    "composition_r_g_b_curve",
    "composition_render_to_image",
    "composition_rotate180",
    "composition_rotate90_clockwise",
    "composition_rotate90_counter_clockwise",
    "composition_s_a_m3_image",
    "composition_saturation_adjust",
    "composition_scale_nearest_neighbor",
    "composition_segment",
    "composition_sharpen",
    "composition_size",
    "composition_sobel_edge_detection",
    "composition_swirl",
    "composition_target_white_kelvin",
    "composition_to_ok_lab_hist",
    "composition_vignette",
    "composition_zoom_blur",
    "curve_evaluate",
    "curve_gamma",
    "curve_identity",
    "curve_pivoted_sigmoid",
    "curve_s_curve",
    "dictionary_create",
    "file_convert_image_to_bmp",
    "file_convert_image_to_heic",
    "file_convert_image_to_jpeg",
    "file_convert_image_to_png",
    "file_convert_image_to_tiff",
    "file_convert_image_to_web_p",
    "file_convert_video_to_animated_web_p",
    "file_convert_video_to_gif",
    "file_convert_video_to_m_p4",
    "file_convert_video_to_web_m",
    "fill_custom",
    "fill_solid",
    "float_add",
    "float_add_to_dictionary",
    "float_cos",
    "float_divide",
    "float_equals",
    "float_greater_than",
    "float_greater_than_or_equal",
    "float_if",
    "float_lerp",
    "float_less_than",
    "float_less_than_or_equal",
    "float_max",
    "float_min",
    "float_multiply",
    "float_passthrough",
    "float_pow",
    "float_round_to_int",
    "float_sin",
    "float_square_root",
    "float_squared",
    "float_subtract",
    "image_from_byte_list",
    "image_to_byte_list",
    "int_abs",
    "int_add",
    "int_add_to_dictionary",
    "int_equals",
    "int_greater_than",
    "int_greater_than_or_equal",
    "int_if",
    "int_less_than",
    "int_less_than_or_equal",
    "int_max",
    "int_min",
    "int_multiply",
    "int_passthrough",
    "int_subtract",
    "int_to_float",
    "monet_network_download_u_r_l_from_asset_i_d",
    "not_",
    "null_value",
    "ok_lab_color_from_components",
    "ok_lab_hist_lightness_quantile",
    "ok_lab_to_r_g_b",
    "or_",
    "painter_add_ellipse_with_render_style",
    "painter_add_path_with_render_style",
    "painter_add_rectangle_with_render_style",
    "painter_new",
    "path_line_to_point",
    "path_move_to_point",
    "path_new",
    "pi",
    "point2f_from_components",
    "r_g_b_a_color_add_to_dictionary",
    "r_g_b_a_color_from_components",
    "r_g_b_a_color_passthrough",
    "r_g_b_color_add_to_dictionary",
    "r_g_b_color_from_components",
    "r_g_b_color_passthrough",
    "r_g_b_to_ok_lab",
    "render_style_brush_and_fill",
    "render_style_brush_only",
    "render_style_fill_only",
    "sequence_adjust_speed",
    "sequence_composition_at_time",
    "sequence_concatenate",
    "sequence_duration",
    "sequence_from_composition_and_duration",
    "sequence_from_u_r_l",
    "sequence_graph",
    "sequence_grayscale",
    "sequence_passthrough",
    "sequence_reverse",
    "sequence_to_mp4",
    "sequence_trim_back",
    "sequence_trim_front",
    "string_if",
    "transform2_identity",
    "transform2_if",
    "transform2_rotate",
    "transform2_scale",
    "transform2_to_list",
    "transform2_translation",
    "upload_byte_list",
    "upload_file_path",
    "vector2_int_to_vector2_float",
    "vector2f_add",
    "vector2f_add_to_dictionary",
    "vector2f_from_components",
    "vector2f_normalize",
    "vector2f_passthrough",
    "vector2f_scalar_multiply",
    "vector2f_x",
    "vector2f_y",
    "vector2i_add",
    "vector2i_add_to_dictionary",
    "vector2i_from_components",
    "vector2i_passthrough",
    "vector2i_to_vector2f",
    "vector2i_x",
    "vector2i_y",
    "vector3f_add",
    "vector3f_from_components",
    "vector3f_normalize",
    "vector3f_x",
    "vector3f_y",
    "vector3f_z",
    "xor",
    ]