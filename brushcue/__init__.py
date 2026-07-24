# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: e13a5d2cd9baafa1b062103c96d6eb53d5e551bb8a9356015e71a46b30b0ba80
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

from . import _py as _internal
from ._py import (
    Bounds,
    Context,
    Graph,
    IDMapper,
    ImageRecipe,
    MovieRecipe,
    NodeDefinition,
    NodeDefinitionInput,
    Project,
    Type,
    TypeDefinition,
    all_tools,
    mcp_prompt,
)
from .input_parsers import (
    parse_bool_graph,
    parse_composition_graph,
    parse_float_graph,
    parse_graph,
    parse_int_graph,
    parse_string_graph,
)

def load_composition(value) -> Graph:
    return parse_composition_graph(value)

def byte_list_constant(value) -> Graph:
    return _internal.byte_list_constant_internal(value)

def point2i_list_constant(value) -> Graph:
    return _internal.point2i_list_constant_internal(value)

def int_constant(value) -> Graph:
    return _internal.int_constant_internal(int(value))

def float_constant(value) -> Graph:
    return _internal.float_constant_internal(float(value))

def string_constant(value: str) -> Graph:
    return _internal.string_constant_internal(value)

def bool_constant(value: bool) -> Graph:
    return _internal.bool_constant_internal(value)

def vector_2i_constant(x: int, y: int) -> Graph:
    return _internal.vector2i_constant_internal(x, y)

def vector2f_constant(x: float, y: float) -> Graph:
    return _internal.vector2f_constant_internal(x, y)


def abs(number) -> Graph:
    """Absolute Value

    Returns the absolute value of a float

    Args:
        number: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    number_parsed = parse_float_graph(number)
    return _internal.abs_internal(number_parsed)

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
    return _internal.and_internal(bool1_parsed, bool2_parsed)

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
    return _internal.bool_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

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
    return _internal.bool_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

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
    return _internal.bounds2f_from_x_y_width_height_internal(x_parsed, y_parsed, width_parsed, height_parsed)

def bounds2f_height(bounds) -> Graph:
    """Bounds2f Height

    Gets the height of the bounds.

    Args:
        bounds: Graph of Bounds2f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    bounds_parsed = parse_graph(bounds)
    return _internal.bounds2f_height_internal(bounds_parsed)

def bounds2f_min_x(bounds) -> Graph:
    """Bounds2f Min X

    Gets the minimum X coordinate (left edge) of the bounds.

    Args:
        bounds: Graph of Bounds2f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    bounds_parsed = parse_graph(bounds)
    return _internal.bounds2f_min_x_internal(bounds_parsed)

def bounds2f_min_y(bounds) -> Graph:
    """Bounds2f Min Y

    Gets the minimum Y coordinate (top edge) of the bounds.

    Args:
        bounds: Graph of Bounds2f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    bounds_parsed = parse_graph(bounds)
    return _internal.bounds2f_min_y_internal(bounds_parsed)

def bounds2f_width(bounds) -> Graph:
    """Bounds2f Width

    Gets the width of the bounds.

    Args:
        bounds: Graph of Bounds2f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    bounds_parsed = parse_graph(bounds)
    return _internal.bounds2f_width_internal(bounds_parsed)

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
    return _internal.bounds2i_from_x_y_width_height_internal(x_parsed, y_parsed, width_parsed, height_parsed)

def brush_solid(color, radius) -> Graph:
    """Brush Solid

    Creates a brush with a color and radius. Will stroke with the solid color.

    Args:
        color: Graph of ProfiledColor
        radius: Graph of Float
        

    Returns:
        Graph: A graph node producing a Brush.
    """
    color_parsed = parse_graph(color)
    radius_parsed = parse_float_graph(radius)
    return _internal.brush_solid_internal(color_parsed, radius_parsed)

def byte_list_from_u_r_l(url) -> Graph:
    """Byte List from URL

    Given a URL. Performs a GET request and downloads the result as bytes.

    Args:
        url: Graph of String
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    url_parsed = parse_string_graph(url)
    return _internal.byte_list_from_u_r_l_internal(url_parsed)

def color_profile_a_c_e_scg() -> Graph:
    """Color Profile ACEScg

    Creates an ACEScg Color Profile

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return _internal.color_profile_a_c_e_scg_internal()

def color_profile_b_t709() -> Graph:
    """Color Profile BT.709

    Creates a BT.709 Color Profile

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return _internal.color_profile_b_t709_internal()

def color_profile_ok_lab_a() -> Graph:
    """Color Profile OkLabA

    Creates an OkLabA color profile. OkLab with also an alpha component.

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return _internal.color_profile_ok_lab_a_internal()

def color_profile_p3() -> Graph:
    """Color Profile P3

    Creates a P3 Color Profile

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return _internal.color_profile_p3_internal()

def color_profile_p_n_g_s_r_g_b() -> Graph:
    """Color Profile PNG sRGB

    Creates a color profile that is the same one as PNG sRGB.

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return _internal.color_profile_p_n_g_s_r_g_b_internal()

def color_profile_s_r_g_b() -> Graph:
    """Color Profile sRGB

    Creates an sRGB Color Profile

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return _internal.color_profile_s_r_g_b_internal()

def color_profile_s_r_g_b_linear() -> Graph:
    """Color Profile Linear sRGB

    Creates a linear sRGB Color Profile

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return _internal.color_profile_s_r_g_b_linear_internal()

def color_profile_x_y_z() -> Graph:
    """Color Profile XYZ

    Creates an XYZ Color Profile

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    return _internal.color_profile_x_y_z_internal()

def color_representation_a_c_e_scg() -> Graph:
    """Color Representation ACEScg

    Creates a Color Representation using the ACEScg Color Profile with linear light, straight alpha pixel values.

    Returns:
        Graph: A graph node producing a ColorRepresentation.
    """
    return _internal.color_representation_a_c_e_scg_internal()

def color_representation_from_color_profile_and_pixel_encoding(color_profile, pixel_encoding) -> Graph:
    """Color Representation From Color Profile And Pixel Encoding

    Creates a Color Representation by pairing a Color Profile with a Pixel Encoding.

    Args:
        color profile: Graph of ColorProfile
        pixel encoding: Graph of PixelEncoding
        

    Returns:
        Graph: A graph node producing a ColorRepresentation.
    """
    color_profile_parsed = parse_graph(color_profile)
    pixel_encoding_parsed = parse_graph(pixel_encoding)
    return _internal.color_representation_from_color_profile_and_pixel_encoding_internal(color_profile_parsed, pixel_encoding_parsed)

def color_representation_ok_lab_a() -> Graph:
    """Color Representation OkLabA

    Creates a Color Representation using the OkLabA Color Profile with encoded pixel values.

    Returns:
        Graph: A graph node producing a ColorRepresentation.
    """
    return _internal.color_representation_ok_lab_a_internal()

def color_representation_profile(color_representation) -> Graph:
    """Color Profile of a Color Representation

    Given a color representation. Extracts the color profile of that color representation

    Args:
        color representation: Graph of ColorRepresentation
        

    Returns:
        Graph: A graph node producing a ColorProfile.
    """
    color_representation_parsed = parse_graph(color_representation)
    return _internal.color_representation_profile_internal(color_representation_parsed)

def color_representation_r_g_b_b_t2020() -> Graph:
    """Color Representation BT.2020

    Creates a Color Representation using the BT.2020 Color Profile with gamma-encoded pixel values.

    Returns:
        Graph: A graph node producing a ColorRepresentation.
    """
    return _internal.color_representation_r_g_b_b_t2020_internal()

def color_representation_s_r_g_b() -> Graph:
    """Color Representation sRGB

    Creates a Color Representation using the sRGB Color Profile with gamma-encoded pixel values.

    Returns:
        Graph: A graph node producing a ColorRepresentation.
    """
    return _internal.color_representation_s_r_g_b_internal()

def color_representation_s_r_g_b_linear() -> Graph:
    """Color Representation Linear sRGB

    Creates a Color Representation using the linear sRGB Color Profile with linear light, straight alpha pixel values.

    Returns:
        Graph: A graph node producing a ColorRepresentation.
    """
    return _internal.color_representation_s_r_g_b_linear_internal()

def color_representation_x_y_z_a() -> Graph:
    """Color Representation XYZA

    Creates a Color Representation using the XYZA Color Profile with linear light, straight alpha pixel values.

    Returns:
        Graph: A graph node producing a ColorRepresentation.
    """
    return _internal.color_representation_x_y_z_a_internal()

def composition_absolute_value(image) -> Graph:
    """Composition Absolute Value

    Takes the absolute value of all the pixels in the image.

    Args:
        image: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    image_parsed = parse_graph(image)
    return _internal.composition_absolute_value_internal(image_parsed)

def composition_blend_add(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Add

    Adds the foreground and background images together using additive blending.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return _internal.composition_blend_add_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_alpha(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Alpha

    Blends between the foreground and background using the alpha component of the foreground. 1 is foreground. 0 is background.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return _internal.composition_blend_alpha_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_max(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Max

    Blends the foreground and background images using maximum value blending.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return _internal.composition_blend_max_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_min(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Min

    Blends the foreground and background images using minimum blending, taking the minimum value for each pixel.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return _internal.composition_blend_min_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_multiply(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Multiply

    Multiplies the foreground and background images together using multiply blending.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return _internal.composition_blend_multiply_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_stencil(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Stencil

    Blends the foreground and background images using stencil blending. When the foreground is over the background, the foreground's alpha and the background's r, g and b are used.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return _internal.composition_blend_stencil_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_blend_subtract(foreground, background, foreground_transform) -> Graph:
    """Composition Blend Subtract

    Subtracts the foreground image from the background image using subtractive blending.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return _internal.composition_blend_subtract_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_bloom(composition, threshold, sigma, intensity) -> Graph:
    """Composition Bloom

    Adds a soft bloom glow by blurring the image's bright areas and additively blending them back over the original. Threshold selects bright areas (OkLab lightness), sigma controls glow spread, intensity scales the glow strength.

    Args:
        composition: Graph of Composition
        threshold: Graph of Float
        sigma: Graph of Float
        intensity: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    threshold_parsed = parse_float_graph(threshold)
    sigma_parsed = parse_float_graph(sigma)
    intensity_parsed = parse_float_graph(intensity)
    return _internal.composition_bloom_internal(composition_parsed, threshold_parsed, sigma_parsed, intensity_parsed)

def composition_bounds(composition) -> Graph:
    """Composition Bounds

    Computes the bounding box of a composition.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Bounds2f.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_bounds_internal(composition_parsed)

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
    return _internal.composition_box_blur_internal(composition_parsed, dimension_parsed)

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
    return _internal.composition_brightness_adjust_internal(composition_parsed, scale_parsed)

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
    return _internal.composition_chroma_offset_internal(composition_parsed, offset_parsed)

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
    return _internal.composition_color_convert_internal(composition_parsed, color_profile_parsed)

def composition_color_invert(composition) -> Graph:
    """Composition Color Invert

    Applies a color invert operation to a composition. Taking 1 and subtracting each RGB operation against it. Works in linear color.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_color_invert_internal(composition_parsed)

def composition_color_representation(composition) -> Graph:
    """Composition Color Representation

    Gets the color representation associated with a Composition

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a ColorRepresentation.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_color_representation_internal(composition_parsed)

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
    return _internal.composition_color_threshold_internal(composition_parsed, threshold_parsed)

def composition_color_transformer_shader(composition, function_body, helpers, input_color_representation, output_color_representation, inputs) -> Graph:
    """Composition Color Transformer Shader

    Defines a custom shader that takes an input color and then transforms that color to an output color.

    Args:
        composition: Graph of Composition
        function body: Graph of String
        helpers: Graph of String
        input color representation: Graph of ColorRepresentation
        output color representation: Graph of ColorRepresentation
        inputs: Graph of Dictionary
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    function_body_parsed = parse_string_graph(function_body)
    helpers_parsed = parse_string_graph(helpers)
    input_color_representation_parsed = parse_graph(input_color_representation)
    output_color_representation_parsed = parse_graph(output_color_representation)
    inputs_parsed = parse_graph(inputs)
    return _internal.composition_color_transformer_shader_internal(composition_parsed, function_body_parsed, helpers_parsed, input_color_representation_parsed, output_color_representation_parsed, inputs_parsed)

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
    return _internal.composition_contrast_adjustment_internal(composition_parsed, contrast_parsed)

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
    return _internal.composition_convolution_internal(composition_parsed, kernel_parsed, kernel_width_parsed, kernel_height_parsed)

def composition_crop(composition, rect) -> Graph:
    """Composition Crop

    Applies a crop to a Composition

    Args:
        composition: Graph of Composition
        rect: Graph of Bounds2f
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    rect_parsed = parse_graph(rect)
    return _internal.composition_crop_internal(composition_parsed, rect_parsed)

def composition_duotone(composition, threshold, color_1, color_2) -> Graph:
    """Composition Duotone

    Creates a duotone effect. Colors below the threshold will be color 1, colors above will be color 2.

    Args:
        composition: Graph of Composition
        threshold: Graph of Float
        color 1: Graph of ProfiledColor
        color 2: Graph of ProfiledColor
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    threshold_parsed = parse_float_graph(threshold)
    color_1_parsed = parse_graph(color_1)
    color_2_parsed = parse_graph(color_2)
    return _internal.composition_duotone_internal(composition_parsed, threshold_parsed, color_1_parsed, color_2_parsed)

def composition_film_grain(composition, grain_strength, fine_grain_frequency, fine_weight, medium_grain_frequency, medium_weight, high_grain_frequency, high_weight) -> Graph:
    """Composition Film Grain

    adds multi-octave value-noise film grain in OkLabA - grain_strength controls the overall intensity, and the fine/medium/high frequency and weight pairs control the size and contribution of each grain octave.

    Args:
        composition: Graph of Composition
        grain strength: Graph of Float
        fine grain frequency: Graph of Float
        fine weight: Graph of Float
        medium grain frequency: Graph of Float
        medium weight: Graph of Float
        high grain frequency: Graph of Float
        high weight: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    grain_strength_parsed = parse_float_graph(grain_strength)
    fine_grain_frequency_parsed = parse_float_graph(fine_grain_frequency)
    fine_weight_parsed = parse_float_graph(fine_weight)
    medium_grain_frequency_parsed = parse_float_graph(medium_grain_frequency)
    medium_weight_parsed = parse_float_graph(medium_weight)
    high_grain_frequency_parsed = parse_float_graph(high_grain_frequency)
    high_weight_parsed = parse_float_graph(high_weight)
    return _internal.composition_film_grain_internal(composition_parsed, grain_strength_parsed, fine_grain_frequency_parsed, fine_weight_parsed, medium_grain_frequency_parsed, medium_weight_parsed, high_grain_frequency_parsed, high_weight_parsed)

def composition_flip_horizontal(composition) -> Graph:
    """Composition Flip Horizontal

    Flips the image along the horizontal axis

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_flip_horizontal_internal(composition_parsed)

def composition_flip_vertical(composition) -> Graph:
    """Composition Flip Vertical

    Flips the image vertically

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_flip_vertical_internal(composition_parsed)

def composition_from_asset(asset_id) -> Graph:
    """Composition from Asset

    Creates a composition from an asset in your catalog.

    Args:
        asset id: Graph of Int
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    asset_id_parsed = parse_int_graph(asset_id)
    return _internal.composition_from_asset_internal(asset_id_parsed)

def composition_from_image(image) -> Graph:
    """Composition from Image

    Creates an composition out of an image

    Args:
        image: Graph of Image
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    image_parsed = parse_graph(image)
    return _internal.composition_from_image_internal(image_parsed)

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
    return _internal.composition_gaussian_blur_internal(composition_parsed, sigma_parsed)

def composition_grayscale(composition) -> Graph:
    """Composition Grayscale

    Applies grayscale to a Composition

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_grayscale_internal(composition_parsed)

def composition_halftone(composition, pixel_size, foreground_color, background_color) -> Graph:
    """Composition Halftone

    Applies a halftone effect to a composition, tiling it into cells and painting a foreground-colored dot in each cell whose radius grows as the cell darkens, over a background color.

    Args:
        composition: Graph of Composition
        pixel size: Graph of Int
        foreground color: Graph of ProfiledColor
        background color: Graph of ProfiledColor
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    pixel_size_parsed = parse_int_graph(pixel_size)
    foreground_color_parsed = parse_graph(foreground_color)
    background_color_parsed = parse_graph(background_color)
    return _internal.composition_halftone_internal(composition_parsed, pixel_size_parsed, foreground_color_parsed, background_color_parsed)

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
    return _internal.composition_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

def composition_kaleidoscope(composition, segments, rotation, warp, warp_frequency) -> Graph:
    """Composition Kaleidoscope

    Applies a kaleidoscope effect, folding the image into mirrored wedges around the center. segments controls the number of wedges, rotation spins the pattern, and warp/warp_frequency add a radial glass-like distortion.

    Args:
        composition: Graph of Composition
        segments: Graph of Float
        rotation: Graph of Float
        warp: Graph of Float
        warp frequency: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    segments_parsed = parse_float_graph(segments)
    rotation_parsed = parse_float_graph(rotation)
    warp_parsed = parse_float_graph(warp)
    warp_frequency_parsed = parse_float_graph(warp_frequency)
    return _internal.composition_kaleidoscope_internal(composition_parsed, segments_parsed, rotation_parsed, warp_parsed, warp_frequency_parsed)

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
    return _internal.composition_l_curve_internal(composition_parsed, l_curve_parsed)

def composition_lightness_threshold(composition, threshold) -> Graph:
    """Composition Lightness Threshold

    Thresholds a Composition by OkLab lightness, producing an opaque white mask where lightness exceeds the threshold and transparent black elsewhere.

    Args:
        composition: Graph of Composition
        threshold: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    threshold_parsed = parse_float_graph(threshold)
    return _internal.composition_lightness_threshold_internal(composition_parsed, threshold_parsed)

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
    return _internal.composition_linear_transform_internal(composition_parsed, entry_0_0_parsed, entry_0_1_parsed, entry_0_2_parsed, entry_0_3_parsed, entry_1_0_parsed, entry_1_1_parsed, entry_1_2_parsed, entry_1_3_parsed, entry_2_0_parsed, entry_2_1_parsed, entry_2_2_parsed, entry_2_3_parsed, entry_3_0_parsed, entry_3_1_parsed, entry_3_2_parsed, entry_3_3_parsed)

def composition_liquify(composition, amplitude, frequency) -> Graph:
    """Composition Liquify

    Applies a sinusoidal liquify distortion to this composition, displacing pixels by a wave whose size is controlled by amplitude and whose density is controlled by frequency.

    Args:
        composition: Graph of Composition
        amplitude: Graph of Float
        frequency: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    amplitude_parsed = parse_float_graph(amplitude)
    frequency_parsed = parse_float_graph(frequency)
    return _internal.composition_liquify_internal(composition_parsed, amplitude_parsed, frequency_parsed)

def composition_max_color(composition) -> Graph:
    """Composition Max Color

    Computes the maximum color in a composition. Works by finding the maximum L, a and b and alpha components of an OkLabA color.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_max_color_internal(composition_parsed)

def composition_median(composition, kernel_size) -> Graph:
    """Composition Median

    Applies a per-channel median filter to a composition over a square window, reducing noise while preserving edges. kernel_size controls the window size (window width is 2*kernel_size-1).

    Args:
        composition: Graph of Composition
        kernel size: Graph of Int
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    kernel_size_parsed = parse_int_graph(kernel_size)
    return _internal.composition_median_internal(composition_parsed, kernel_size_parsed)

def composition_min_color(composition) -> Graph:
    """Composition Min Color

    Computes the minimum color in a composition. Works by finding the minimum L, a and b and alpha components of an OkLabA color.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_min_color_internal(composition_parsed)

def composition_min_max_colors(composition) -> Graph:
    """Composition Min Max Colors

    Computes the minimum and maximum colors in a composition. Works by finding the minimum and maximum L, a and b and alpha components of an OkLabA color.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a ProfiledColorList.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_min_max_colors_internal(composition_parsed)

def composition_monet_women_with_parasol() -> Graph:
    """Monet's Women with a Parasol

    Creates a composition from Monet's "Women with a Parasol" painting. Used frequently as a test asset.

    Returns:
        Graph: A graph node producing a Composition.
    """
    return _internal.composition_monet_women_with_parasol_internal()

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
    return _internal.composition_morphological_max_internal(composition_parsed, dimension_parsed)

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
    return _internal.composition_morphological_min_internal(composition_parsed, dimension_parsed)

def composition_negative(composition) -> Graph:
    """Composition Negative

    Creates the effect of a negative image by subracting from each component of the image.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_negative_internal(composition_parsed)

def composition_nonlinear_r_g_b_blend_alpha(foreground, background, foreground_transform) -> Graph:
    """Composition Nonlinear RGB Blend Alpha

    A specialized version of CompositionBlendAlpha. Blends in a non-linear RGB.

    Args:
        foreground: Graph of Composition
        background: Graph of Composition
        transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    foreground_parsed = parse_graph(foreground)
    background_parsed = parse_graph(background)
    foreground_transform_parsed = parse_graph(foreground_transform)
    return _internal.composition_nonlinear_r_g_b_blend_alpha_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

def composition_opacity_scale(composition, scale) -> Graph:
    """Composition Opacity Scale

    Changes the opacity of an image by multiplying it by a scalar.

    Args:
        composition: Graph of Composition
        scale: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    scale_parsed = parse_float_graph(scale)
    return _internal.composition_opacity_scale_internal(composition_parsed, scale_parsed)

def composition_painter(painter) -> Graph:
    """Composition Painter

    Creates a composition from a painter.

    Args:
        painter: Graph of Painter
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    painter_parsed = parse_graph(painter)
    return _internal.composition_painter_internal(painter_parsed)

def composition_palette(composition, size) -> Graph:
    """Composition Palette

    Generates a palette of the most dominant colors of a composition.

    Args:
        composition: Graph of Composition
        number of colors in the palette: Graph of Int
        

    Returns:
        Graph: A graph node producing a ProfiledColorList.
    """
    composition_parsed = parse_graph(composition)
    size_parsed = parse_int_graph(size)
    return _internal.composition_palette_internal(composition_parsed, size_parsed)

def composition_palette_reduction(composition, palette) -> Graph:
    """Composition Palette Reduction

    Reduces the number of colors in a composition to a specified palette.

    Args:
        composition: Graph of Composition
        palette: Graph of ProfiledColorList
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    palette_parsed = parse_graph(palette)
    return _internal.composition_palette_reduction_internal(composition_parsed, palette_parsed)

def composition_passthrough(value) -> Graph:
    """Composition Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    value_parsed = parse_graph(value)
    return _internal.composition_passthrough_internal(value_parsed)

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
    return _internal.composition_pixelate_internal(composition_parsed, pixel_size_parsed)

def composition_point_effect_shader(composition, function_body, helpers, effect_center_point, effect_radius, inputs, working_color_representation) -> Graph:
    """Composition Point Effect Shader

    Runs a custom shader over a circular region around an effect center point.

    Args:
        composition: Graph of Composition
        function body: Graph of String
        helpers: Graph of String
        effect center point: Graph of Point2f
        effect radius: Graph of Float
        inputs: Graph of Dictionary
        working color representation: Graph of ColorRepresentation
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    function_body_parsed = parse_string_graph(function_body)
    helpers_parsed = parse_string_graph(helpers)
    effect_center_point_parsed = parse_graph(effect_center_point)
    effect_radius_parsed = parse_float_graph(effect_radius)
    inputs_parsed = parse_graph(inputs)
    working_color_representation_parsed = parse_graph(working_color_representation)
    return _internal.composition_point_effect_shader_internal(composition_parsed, function_body_parsed, helpers_parsed, effect_center_point_parsed, effect_radius_parsed, inputs_parsed, working_color_representation_parsed)

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
    return _internal.composition_r_g_b_curve_internal(composition_parsed, r_curve_parsed, g_curve_parsed, b_curve_parsed)

def composition_render_to_image(composition) -> Graph:
    """Composition Render to Image

    Renders a Composition to an Image

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Image.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_render_to_image_internal(composition_parsed)

def composition_rotate180(composition) -> Graph:
    """Composition Rotate 180

    Rotates the image 180 degrees

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_rotate180_internal(composition_parsed)

def composition_rotate90_clockwise(composition) -> Graph:
    """Composition Rotate 90 Clockwise

    Rotates the image 90 degrees clockwise

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_rotate90_clockwise_internal(composition_parsed)

def composition_rotate90_counter_clockwise(composition) -> Graph:
    """Composition Rotate 90 Counter Clockwise

    Rotates the image 90 degrees counter-clockwise

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_rotate90_counter_clockwise_internal(composition_parsed)

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
    return _internal.composition_s_a_m3_image_internal(composition_parsed, prompt_parsed, positive_points_parsed, negative_points_parsed)

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
    return _internal.composition_saturation_adjust_internal(composition_parsed, scale_parsed)

def composition_scanlines(composition, size, beam_power, line_offset, intensity) -> Graph:
    """Composition Scanlines

    Applies a CRT-style scanline effect, darkening the composition in horizontal bands whose spacing is set by size, sharpness by beam power, vertical phase by line offset, and overall strength by intensity.

    Args:
        composition: Graph of Composition
        size: Graph of Float
        beam power: Graph of Float
        line offset: Graph of Float
        intensity: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    size_parsed = parse_float_graph(size)
    beam_power_parsed = parse_float_graph(beam_power)
    line_offset_parsed = parse_float_graph(line_offset)
    intensity_parsed = parse_float_graph(intensity)
    return _internal.composition_scanlines_internal(composition_parsed, size_parsed, beam_power_parsed, line_offset_parsed, intensity_parsed)

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
    return _internal.composition_segment_internal(composition_parsed, prompt_parsed, positive_points_parsed, negative_points_parsed)

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
    return _internal.composition_sharpen_internal(composition_parsed, radius_parsed, strength_parsed)

def composition_sobel_edge_detection(composition) -> Graph:
    """Composition Sobel Edge Detection

    Applies Sobel edge detection to an image.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_sobel_edge_detection_internal(composition_parsed)

def composition_spacial_effect_shader(composition, function_body, helpers, max_displacement, inputs, working_color_representation) -> Graph:
    """Composition Spacial Effect Shader

    Runs a custom shader over an input that can spatially displace pixels by up to a maximum displacement.

    Args:
        composition: Graph of Composition
        function body: Graph of String
        helpers: Graph of String
        max displacement: Graph of Float
        inputs: Graph of Dictionary
        working color representation: Graph of ColorRepresentation
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    function_body_parsed = parse_string_graph(function_body)
    helpers_parsed = parse_string_graph(helpers)
    max_displacement_parsed = parse_float_graph(max_displacement)
    inputs_parsed = parse_graph(inputs)
    working_color_representation_parsed = parse_graph(working_color_representation)
    return _internal.composition_spacial_effect_shader_internal(composition_parsed, function_body_parsed, helpers_parsed, max_displacement_parsed, inputs_parsed, working_color_representation_parsed)

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
    return _internal.composition_swirl_internal(composition_parsed, center_parsed, radius_parsed, amount_parsed)

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
    return _internal.composition_target_white_kelvin_internal(composition_parsed, kelvin_parsed)

def composition_to_ok_lab_hist(composition) -> Graph:
    """Composition to OkLab Histogram

    Creates an OkLab Histogram from the colors in a Composition.

    Args:
        composition: Graph of Composition
        

    Returns:
        Graph: A graph node producing a OkLabHist.
    """
    composition_parsed = parse_graph(composition)
    return _internal.composition_to_ok_lab_hist_internal(composition_parsed)

def composition_transform(composition, transform) -> Graph:
    """Composition Transform

    Applies a 2D transform to a Composition.

    Args:
        composition: Graph of Composition
        transform: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    transform_parsed = parse_graph(transform)
    return _internal.composition_transform_internal(composition_parsed, transform_parsed)

def composition_vibrance_adjustment(composition, strength) -> Graph:
    """Composition Vibrance Adjustment

    Adjusts the vibrance of an image by a given strength. Internally, boosts chroma in OkLab color space adaptively, applying more boost to less saturated colors.

    Args:
        composition: Graph of Composition
        strength: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    strength_parsed = parse_float_graph(strength)
    return _internal.composition_vibrance_adjustment_internal(composition_parsed, strength_parsed)

def composition_vignette(composition, center, radius_x, radius_y, softness, strength) -> Graph:
    """Composition Vignette

    darkens the area outside an ellipse - center is the bright spot in pixel coordinates, radius_x and radius_y are the ellipse semi-axes in pixels where the falloff starts, softness is the width of the fade-out band in pixels, and strength (0-1) defines how dark the edges become at maximum.

    Args:
        composition: Graph of Composition
        center: Graph of Vector2f
        radius x: Graph of Float
        radius y: Graph of Float
        softness: Graph of Float
        strength: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    center_parsed = parse_graph(center)
    radius_x_parsed = parse_float_graph(radius_x)
    radius_y_parsed = parse_float_graph(radius_y)
    softness_parsed = parse_float_graph(softness)
    strength_parsed = parse_float_graph(strength)
    return _internal.composition_vignette_internal(composition_parsed, center_parsed, radius_x_parsed, radius_y_parsed, softness_parsed, strength_parsed)

def composition_zoom_blur(composition, center, strength, falloff, effect_radius) -> Graph:
    """Composition Zoom Blur

    Performs a zoom blur on this composition

    Args:
        composition: Graph of Composition
        center: Graph of Vector2f
        strength: Graph of Float
        falloff: Graph of Float
        effect radius: Graph of Float
        

    Returns:
        Graph: A graph node producing a Composition.
    """
    composition_parsed = parse_graph(composition)
    center_parsed = parse_graph(center)
    strength_parsed = parse_float_graph(strength)
    falloff_parsed = parse_float_graph(falloff)
    effect_radius_parsed = parse_float_graph(effect_radius)
    return _internal.composition_zoom_blur_internal(composition_parsed, center_parsed, strength_parsed, falloff_parsed, effect_radius_parsed)

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
    return _internal.curve_evaluate_internal(curve_parsed, input_parsed)

def curve_gamma(gamma) -> Graph:
    """Curve Gamma

    A gamma curve. The gamma parameter corresponding to y=x^gamma.

    Args:
        gamma: Graph of Float
        

    Returns:
        Graph: A graph node producing a Curve.
    """
    gamma_parsed = parse_float_graph(gamma)
    return _internal.curve_gamma_internal(gamma_parsed)

def curve_identity() -> Graph:
    """Curve Identity

    An identity curve, y=x

    Returns:
        Graph: A graph node producing a Curve.
    """
    return _internal.curve_identity_internal()

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
    return _internal.curve_pivoted_sigmoid_internal(pivot_parsed, slope_parsed)

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
    return _internal.curve_s_curve_internal(pivot_parsed, slope_parsed, toe_parsed, shoulder_parsed)

def dictionary_create() -> Graph:
    """Dictionary Create

    Creates a new dictionary

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    return _internal.dictionary_create_internal()

def file_convert_image_to_bmp(image_bytes) -> Graph:
    """File Convert Image to BMP

    Converts any image format (JPEG, PNG, WebP, TIFF, HEIC, etc.) to BMP. Returns BMP bytes.

    Args:
        image bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_bytes_parsed = parse_graph(image_bytes)
    return _internal.file_convert_image_to_bmp_internal(image_bytes_parsed)

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
    return _internal.file_convert_image_to_heic_internal(image_bytes_parsed, quality_parsed)

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
    return _internal.file_convert_image_to_jpeg_internal(image_bytes_parsed, quality_parsed)

def file_convert_image_to_png(image_bytes) -> Graph:
    """File Convert Image to PNG

    Converts any image format (JPEG, WebP, TIFF, BMP, HEIC, etc.) to PNG. Returns PNG bytes.

    Args:
        image bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_bytes_parsed = parse_graph(image_bytes)
    return _internal.file_convert_image_to_png_internal(image_bytes_parsed)

def file_convert_image_to_tiff(image_bytes) -> Graph:
    """File Convert Image to TIFF

    Converts any image format (JPEG, PNG, WebP, BMP, HEIC, etc.) to TIFF. Returns TIFF bytes.

    Args:
        image bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_bytes_parsed = parse_graph(image_bytes)
    return _internal.file_convert_image_to_tiff_internal(image_bytes_parsed)

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
    return _internal.file_convert_image_to_web_p_internal(image_bytes_parsed, quality_parsed)

def file_convert_video_to_animated_web_p(video_bytes) -> Graph:
    """File Convert Video to Animated WebP

    Converts any video format (MP4, MOV, WebM, AVI, MKV) to an animated WebP. Returns animated WebP bytes.

    Args:
        video bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    video_bytes_parsed = parse_graph(video_bytes)
    return _internal.file_convert_video_to_animated_web_p_internal(video_bytes_parsed)

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
    return _internal.file_convert_video_to_gif_internal(video_bytes_parsed, frame_rate_parsed)

def file_convert_video_to_m_p4(video_bytes) -> Graph:
    """File Convert Video to MP4

    Converts any video format (MOV, WebM, AVI, MKV) to MP4. Returns MP4 bytes.

    Args:
        video bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    video_bytes_parsed = parse_graph(video_bytes)
    return _internal.file_convert_video_to_m_p4_internal(video_bytes_parsed)

def file_convert_video_to_web_m(video_bytes) -> Graph:
    """File Convert Video to WebM

    Converts any video format (MP4, MOV, AVI, MKV) to WebM. Returns WebM bytes.

    Args:
        video bytes (any format): Graph of ByteList
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    video_bytes_parsed = parse_graph(video_bytes)
    return _internal.file_convert_video_to_web_m_internal(video_bytes_parsed)

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
    return _internal.fill_custom_internal(function_body_parsed, helpers_parsed, inputs_parsed)

def fill_solid(color) -> Graph:
    """Fill Solid

    Creates a fill with a solid color.

    Args:
        color: Graph of ProfiledColor
        

    Returns:
        Graph: A graph node producing a Fill.
    """
    color_parsed = parse_graph(color)
    return _internal.fill_solid_internal(color_parsed)

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
    return _internal.float_add_internal(float1_parsed, float2_parsed)

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
    return _internal.float_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

def float_cos(angle) -> Graph:
    """Float Cosine

    Computes the cosine of a float (in radians).

    Args:
        Angle in radians: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    angle_parsed = parse_float_graph(angle)
    return _internal.float_cos_internal(angle_parsed)

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
    return _internal.float_divide_internal(float1_parsed, float2_parsed)

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
    return _internal.float_equals_internal(float_1_parsed, float_2_parsed)

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
    return _internal.float_greater_than_internal(float_1_parsed, float_2_parsed)

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
    return _internal.float_greater_than_or_equal_internal(float_1_parsed, float_2_parsed)

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
    return _internal.float_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

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
    return _internal.float_lerp_internal(x_parsed, float1_parsed, float2_parsed)

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
    return _internal.float_less_than_internal(float_1_parsed, float_2_parsed)

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
    return _internal.float_less_than_or_equal_internal(float_1_parsed, float_2_parsed)

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
    return _internal.float_max_internal(float1_parsed, float2_parsed)

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
    return _internal.float_min_internal(float1_parsed, float2_parsed)

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
    return _internal.float_multiply_internal(float1_parsed, float2_parsed)

def float_passthrough(value) -> Graph:
    """Float Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    value_parsed = parse_float_graph(value)
    return _internal.float_passthrough_internal(value_parsed)

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
    return _internal.float_pow_internal(float1_parsed, float2_parsed)

def float_round_to_int(float) -> Graph:
    """Float Round to Int

    Rounds the float to the nearest int

    Args:
        float: Graph of Float
        

    Returns:
        Graph: A graph node producing a Int.
    """
    float_parsed = parse_float_graph(float)
    return _internal.float_round_to_int_internal(float_parsed)

def float_sin(angle) -> Graph:
    """Float Sine

    Computes the sine of a float (in radians).

    Args:
        Angle in radians: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    angle_parsed = parse_float_graph(angle)
    return _internal.float_sin_internal(angle_parsed)

def float_square_root(number) -> Graph:
    """Float Square Root

    Compares the square root of a number

    Args:
        Number: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    number_parsed = parse_float_graph(number)
    return _internal.float_square_root_internal(number_parsed)

def float_squared(number) -> Graph:
    """Float Squared

    Raises a float to the power of 2.

    Args:
        Number: Graph of Float
        

    Returns:
        Graph: A graph node producing a Float.
    """
    number_parsed = parse_float_graph(number)
    return _internal.float_squared_internal(number_parsed)

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
    return _internal.float_subtract_internal(float1_parsed, float2_parsed)

def image_from_byte_list(bytes) -> Graph:
    """Image from Bytes

    Given some bytes, parses an image

    Args:
        bytes: Graph of ByteList
        

    Returns:
        Graph: A graph node producing a Image.
    """
    bytes_parsed = parse_graph(bytes)
    return _internal.image_from_byte_list_internal(bytes_parsed)

def image_to_byte_list(image) -> Graph:
    """Image to Byte List

    Given an image, converts it to a byte list

    Args:
        image: Graph of Image
        

    Returns:
        Graph: A graph node producing a ByteList.
    """
    image_parsed = parse_graph(image)
    return _internal.image_to_byte_list_internal(image_parsed)

def int_abs(number) -> Graph:
    """Int Absolute Value

    Returns the absolute value of an int

    Args:
        number: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    number_parsed = parse_int_graph(number)
    return _internal.int_abs_internal(number_parsed)

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
    return _internal.int_add_internal(int_1_parsed, int_2_parsed)

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
    return _internal.int_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

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
    return _internal.int_equals_internal(int_1_parsed, int_2_parsed)

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
    return _internal.int_greater_than_internal(int_1_parsed, int_2_parsed)

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
    return _internal.int_greater_than_or_equal_internal(int_1_parsed, int_2_parsed)

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
    return _internal.int_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

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
    return _internal.int_less_than_internal(int_1_parsed, int_2_parsed)

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
    return _internal.int_less_than_or_equal_internal(int_1_parsed, int_2_parsed)

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
    return _internal.int_max_internal(int1_parsed, int2_parsed)

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
    return _internal.int_min_internal(int1_parsed, int2_parsed)

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
    return _internal.int_multiply_internal(int_1_parsed, int_2_parsed)

def int_passthrough(value) -> Graph:
    """Int Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Int
        

    Returns:
        Graph: A graph node producing a Int.
    """
    value_parsed = parse_int_graph(value)
    return _internal.int_passthrough_internal(value_parsed)

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
    return _internal.int_subtract_internal(int_1_parsed, int_2_parsed)

def int_to_float(int) -> Graph:
    """Int To Float

    Converts an Int to a Float

    Args:
        int: Graph of Int
        

    Returns:
        Graph: A graph node producing a Float.
    """
    int_parsed = parse_int_graph(int)
    return _internal.int_to_float_internal(int_parsed)

def monet_network_download_u_r_l_from_asset_i_d(asset_id) -> Graph:
    """Monet Network Download URL from Asset ID

    Creates a Download URL from asset ID in the Monet Network

    Args:
        asset id: Graph of Int
        

    Returns:
        Graph: A graph node producing a String.
    """
    asset_id_parsed = parse_int_graph(asset_id)
    return _internal.monet_network_download_u_r_l_from_asset_i_d_internal(asset_id_parsed)

def not_(bool) -> Graph:
    """Not

    Returns the opposite of a boolean

    Args:
        Bool: Graph of Bool
        

    Returns:
        Graph: A graph node producing a Bool.
    """
    bool_parsed = parse_bool_graph(bool)
    return _internal.not_internal(bool_parsed)

def null_value() -> Graph:
    """Null Value

    Returns a null value

    Returns:
        Graph: A graph node producing a Null.
    """
    return _internal.null_value_internal()

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
    return _internal.ok_lab_color_from_components_internal(l_parsed, a_parsed, b_parsed)

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
    return _internal.ok_lab_hist_lightness_quantile_internal(hist_parsed, quantile_parsed)

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
    return _internal.or_internal(bool1_parsed, bool2_parsed)

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
    return _internal.painter_add_ellipse_with_render_style_internal(painter_parsed, center_parsed, dimensions_parsed, rotation_parsed, render_style_parsed, instances_parsed)

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
    return _internal.painter_add_path_with_render_style_internal(painter_parsed, path_parsed, render_style_parsed, instances_parsed)

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
    return _internal.painter_add_rectangle_with_render_style_internal(painter_parsed, center_parsed, dimensions_parsed, rotation_parsed, render_style_parsed, instances_parsed)

def painter_new() -> Graph:
    """Painter New

    Creates a new painter.

    Returns:
        Graph: A graph node producing a Painter.
    """
    return _internal.painter_new_internal()

def path_cardinal_cubic_to_point(path, point, tension) -> Graph:
    """Path Cardinal Cubic to Point

    Moves the path from it's current point to another with a Cardinal Cubic spline.

    Args:
        path: Graph of Path
        point: Graph of Point2f
        tension: Graph of Float
        

    Returns:
        Graph: A graph node producing a Path.
    """
    path_parsed = parse_graph(path)
    point_parsed = parse_graph(point)
    tension_parsed = parse_float_graph(tension)
    return _internal.path_cardinal_cubic_to_point_internal(path_parsed, point_parsed, tension_parsed)

def path_catmull_rom_to_point(path, point) -> Graph:
    """Path Catmull-Rom to Point

    Moves the path from it's current point to another with a Catmull-Rom spline.

    Args:
        path: Graph of Path
        point: Graph of Point2f
        

    Returns:
        Graph: A graph node producing a Path.
    """
    path_parsed = parse_graph(path)
    point_parsed = parse_graph(point)
    return _internal.path_catmull_rom_to_point_internal(path_parsed, point_parsed)

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
    return _internal.path_line_to_point_internal(path_parsed, point_parsed)

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
    return _internal.path_move_to_point_internal(path_parsed, point_parsed)

def path_new() -> Graph:
    """Path New

    Creates a new empty path.

    Returns:
        Graph: A graph node producing a Path.
    """
    return _internal.path_new_internal()

def pi() -> Graph:
    """Pi

    Returns π as a float

    Returns:
        Graph: A graph node producing a Float.
    """
    return _internal.pi_internal()

def pixel_encoding_encoded() -> Graph:
    """Pixel Encoding Encoded

    Creates a Pixel Encoding representing gamma or other non-linear encoded values.

    Returns:
        Graph: A graph node producing a PixelEncoding.
    """
    return _internal.pixel_encoding_encoded_internal()

def pixel_encoding_linear() -> Graph:
    """Pixel Encoding Linear

    Creates a Pixel Encoding representing linear light, straight alpha values.

    Returns:
        Graph: A graph node producing a PixelEncoding.
    """
    return _internal.pixel_encoding_linear_internal()

def pixel_encoding_premultiplied_alpha() -> Graph:
    """Pixel Encoding Premultiplied Alpha

    Creates a Pixel Encoding representing linear light, premultiplied alpha values.

    Returns:
        Graph: A graph node producing a PixelEncoding.
    """
    return _internal.pixel_encoding_premultiplied_alpha_internal()

def point2f_distance(lhs, rhs) -> Graph:
    """Point 2 Float Distance

    The Euclidean distance between two Point 2 Floats.

    Args:
        The first point: Graph of Point2f
        The second point: Graph of Point2f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    lhs_parsed = parse_graph(lhs)
    rhs_parsed = parse_graph(rhs)
    return _internal.point2f_distance_internal(lhs_parsed, rhs_parsed)

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
    return _internal.point2f_from_components_internal(x_parsed, y_parsed)

def point2i_distance(lhs, rhs) -> Graph:
    """Point 2 Int Distance

    The Euclidean distance between two Point 2 Ints, returned as a Float.

    Args:
        The first point: Graph of Point2i
        The second point: Graph of Point2i
        

    Returns:
        Graph: A graph node producing a Float.
    """
    lhs_parsed = parse_graph(lhs)
    rhs_parsed = parse_graph(rhs)
    return _internal.point2i_distance_internal(lhs_parsed, rhs_parsed)

def point2i_from_components(x, y) -> Graph:
    """Point 2 Int from Components

    Given an x and y creates a point

    Args:
        x: Graph of Int
        y: Graph of Int
        

    Returns:
        Graph: A graph node producing a Point2i.
    """
    x_parsed = parse_int_graph(x)
    y_parsed = parse_int_graph(y)
    return _internal.point2i_from_components_internal(x_parsed, y_parsed)

def profiled_color_add_to_dictionary(dictionary, key, value) -> Graph:
    """Profiled Color Add To Dictionary

    Adds a Profiled Color to a Dictionary

    Args:
        dictionary: Graph of Dictionary
        key: Graph of String
        value: Graph of ProfiledColor
        

    Returns:
        Graph: A graph node producing a Dictionary.
    """
    dictionary_parsed = parse_graph(dictionary)
    key_parsed = parse_string_graph(key)
    value_parsed = parse_graph(value)
    return _internal.profiled_color_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

def profiled_color_brightness_adjust(profiled_color, offset) -> Graph:
    """Profiled Color Brightness Adjust

    Adjusts a profiled color's lightness in OkLab.

    Args:
        profiled color: Graph of ProfiledColor
        lightness offset: Graph of Float
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    profiled_color_parsed = parse_graph(profiled_color)
    offset_parsed = parse_float_graph(offset)
    return _internal.profiled_color_brightness_adjust_internal(profiled_color_parsed, offset_parsed)

def profiled_color_chroma_offset(profiled_color, offset) -> Graph:
    """Profiled Color Chroma Offset

    Applies an offset to the a and b chroma components of a profiled color in OkLab.

    Args:
        profiled color: Graph of ProfiledColor
        chroma offset: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    profiled_color_parsed = parse_graph(profiled_color)
    offset_parsed = parse_graph(offset)
    return _internal.profiled_color_chroma_offset_internal(profiled_color_parsed, offset_parsed)

def profiled_color_from_ok_lab_a(ok_lab_a) -> Graph:
    """Profiled Color from OkLab with Alpha

    Creates a profiled color from OkLab channels and alpha.

    Args:
        OkLab color with alpha: Graph of OkLabA
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    ok_lab_a_parsed = parse_graph(ok_lab_a)
    return _internal.profiled_color_from_ok_lab_a_internal(ok_lab_a_parsed)

def profiled_color_from_rgba_aces_cg(rgba) -> Graph:
    """Profiled Color from RGBA ACEScg

    Creates a profiled color from linear ACEScg RGBA channels.

    Args:
        linear ACEScg color: Graph of RGBAColor
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    rgba_parsed = parse_graph(rgba)
    return _internal.profiled_color_from_rgba_aces_cg_internal(rgba_parsed)

def profiled_color_from_rgba_srgb(rgba) -> Graph:
    """Profiled Color from RGBA sRGB

    Creates a profiled color from encoded sRGB RGBA channels.

    Args:
        encoded sRGB color: Graph of RGBAColor
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    rgba_parsed = parse_graph(rgba)
    return _internal.profiled_color_from_rgba_srgb_internal(rgba_parsed)

def profiled_color_from_xyz_a(xyza) -> Graph:
    """Profiled Color from XYZ with Alpha

    Creates a profiled color from XYZ channels and alpha.

    Args:
        XYZ color with alpha: Graph of XYZA
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    xyza_parsed = parse_graph(xyza)
    return _internal.profiled_color_from_xyz_a_internal(xyza_parsed)

def profiled_color_grayscale(profiled_color) -> Graph:
    """Profiled Color Grayscale

    Removes chroma from a profiled color.

    Args:
        profiled color: Graph of ProfiledColor
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    profiled_color_parsed = parse_graph(profiled_color)
    return _internal.profiled_color_grayscale_internal(profiled_color_parsed)

def profiled_color_lightness_curve(profiled_color, l_curve) -> Graph:
    """Profiled Color Lightness Curve

    Applies a curve to the L component of a profiled color in OkLab.

    Args:
        profiled color: Graph of ProfiledColor
        lightness curve: Graph of Curve
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    profiled_color_parsed = parse_graph(profiled_color)
    l_curve_parsed = parse_graph(l_curve)
    return _internal.profiled_color_lightness_curve_internal(profiled_color_parsed, l_curve_parsed)

def profiled_color_saturation_adjust(profiled_color, scale) -> Graph:
    """Profiled Color Saturation Adjust

    Scales the chroma components of a profiled color in OkLab.

    Args:
        profiled color: Graph of ProfiledColor
        saturation scale: Graph of Float
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    profiled_color_parsed = parse_graph(profiled_color)
    scale_parsed = parse_float_graph(scale)
    return _internal.profiled_color_saturation_adjust_internal(profiled_color_parsed, scale_parsed)

def profiled_color_target_white(profiled_color, target_white) -> Graph:
    """Profiled Color Target White

    Adapts a profiled color to the specified XYZ white point.

    Args:
        profiled color: Graph of ProfiledColor
        target white point: Graph of XYZ
        

    Returns:
        Graph: A graph node producing a ProfiledColor.
    """
    profiled_color_parsed = parse_graph(profiled_color)
    target_white_parsed = parse_graph(target_white)
    return _internal.profiled_color_target_white_internal(profiled_color_parsed, target_white_parsed)

def profiled_color_to_ok_lab_a(profiled_color) -> Graph:
    """Profiled Color to OkLab with Alpha

    Converts a profiled color to OkLab channels with alpha.

    Args:
        profiled color: Graph of ProfiledColor
        

    Returns:
        Graph: A graph node producing a OkLabA.
    """
    profiled_color_parsed = parse_graph(profiled_color)
    return _internal.profiled_color_to_ok_lab_a_internal(profiled_color_parsed)

def profiled_color_to_rgb_encoded_with_in_color_profile(profiled_color) -> Graph:
    """Profiled Color to Encoded RGB in Input Color Profile

    Converts a profiled color to encoded RGB channels in its input color profile. The input color profile must be RGB.

    Args:
        profiled color: Graph of ProfiledColor
        

    Returns:
        Graph: A graph node producing a RGBAColor.
    """
    profiled_color_parsed = parse_graph(profiled_color)
    return _internal.profiled_color_to_rgb_encoded_with_in_color_profile_internal(profiled_color_parsed)

def profiled_color_to_xyz_a(profiled_color) -> Graph:
    """Profiled Color to XYZ with Alpha

    Converts a profiled color to XYZ channels with alpha.

    Args:
        profiled color: Graph of ProfiledColor
        

    Returns:
        Graph: A graph node producing a XYZA.
    """
    profiled_color_parsed = parse_graph(profiled_color)
    return _internal.profiled_color_to_xyz_a_internal(profiled_color_parsed)

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
    return _internal.r_g_b_a_color_from_components_internal(r_parsed, g_parsed, b_parsed, a_parsed)

def r_g_b_a_color_passthrough(value) -> Graph:
    """RGBA Color Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of RGBAColor
        

    Returns:
        Graph: A graph node producing a RGBAColor.
    """
    value_parsed = parse_graph(value)
    return _internal.r_g_b_a_color_passthrough_internal(value_parsed)

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
    return _internal.r_g_b_color_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

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
    return _internal.r_g_b_color_from_components_internal(r_parsed, g_parsed, b_parsed)

def r_g_b_color_passthrough(value) -> Graph:
    """RGB Color Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of RGBColor
        

    Returns:
        Graph: A graph node producing a RGBColor.
    """
    value_parsed = parse_graph(value)
    return _internal.r_g_b_color_passthrough_internal(value_parsed)

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
    return _internal.r_g_b_to_ok_lab_internal(rgb_parsed, color_profile_parsed)

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
    return _internal.render_style_brush_and_fill_internal(brush_parsed, fill_parsed)

def render_style_brush_only(brush) -> Graph:
    """Render Style Brush Only

    Creates a render style that will only have a brush.

    Args:
        brush: Graph of Brush
        

    Returns:
        Graph: A graph node producing a RenderStyle.
    """
    brush_parsed = parse_graph(brush)
    return _internal.render_style_brush_only_internal(brush_parsed)

def render_style_fill_only(fill) -> Graph:
    """Render Style Fill Only

    Creates a render style that will only have a fill.

    Args:
        fill: Graph of Fill
        

    Returns:
        Graph: A graph node producing a RenderStyle.
    """
    fill_parsed = parse_graph(fill)
    return _internal.render_style_fill_only_internal(fill_parsed)

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
    return _internal.sequence_adjust_speed_internal(sequence_parsed, factor_parsed)

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
    return _internal.sequence_composition_at_time_internal(sequence_parsed, time_parsed)

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
    return _internal.sequence_concatenate_internal(sequence_1_parsed, sequence_2_parsed)

def sequence_duration(sequence) -> Graph:
    """Sequence Duration

    Gets the duration from a sequence

    Args:
        sequence: Graph of Sequence
        

    Returns:
        Graph: A graph node producing a Float.
    """
    sequence_parsed = parse_graph(sequence)
    return _internal.sequence_duration_internal(sequence_parsed)

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
    return _internal.sequence_from_composition_and_duration_internal(composition_parsed, duration_parsed)

def sequence_from_u_r_l(url) -> Graph:
    """Sequence from URL

    Creates a sequence from URL

    Args:
        url: Graph of String
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    url_parsed = parse_string_graph(url)
    return _internal.sequence_from_u_r_l_internal(url_parsed)

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
    return _internal.sequence_graph_internal(duration_parsed, time_parsed, frame_parsed)

def sequence_grayscale(sequence) -> Graph:
    """Sequence Grayscale

    Creates a sequence that converts the video to grayscale

    Args:
        sequence: Graph of Sequence
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    sequence_parsed = parse_graph(sequence)
    return _internal.sequence_grayscale_internal(sequence_parsed)

def sequence_passthrough(value) -> Graph:
    """Sequence Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Sequence
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    value_parsed = parse_graph(value)
    return _internal.sequence_passthrough_internal(value_parsed)

def sequence_reverse(sequence) -> Graph:
    """Sequence Reverse

    Given a sequence. Reverses it.

    Args:
        sequence: Graph of Sequence
        

    Returns:
        Graph: A graph node producing a Sequence.
    """
    sequence_parsed = parse_graph(sequence)
    return _internal.sequence_reverse_internal(sequence_parsed)

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
    return _internal.sequence_to_mp4_internal(sequence_parsed, frame_rate_parsed)

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
    return _internal.sequence_trim_back_internal(sequence_parsed, amount_parsed)

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
    return _internal.sequence_trim_front_internal(sequence_parsed, amount_parsed)

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
    return _internal.string_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

def transform2_identity() -> Graph:
    """Transform 2D Identity

    Creates a 2D transform that is the identity transform.

    Returns:
        Graph: A graph node producing a Transform2.
    """
    return _internal.transform2_identity_internal()

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
    return _internal.transform2_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

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
    return _internal.transform2_rotate_internal(transform_parsed, angle_parsed)

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
    return _internal.transform2_scale_internal(transform_parsed, scale_parsed)

def transform2_to_list(item) -> Graph:
    """Transform 2D to List

    Converts Transform 2D to a single item list

    Args:
        item: Graph of Transform2
        

    Returns:
        Graph: A graph node producing a Transform2List.
    """
    item_parsed = parse_graph(item)
    return _internal.transform2_to_list_internal(item_parsed)

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
    return _internal.transform2_translation_internal(transform_parsed, translation_parsed)

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
    return _internal.upload_byte_list_internal(bytes_parsed, url_parsed, content_type_parsed)

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
    return _internal.upload_file_path_internal(path_parsed, url_parsed, content_type_parsed)

def vector2_int_to_vector2_float(vector) -> Graph:
    """Vector 2 Int to Vector 2 Float

    Given a Vector 2 Int. Creates a Vector 2 Float.

    Args:
        vector: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector2_int_to_vector2_float_internal(vector_parsed)

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
    return _internal.vector2f_add_internal(lhs_parsed, rhs_parsed)

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
    return _internal.vector2f_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

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
    return _internal.vector2f_from_components_internal(x_parsed, y_parsed)

def vector2f_normalize(vector) -> Graph:
    """Vector 2 Float Normalize

    Normalizes a Vector. Converting it's length to 1.

    Args:
        Vector: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector2f_normalize_internal(vector_parsed)

def vector2f_passthrough(value) -> Graph:
    """Vector 2 Float Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    value_parsed = parse_graph(value)
    return _internal.vector2f_passthrough_internal(value_parsed)

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
    return _internal.vector2f_scalar_multiply_internal(vector_parsed, scalar_parsed)

def vector2f_x(vector) -> Graph:
    """Vector 2 Float get X

    Retrieves the X component of a Vector 2 Float.

    Args:
        vector: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector2f_x_internal(vector_parsed)

def vector2f_y(vector) -> Graph:
    """Vector 2 Float get Y

    Retrieves the Y component of a Vector 2 Float.

    Args:
        vector: Graph of Vector2f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector2f_y_internal(vector_parsed)

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
    return _internal.vector2i_add_internal(lhs_parsed, rhs_parsed)

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
    return _internal.vector2i_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

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
    return _internal.vector2i_from_components_internal(x_parsed, y_parsed)

def vector2i_passthrough(value) -> Graph:
    """Vector 2 Int Passthrough

    Responds with the value provided. Doing nothing to it.

    Args:
        value: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Vector2i.
    """
    value_parsed = parse_graph(value)
    return _internal.vector2i_passthrough_internal(value_parsed)

def vector2i_to_vector2f(vector) -> Graph:
    """Vector 2 Int to Vector 2 Float

    Given a Vector 2 Int. Creates a Vector 2 Float.

    Args:
        vector: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Vector2f.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector2i_to_vector2f_internal(vector_parsed)

def vector2i_x(vector) -> Graph:
    """Vector 2 Int get X

    Retrieves the X component of a Vector 2 Int.

    Args:
        vector: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Int.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector2i_x_internal(vector_parsed)

def vector2i_y(vector) -> Graph:
    """Vector 2 Int get Y

    Retrieves the Y component of a Vector 2 Int.

    Args:
        vector: Graph of Vector2i
        

    Returns:
        Graph: A graph node producing a Int.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector2i_y_internal(vector_parsed)

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
    return _internal.vector3f_add_internal(lhs_parsed, rhs_parsed)

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
    return _internal.vector3f_from_components_internal(x_parsed, y_parsed, z_parsed)

def vector3f_normalize(vector) -> Graph:
    """Vector 3 Normalize

    Normalizes a Vector 3 Float. Converting it's length to 1.

    Args:
        Vector: Graph of Vector3f
        

    Returns:
        Graph: A graph node producing a Vector3f.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector3f_normalize_internal(vector_parsed)

def vector3f_x(vector) -> Graph:
    """Vector 3D Float X

    Gets the value in the x component for the provided vector

    Args:
        vector: Graph of Vector3f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector3f_x_internal(vector_parsed)

def vector3f_y(vector) -> Graph:
    """Vector 3D Y Float

    Gets the value in the y component for the provided vector

    Args:
        vector: Graph of Vector3f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector3f_y_internal(vector_parsed)

def vector3f_z(vector) -> Graph:
    """Vector 3D Float Z

    Gets the value in the z component for the provided vector

    Args:
        vector: Graph of Vector3f
        

    Returns:
        Graph: A graph node producing a Float.
    """
    vector_parsed = parse_graph(vector)
    return _internal.vector3f_z_internal(vector_parsed)

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
    return _internal.xor_internal(bool1_parsed, bool2_parsed)


__all__ = [
    # Core classes
    "Context", "Graph", "Project", "Type",
    "TypeDefinition", "NodeDefinition", "NodeDefinitionInput", "ImageRecipe", "Bounds",
    # Constant functions
    "load_composition",
    "int_constant", "float_constant", "string_constant", "bool_constant",
    "byte_list_constant", "point2i_list_constant",
    # Node functions
    "abs",
    "and_",
    "bool_add_to_dictionary",
    "bool_if",
    "bounds2f_from_x_y_width_height",
    "bounds2f_height",
    "bounds2f_min_x",
    "bounds2f_min_y",
    "bounds2f_width",
    "bounds2i_from_x_y_width_height",
    "brush_solid",
    "byte_list_from_u_r_l",
    "color_profile_a_c_e_scg",
    "color_profile_b_t709",
    "color_profile_ok_lab_a",
    "color_profile_p3",
    "color_profile_p_n_g_s_r_g_b",
    "color_profile_s_r_g_b",
    "color_profile_s_r_g_b_linear",
    "color_profile_x_y_z",
    "color_representation_a_c_e_scg",
    "color_representation_from_color_profile_and_pixel_encoding",
    "color_representation_ok_lab_a",
    "color_representation_profile",
    "color_representation_r_g_b_b_t2020",
    "color_representation_s_r_g_b",
    "color_representation_s_r_g_b_linear",
    "color_representation_x_y_z_a",
    "composition_absolute_value",
    "composition_blend_add",
    "composition_blend_alpha",
    "composition_blend_max",
    "composition_blend_min",
    "composition_blend_multiply",
    "composition_blend_stencil",
    "composition_blend_subtract",
    "composition_bloom",
    "composition_bounds",
    "composition_box_blur",
    "composition_brightness_adjust",
    "composition_chroma_offset",
    "composition_color_convert",
    "composition_color_invert",
    "composition_color_representation",
    "composition_color_threshold",
    "composition_color_transformer_shader",
    "composition_contrast_adjustment",
    "composition_convolution",
    "composition_crop",
    "composition_duotone",
    "composition_film_grain",
    "composition_flip_horizontal",
    "composition_flip_vertical",
    "composition_from_asset",
    "composition_from_image",
    "composition_gaussian_blur",
    "composition_grayscale",
    "composition_halftone",
    "composition_if",
    "composition_kaleidoscope",
    "composition_l_curve",
    "composition_lightness_threshold",
    "composition_linear_transform",
    "composition_liquify",
    "composition_max_color",
    "composition_median",
    "composition_min_color",
    "composition_min_max_colors",
    "composition_monet_women_with_parasol",
    "composition_morphological_max",
    "composition_morphological_min",
    "composition_negative",
    "composition_nonlinear_r_g_b_blend_alpha",
    "composition_opacity_scale",
    "composition_painter",
    "composition_palette",
    "composition_palette_reduction",
    "composition_passthrough",
    "composition_pixelate",
    "composition_point_effect_shader",
    "composition_r_g_b_curve",
    "composition_render_to_image",
    "composition_rotate180",
    "composition_rotate90_clockwise",
    "composition_rotate90_counter_clockwise",
    "composition_s_a_m3_image",
    "composition_saturation_adjust",
    "composition_scanlines",
    "composition_segment",
    "composition_sharpen",
    "composition_sobel_edge_detection",
    "composition_spacial_effect_shader",
    "composition_swirl",
    "composition_target_white_kelvin",
    "composition_to_ok_lab_hist",
    "composition_transform",
    "composition_vibrance_adjustment",
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
    "or_",
    "painter_add_ellipse_with_render_style",
    "painter_add_path_with_render_style",
    "painter_add_rectangle_with_render_style",
    "painter_new",
    "path_cardinal_cubic_to_point",
    "path_catmull_rom_to_point",
    "path_line_to_point",
    "path_move_to_point",
    "path_new",
    "pi",
    "pixel_encoding_encoded",
    "pixel_encoding_linear",
    "pixel_encoding_premultiplied_alpha",
    "point2f_distance",
    "point2f_from_components",
    "point2i_distance",
    "point2i_from_components",
    "profiled_color_add_to_dictionary",
    "profiled_color_brightness_adjust",
    "profiled_color_chroma_offset",
    "profiled_color_from_ok_lab_a",
    "profiled_color_from_rgba_aces_cg",
    "profiled_color_from_rgba_srgb",
    "profiled_color_from_xyz_a",
    "profiled_color_grayscale",
    "profiled_color_lightness_curve",
    "profiled_color_saturation_adjust",
    "profiled_color_target_white",
    "profiled_color_to_ok_lab_a",
    "profiled_color_to_rgb_encoded_with_in_color_profile",
    "profiled_color_to_xyz_a",
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