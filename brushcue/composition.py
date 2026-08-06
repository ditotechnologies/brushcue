# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: d293e0c3ed90df2d5bdcff842d241728f3f83c3b882bcb4f6a7888c0e6142549
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import bounds2f

    from . import bounds2i_list

    from . import byte_list

    from . import color_representation

    from . import image

    from . import ok_lab_hist

    from . import profiled_color

    from . import profiled_color_list



class Composition(_GraphWrapper):
    """A composition to create an image."""

    def execute(self, context):

        return self._inner.execute(context).as_composition()


    @staticmethod
    def load(value) -> Composition:
        return Composition(input_parsers.parse_composition_graph(value))


    def absolute_value(self) -> Composition:
        """Composition Absolute Value

        Takes the absolute value of all the pixels in the image.
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        image_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_absolute_value_internal(image_parsed)

        return Composition(result)

    def blend_add(self, background, foreground_transform) -> Composition:
        """Composition Blend Add

        Adds the foreground and background images together using additive blending.
    
        Args:
            background: Graph of Composition
            foreground_transform: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        foreground_parsed = input_parsers.parse_graph(self)
        background_parsed = input_parsers.parse_graph(background)
        foreground_transform_parsed = input_parsers.parse_graph(foreground_transform)
        result = _internal.composition_blend_add_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

        return Composition(result)

    def blend_alpha(self, background, foreground_transform) -> Composition:
        """Composition Blend Alpha

        Blends between the foreground and background using the alpha component of the foreground. 1 is foreground. 0 is background.
    
        Args:
            background: Graph of Composition
            foreground_transform: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        foreground_parsed = input_parsers.parse_graph(self)
        background_parsed = input_parsers.parse_graph(background)
        foreground_transform_parsed = input_parsers.parse_graph(foreground_transform)
        result = _internal.composition_blend_alpha_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

        return Composition(result)

    def blend_max(self, background, foreground_transform) -> Composition:
        """Composition Blend Max

        Blends the foreground and background images using maximum value blending.
    
        Args:
            background: Graph of Composition
            foreground_transform: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        foreground_parsed = input_parsers.parse_graph(self)
        background_parsed = input_parsers.parse_graph(background)
        foreground_transform_parsed = input_parsers.parse_graph(foreground_transform)
        result = _internal.composition_blend_max_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

        return Composition(result)

    def blend_min(self, background, foreground_transform) -> Composition:
        """Composition Blend Min

        Blends the foreground and background images using minimum blending, taking the minimum value for each pixel.
    
        Args:
            background: Graph of Composition
            foreground_transform: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        foreground_parsed = input_parsers.parse_graph(self)
        background_parsed = input_parsers.parse_graph(background)
        foreground_transform_parsed = input_parsers.parse_graph(foreground_transform)
        result = _internal.composition_blend_min_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

        return Composition(result)

    def blend_multiply(self, background, foreground_transform) -> Composition:
        """Composition Blend Multiply

        Multiplies the foreground and background images together using multiply blending.
    
        Args:
            background: Graph of Composition
            foreground_transform: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        foreground_parsed = input_parsers.parse_graph(self)
        background_parsed = input_parsers.parse_graph(background)
        foreground_transform_parsed = input_parsers.parse_graph(foreground_transform)
        result = _internal.composition_blend_multiply_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

        return Composition(result)

    def blend_stencil(self, background, foreground_transform) -> Composition:
        """Composition Blend Stencil

        Blends the foreground and background images using stencil blending. When the foreground is over the background, the foreground's alpha and the background's r, g and b are used.
    
        Args:
            background: Graph of Composition
            foreground_transform: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        foreground_parsed = input_parsers.parse_graph(self)
        background_parsed = input_parsers.parse_graph(background)
        foreground_transform_parsed = input_parsers.parse_graph(foreground_transform)
        result = _internal.composition_blend_stencil_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

        return Composition(result)

    def blend_subtract(self, background, foreground_transform) -> Composition:
        """Composition Blend Subtract

        Subtracts the foreground image from the background image using subtractive blending.
    
        Args:
            background: Graph of Composition
            foreground_transform: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        foreground_parsed = input_parsers.parse_graph(self)
        background_parsed = input_parsers.parse_graph(background)
        foreground_transform_parsed = input_parsers.parse_graph(foreground_transform)
        result = _internal.composition_blend_subtract_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

        return Composition(result)

    def bloom(self, threshold, sigma, intensity) -> Composition:
        """Composition Bloom

        Adds a soft bloom glow by blurring the image's bright areas and additively blending them back over the original. Threshold selects bright areas (OkLab lightness), sigma controls glow spread, intensity scales the glow strength.
    
        Args:
            threshold: Graph of Float
            sigma: Graph of Float
            intensity: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        threshold_parsed = input_parsers.parse_float_graph(threshold)
        sigma_parsed = input_parsers.parse_float_graph(sigma)
        intensity_parsed = input_parsers.parse_float_graph(intensity)
        result = _internal.composition_bloom_internal(composition_parsed, threshold_parsed, sigma_parsed, intensity_parsed)

        return Composition(result)

    def bounds(self) -> bounds2f.Bounds2f:
        """Composition Bounds

        Computes the bounding box of a composition.
    
        Returns:
            Graph: A graph node producing a Bounds2f.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_bounds_internal(composition_parsed)

        from .bounds2f import Bounds2f
        return Bounds2f(result)

    def box_blur(self, dimension) -> Composition:
        """Composition Box Blur

        Applies a box blur to an image. Dimension is the size. 1 corresponding to 3x3, 2 5x5 and so on.
    
        Args:
            dimension: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        dimension_parsed = input_parsers.parse_int_graph(dimension)
        result = _internal.composition_box_blur_internal(composition_parsed, dimension_parsed)

        return Composition(result)

    def brightness_adjust(self, scale) -> Composition:
        """Composition Brightness Adjust

        Adjusts the brightness of an image by a given factor. Internally, works by modifying the L component of OkLab by multiplying it by the scale.
    
        Args:
            scale: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        scale_parsed = input_parsers.parse_float_graph(scale)
        result = _internal.composition_brightness_adjust_internal(composition_parsed, scale_parsed)

        return Composition(result)

    def chroma_offset(self, offset) -> Composition:
        """Composition Chroma Offset

        Applies a chroma offset to an image. This is done by modifying the a and b components of OkLab. For the vector, X applies to a, Y to to b.
    
        Args:
            offset: Graph of Vector2f
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        offset_parsed = input_parsers.parse_graph(offset)
        result = _internal.composition_chroma_offset_internal(composition_parsed, offset_parsed)

        return Composition(result)

    def color_convert(self, color_profile) -> Composition:
        """Composition Color Convert

        Converts a Composition from one color space to another.
    
        Args:
            color_profile: Graph of ColorProfile
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        color_profile_parsed = input_parsers.parse_graph(color_profile)
        result = _internal.composition_color_convert_internal(composition_parsed, color_profile_parsed)

        return Composition(result)

    def color_invert(self) -> Composition:
        """Composition Color Invert

        Applies a color invert operation to a composition. Taking 1 and subtracting each RGB operation against it. Works in linear color.
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_color_invert_internal(composition_parsed)

        return Composition(result)

    def color_representation(self) -> color_representation.ColorRepresentation:
        """Composition Color Representation

        Gets the color representation associated with a Composition
    
        Returns:
            Graph: A graph node producing a ColorRepresentation.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_color_representation_internal(composition_parsed)

        from .color_representation import ColorRepresentation
        return ColorRepresentation(result)

    def color_threshold(self, threshold) -> Composition:
        """Composition Color Threshold

        Applies a color threshold to a Composition
    
        Args:
            threshold: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        threshold_parsed = input_parsers.parse_float_graph(threshold)
        result = _internal.composition_color_threshold_internal(composition_parsed, threshold_parsed)

        return Composition(result)

    def color_transformer_shader(self, function_body, helpers, input_color_representation, output_color_representation, inputs) -> Composition:
        """Composition Color Transformer Shader

        Defines a custom shader that takes an input color and then transforms that color to an output color.
    
        Args:
            function_body: Graph of String
            helpers: Graph of String
            input_color_representation: Graph of ColorRepresentation
            output_color_representation: Graph of ColorRepresentation
            inputs: Graph of Dictionary
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        function_body_parsed = input_parsers.parse_string_graph(function_body)
        helpers_parsed = input_parsers.parse_string_graph(helpers)
        input_color_representation_parsed = input_parsers.parse_graph(input_color_representation)
        output_color_representation_parsed = input_parsers.parse_graph(output_color_representation)
        inputs_parsed = input_parsers.parse_graph(inputs)
        result = _internal.composition_color_transformer_shader_internal(composition_parsed, function_body_parsed, helpers_parsed, input_color_representation_parsed, output_color_representation_parsed, inputs_parsed)

        return Composition(result)

    def connected_component_boxes(self) -> bounds2i_list.Bounds2iList:
        """Composition Connected Component Boxes

        Finds boxes with a r alpha channel value greater than 0.5 in the image. Recommended to use a binary image for this.
    
        Returns:
            Graph: A graph node producing a Bounds2iList.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_connected_component_boxes_internal(composition_parsed)

        from .bounds2i_list import Bounds2iList
        return Bounds2iList(result)

    def contrast_adjustment(self, contrast) -> Composition:
        """Composition Contrast Adjustment

        Adjusts the contrast of a Composition
    
        Args:
            contrast: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        contrast_parsed = input_parsers.parse_float_graph(contrast)
        result = _internal.composition_contrast_adjustment_internal(composition_parsed, contrast_parsed)

        return Composition(result)

    def convolution(self, kernel, kernel_width, kernel_height) -> Composition:
        """Composition Convolution

        Performs a convolution on an composition
    
        Args:
            kernel: Graph of FloatList
            kernel_width: Graph of Int
            kernel_height: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        kernel_parsed = input_parsers.parse_graph(kernel)
        kernel_width_parsed = input_parsers.parse_int_graph(kernel_width)
        kernel_height_parsed = input_parsers.parse_int_graph(kernel_height)
        result = _internal.composition_convolution_internal(composition_parsed, kernel_parsed, kernel_width_parsed, kernel_height_parsed)

        return Composition(result)

    def crop(self, rect) -> Composition:
        """Composition Crop

        Applies a crop to a Composition
    
        Args:
            rect: Graph of Bounds2f
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        rect_parsed = input_parsers.parse_graph(rect)
        result = _internal.composition_crop_internal(composition_parsed, rect_parsed)

        return Composition(result)

    def duotone(self, threshold, color_1, color_2) -> Composition:
        """Composition Duotone

        Creates a duotone effect. Colors below the threshold will be color 1, colors above will be color 2.
    
        Args:
            threshold: Graph of Float
            color_1: Graph of ProfiledColor
            color_2: Graph of ProfiledColor
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        threshold_parsed = input_parsers.parse_float_graph(threshold)
        color_1_parsed = input_parsers.parse_graph(color_1)
        color_2_parsed = input_parsers.parse_graph(color_2)
        result = _internal.composition_duotone_internal(composition_parsed, threshold_parsed, color_1_parsed, color_2_parsed)

        return Composition(result)

    def film_grain(self, grain_strength, fine_grain_frequency, fine_weight, medium_grain_frequency, medium_weight, high_grain_frequency, high_weight) -> Composition:
        """Composition Film Grain

        adds multi-octave value-noise film grain in OkLabA - grain_strength controls the overall intensity, and the fine/medium/high frequency and weight pairs control the size and contribution of each grain octave.
    
        Args:
            grain_strength: Graph of Float
            fine_grain_frequency: Graph of Float
            fine_weight: Graph of Float
            medium_grain_frequency: Graph of Float
            medium_weight: Graph of Float
            high_grain_frequency: Graph of Float
            high_weight: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        grain_strength_parsed = input_parsers.parse_float_graph(grain_strength)
        fine_grain_frequency_parsed = input_parsers.parse_float_graph(fine_grain_frequency)
        fine_weight_parsed = input_parsers.parse_float_graph(fine_weight)
        medium_grain_frequency_parsed = input_parsers.parse_float_graph(medium_grain_frequency)
        medium_weight_parsed = input_parsers.parse_float_graph(medium_weight)
        high_grain_frequency_parsed = input_parsers.parse_float_graph(high_grain_frequency)
        high_weight_parsed = input_parsers.parse_float_graph(high_weight)
        result = _internal.composition_film_grain_internal(composition_parsed, grain_strength_parsed, fine_grain_frequency_parsed, fine_weight_parsed, medium_grain_frequency_parsed, medium_weight_parsed, high_grain_frequency_parsed, high_weight_parsed)

        return Composition(result)

    def flip_horizontal(self) -> Composition:
        """Composition Flip Horizontal

        Flips the image along the horizontal axis
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_flip_horizontal_internal(composition_parsed)

        return Composition(result)

    def flip_vertical(self) -> Composition:
        """Composition Flip Vertical

        Flips the image vertically
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_flip_vertical_internal(composition_parsed)

        return Composition(result)

    @staticmethod
    def from_asset(asset_id) -> Composition:
        """Composition from Asset

        Creates a composition from an asset in your catalog.
    
        Args:
            asset_id: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        asset_id_parsed = input_parsers.parse_int_graph(asset_id)
        result = _internal.composition_from_asset_internal(asset_id_parsed)

        return Composition(result)

    @staticmethod
    def from_image(image) -> Composition:
        """Composition from Image

        Creates an composition out of an image
    
        Args:
            image: Graph of Image
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        image_parsed = input_parsers.parse_graph(image)
        result = _internal.composition_from_image_internal(image_parsed)

        return Composition(result)

    def gaussian_blur(self, sigma) -> Composition:
        """Composition Gaussian Blur

        Applies a gaussian blur to an image. Sigma controls the blur intensity.
    
        Args:
            sigma: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        sigma_parsed = input_parsers.parse_float_graph(sigma)
        result = _internal.composition_gaussian_blur_internal(composition_parsed, sigma_parsed)

        return Composition(result)

    def grayscale(self) -> Composition:
        """Composition Grayscale

        Applies grayscale to a Composition
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_grayscale_internal(composition_parsed)

        return Composition(result)

    def halftone(self, pixel_size, foreground_color, background_color) -> Composition:
        """Composition Halftone

        Applies a halftone effect to a composition, tiling it into cells and painting a foreground-colored dot in each cell whose radius grows as the cell darkens, over a background color.
    
        Args:
            pixel_size: Graph of Int
            foreground_color: Graph of ProfiledColor
            background_color: Graph of ProfiledColor
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        pixel_size_parsed = input_parsers.parse_int_graph(pixel_size)
        foreground_color_parsed = input_parsers.parse_graph(foreground_color)
        background_color_parsed = input_parsers.parse_graph(background_color)
        result = _internal.composition_halftone_internal(composition_parsed, pixel_size_parsed, foreground_color_parsed, background_color_parsed)

        return Composition(result)

    @staticmethod
    def if_(bool, input_1, input_2) -> Composition:
        """Composition If

        If the boolean is true returns input 1, otherwise input 2. Type: Composition
    
        Args:
            bool: Graph of Bool
            input_1: Graph of Composition
            input_2: Graph of Composition
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        bool_parsed = input_parsers.parse_bool_graph(bool)
        input_1_parsed = input_parsers.parse_graph(input_1)
        input_2_parsed = input_parsers.parse_graph(input_2)
        result = _internal.composition_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

        return Composition(result)

    def kaleidoscope(self, segments, rotation, warp, warp_frequency) -> Composition:
        """Composition Kaleidoscope

        Applies a kaleidoscope effect, folding the image into mirrored wedges around the center. segments controls the number of wedges, rotation spins the pattern, and warp/warp_frequency add a radial glass-like distortion.
    
        Args:
            segments: Graph of Float
            rotation: Graph of Float
            warp: Graph of Float
            warp_frequency: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        segments_parsed = input_parsers.parse_float_graph(segments)
        rotation_parsed = input_parsers.parse_float_graph(rotation)
        warp_parsed = input_parsers.parse_float_graph(warp)
        warp_frequency_parsed = input_parsers.parse_float_graph(warp_frequency)
        result = _internal.composition_kaleidoscope_internal(composition_parsed, segments_parsed, rotation_parsed, warp_parsed, warp_frequency_parsed)

        return Composition(result)

    def l_curve(self, l_curve) -> Composition:
        """Composition Lightness Curve

        Applies a curve to the L component in an OkLab color. Adjusting the lightness of the image.
    
        Args:
            l_curve: Graph of Curve
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        l_curve_parsed = input_parsers.parse_graph(l_curve)
        result = _internal.composition_l_curve_internal(composition_parsed, l_curve_parsed)

        return Composition(result)

    def lightness_threshold(self, threshold) -> Composition:
        """Composition Lightness Threshold

        Thresholds a Composition by OkLab lightness, producing an opaque white mask where lightness exceeds the threshold and transparent black elsewhere.
    
        Args:
            threshold: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        threshold_parsed = input_parsers.parse_float_graph(threshold)
        result = _internal.composition_lightness_threshold_internal(composition_parsed, threshold_parsed)

        return Composition(result)

    def linear_transform(self, entry_0_0, entry_0_1, entry_0_2, entry_0_3, entry_1_0, entry_1_1, entry_1_2, entry_1_3, entry_2_0, entry_2_1, entry_2_2, entry_2_3, entry_3_0, entry_3_1, entry_3_2, entry_3_3) -> Composition:
        """Composition RGBA Linear Transform

        Applies a linear transform to a Composition's RGBA values. Before application, will convert to a linear version of the color profile and will convert to an RGB profile if needed.
    
        Args:
            entry_0_0: Graph of Float
            entry_0_1: Graph of Float
            entry_0_2: Graph of Float
            entry_0_3: Graph of Float
            entry_1_0: Graph of Float
            entry_1_1: Graph of Float
            entry_1_2: Graph of Float
            entry_1_3: Graph of Float
            entry_2_0: Graph of Float
            entry_2_1: Graph of Float
            entry_2_2: Graph of Float
            entry_2_3: Graph of Float
            entry_3_0: Graph of Float
            entry_3_1: Graph of Float
            entry_3_2: Graph of Float
            entry_3_3: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        entry_0_0_parsed = input_parsers.parse_float_graph(entry_0_0)
        entry_0_1_parsed = input_parsers.parse_float_graph(entry_0_1)
        entry_0_2_parsed = input_parsers.parse_float_graph(entry_0_2)
        entry_0_3_parsed = input_parsers.parse_float_graph(entry_0_3)
        entry_1_0_parsed = input_parsers.parse_float_graph(entry_1_0)
        entry_1_1_parsed = input_parsers.parse_float_graph(entry_1_1)
        entry_1_2_parsed = input_parsers.parse_float_graph(entry_1_2)
        entry_1_3_parsed = input_parsers.parse_float_graph(entry_1_3)
        entry_2_0_parsed = input_parsers.parse_float_graph(entry_2_0)
        entry_2_1_parsed = input_parsers.parse_float_graph(entry_2_1)
        entry_2_2_parsed = input_parsers.parse_float_graph(entry_2_2)
        entry_2_3_parsed = input_parsers.parse_float_graph(entry_2_3)
        entry_3_0_parsed = input_parsers.parse_float_graph(entry_3_0)
        entry_3_1_parsed = input_parsers.parse_float_graph(entry_3_1)
        entry_3_2_parsed = input_parsers.parse_float_graph(entry_3_2)
        entry_3_3_parsed = input_parsers.parse_float_graph(entry_3_3)
        result = _internal.composition_linear_transform_internal(composition_parsed, entry_0_0_parsed, entry_0_1_parsed, entry_0_2_parsed, entry_0_3_parsed, entry_1_0_parsed, entry_1_1_parsed, entry_1_2_parsed, entry_1_3_parsed, entry_2_0_parsed, entry_2_1_parsed, entry_2_2_parsed, entry_2_3_parsed, entry_3_0_parsed, entry_3_1_parsed, entry_3_2_parsed, entry_3_3_parsed)

        return Composition(result)

    def liquify(self, amplitude, frequency) -> Composition:
        """Composition Liquify

        Applies a sinusoidal liquify distortion to this composition, displacing pixels by a wave whose size is controlled by amplitude and whose density is controlled by frequency.
    
        Args:
            amplitude: Graph of Float
            frequency: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        amplitude_parsed = input_parsers.parse_float_graph(amplitude)
        frequency_parsed = input_parsers.parse_float_graph(frequency)
        result = _internal.composition_liquify_internal(composition_parsed, amplitude_parsed, frequency_parsed)

        return Composition(result)

    def max_color(self) -> profiled_color.ProfiledColor:
        """Composition Max Color

        Computes the maximum color in a composition. Works by finding the maximum L, a and b and alpha components of an OkLabA color.
    
        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_max_color_internal(composition_parsed)

        from .profiled_color import ProfiledColor
        return ProfiledColor(result)

    def median(self, kernel_size) -> Composition:
        """Composition Median

        Applies a per-channel median filter to a composition over a square window, reducing noise while preserving edges. kernel_size controls the window size (window width is 2*kernel_size-1).
    
        Args:
            kernel_size: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        kernel_size_parsed = input_parsers.parse_int_graph(kernel_size)
        result = _internal.composition_median_internal(composition_parsed, kernel_size_parsed)

        return Composition(result)

    def min_color(self) -> profiled_color.ProfiledColor:
        """Composition Min Color

        Computes the minimum color in a composition. Works by finding the minimum L, a and b and alpha components of an OkLabA color.
    
        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_min_color_internal(composition_parsed)

        from .profiled_color import ProfiledColor
        return ProfiledColor(result)

    def min_max_colors(self) -> profiled_color_list.ProfiledColorList:
        """Composition Min Max Colors

        Computes the minimum and maximum colors in a composition. Works by finding the minimum and maximum L, a and b and alpha components of an OkLabA color.
    
        Returns:
            Graph: A graph node producing a ProfiledColorList.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_min_max_colors_internal(composition_parsed)

        from .profiled_color_list import ProfiledColorList
        return ProfiledColorList(result)

    @staticmethod
    def monet_women_with_parasol() -> Composition:
        """Monet's Women with a Parasol

        Creates a composition from Monet's "Women with a Parasol" painting. Used frequently as a test asset.
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        result = _internal.composition_monet_women_with_parasol_internal()

        return Composition(result)

    def morphological_max(self, dimension) -> Composition:
        """Composition Morphological Max

        Apples a morphological max operation.
    
        Args:
            dimension: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        dimension_parsed = input_parsers.parse_int_graph(dimension)
        result = _internal.composition_morphological_max_internal(composition_parsed, dimension_parsed)

        return Composition(result)

    def morphological_min(self, dimension) -> Composition:
        """Composition Morphological Min

        Apples a morphological min operation.
    
        Args:
            dimension: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        dimension_parsed = input_parsers.parse_int_graph(dimension)
        result = _internal.composition_morphological_min_internal(composition_parsed, dimension_parsed)

        return Composition(result)

    def negative(self) -> Composition:
        """Composition Negative

        Creates the effect of a negative image by subracting from each component of the image.
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_negative_internal(composition_parsed)

        return Composition(result)

    def nonlinear_rgb_blend_alpha(self, background, foreground_transform) -> Composition:
        """Composition Nonlinear RGB Blend Alpha

        A specialized version of CompositionBlendAlpha. Blends in a non-linear RGB.
    
        Args:
            background: Graph of Composition
            foreground_transform: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        foreground_parsed = input_parsers.parse_graph(self)
        background_parsed = input_parsers.parse_graph(background)
        foreground_transform_parsed = input_parsers.parse_graph(foreground_transform)
        result = _internal.composition_nonlinear_r_g_b_blend_alpha_internal(foreground_parsed, background_parsed, foreground_transform_parsed)

        return Composition(result)

    def opacity_scales(self, scale) -> Composition:
        """Composition Opacity Scale

        Changes the opacity of an image by multiplying it by a scalar.
    
        Args:
            scale: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        scale_parsed = input_parsers.parse_float_graph(scale)
        result = _internal.composition_opacity_scale_internal(composition_parsed, scale_parsed)

        return Composition(result)

    @staticmethod
    def painter(painter) -> Composition:
        """Composition Painter

        Creates a composition from a painter.
    
        Args:
            painter: Graph of Painter
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        painter_parsed = input_parsers.parse_graph(painter)
        result = _internal.composition_painter_internal(painter_parsed)

        return Composition(result)

    def to_palette(self, size) -> profiled_color_list.ProfiledColorList:
        """Composition Palette

        Generates a palette of the most dominant colors of a composition.
    
        Args:
            size: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a ProfiledColorList.
        """
        composition_parsed = input_parsers.parse_graph(self)
        size_parsed = input_parsers.parse_int_graph(size)
        result = _internal.composition_palette_internal(composition_parsed, size_parsed)

        from .profiled_color_list import ProfiledColorList
        return ProfiledColorList(result)

    def palette_reduction(self, palette) -> Composition:
        """Composition Palette Reduction

        Reduces the number of colors in a composition to a specified palette.
    
        Args:
            palette: Graph of ProfiledColorList
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        palette_parsed = input_parsers.parse_graph(palette)
        result = _internal.composition_palette_reduction_internal(composition_parsed, palette_parsed)

        return Composition(result)

    def passthrough(self) -> Composition:
        """Composition Passthrough

        Responds with the value provided. Doing nothing to it.
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        value_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_passthrough_internal(value_parsed)

        return Composition(result)

    def pixelate(self, pixel_size) -> Composition:
        """Composition Pixelate

        Applies a pixelation effect to a composition.
    
        Args:
            pixel_size: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        pixel_size_parsed = input_parsers.parse_int_graph(pixel_size)
        result = _internal.composition_pixelate_internal(composition_parsed, pixel_size_parsed)

        return Composition(result)

    def point_effect_shader(self, function_body, helpers, effect_center_point, effect_radius, inputs, working_color_representation) -> Composition:
        """Composition Point Effect Shader

        Runs a custom shader over a circular region around an effect center point.
    
        Args:
            function_body: Graph of String
            helpers: Graph of String
            effect_center_point: Graph of Point2f
            effect_radius: Graph of Float
            inputs: Graph of Dictionary
            working_color_representation: Graph of ColorRepresentation
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        function_body_parsed = input_parsers.parse_string_graph(function_body)
        helpers_parsed = input_parsers.parse_string_graph(helpers)
        effect_center_point_parsed = input_parsers.parse_graph(effect_center_point)
        effect_radius_parsed = input_parsers.parse_float_graph(effect_radius)
        inputs_parsed = input_parsers.parse_graph(inputs)
        working_color_representation_parsed = input_parsers.parse_graph(working_color_representation)
        result = _internal.composition_point_effect_shader_internal(composition_parsed, function_body_parsed, helpers_parsed, effect_center_point_parsed, effect_radius_parsed, inputs_parsed, working_color_representation_parsed)

        return Composition(result)

    def r_g_b_curve(self, r_curve, g_curve, b_curve) -> Composition:
        """Composition RGB Curve

        Applies a curve to the R, G, and B components
    
        Args:
            r_curve: Graph of Curve
            g_curve: Graph of Curve
            b_curve: Graph of Curve
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        r_curve_parsed = input_parsers.parse_graph(r_curve)
        g_curve_parsed = input_parsers.parse_graph(g_curve)
        b_curve_parsed = input_parsers.parse_graph(b_curve)
        result = _internal.composition_r_g_b_curve_internal(composition_parsed, r_curve_parsed, g_curve_parsed, b_curve_parsed)

        return Composition(result)

    def render_to_image(self) -> image.Image:
        """Composition Render to Image

        Renders a Composition to an Image
    
        Returns:
            Graph: A graph node producing a Image.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_render_to_image_internal(composition_parsed)

        from .image import Image
        return Image(result)

    def rotate_180(self) -> Composition:
        """Composition Rotate 180

        Rotates the image 180 degrees
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_rotate180_internal(composition_parsed)

        return Composition(result)

    def rotate_90_clockwise(self) -> Composition:
        """Composition Rotate 90 Clockwise

        Rotates the image 90 degrees clockwise
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_rotate90_clockwise_internal(composition_parsed)

        return Composition(result)

    def rotate_90_counter_clockwise(self) -> Composition:
        """Composition Rotate 90 Counter Clockwise

        Rotates the image 90 degrees counter-clockwise
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_rotate90_counter_clockwise_internal(composition_parsed)

        return Composition(result)

    def sam3_image(self, prompt, positive_points, negative_points) -> byte_list.ByteList:
        """Composition SAM3 Image

        Runs the SAM3 model on an image
    
        Args:
            prompt: Graph of String
            positive_points: Graph of Point2iList
            negative_points: Graph of Point2iList
            
    
        Returns:
            Graph: A graph node producing a ByteList.
        """
        composition_parsed = input_parsers.parse_graph(self)
        prompt_parsed = input_parsers.parse_string_graph(prompt)
        positive_points_parsed = input_parsers.parse_graph(positive_points)
        negative_points_parsed = input_parsers.parse_graph(negative_points)
        result = _internal.composition_s_a_m3_image_internal(composition_parsed, prompt_parsed, positive_points_parsed, negative_points_parsed)

        from .byte_list import ByteList
        return ByteList(result)

    def saturation_adjust(self, scale) -> Composition:
        """Composition Saturation Adjust

        Adjusts the saturation of an image by a given factor. Internally, scales the chroma components in OkLab color space.
    
        Args:
            scale: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        scale_parsed = input_parsers.parse_float_graph(scale)
        result = _internal.composition_saturation_adjust_internal(composition_parsed, scale_parsed)

        return Composition(result)

    def scanlines(self, size, beam_power, line_offset, intensity) -> Composition:
        """Composition Scanlines

        Applies a CRT-style scanline effect, darkening the composition in horizontal bands whose spacing is set by size, sharpness by beam power, vertical phase by line offset, and overall strength by intensity.
    
        Args:
            size: Graph of Float
            beam_power: Graph of Float
            line_offset: Graph of Float
            intensity: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        size_parsed = input_parsers.parse_float_graph(size)
        beam_power_parsed = input_parsers.parse_float_graph(beam_power)
        line_offset_parsed = input_parsers.parse_float_graph(line_offset)
        intensity_parsed = input_parsers.parse_float_graph(intensity)
        result = _internal.composition_scanlines_internal(composition_parsed, size_parsed, beam_power_parsed, line_offset_parsed, intensity_parsed)

        return Composition(result)

    def segment(self, prompt, positive_points, negative_points) -> Composition:
        """Composition Segment

        Segments objects in a composition using SAM3. Accepts a text prompt and lists of positive/negative click points.
    
        Args:
            prompt: Graph of String
            positive_points: Graph of Point2iList
            negative_points: Graph of Point2iList
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        prompt_parsed = input_parsers.parse_string_graph(prompt)
        positive_points_parsed = input_parsers.parse_graph(positive_points)
        negative_points_parsed = input_parsers.parse_graph(negative_points)
        result = _internal.composition_segment_internal(composition_parsed, prompt_parsed, positive_points_parsed, negative_points_parsed)

        return Composition(result)

    def sharpen(self, radius, strength) -> Composition:
        """Composition Sharpen

        Applies a sharpen filter to the composition.
    
        Args:
            radius: Graph of Float
            strength: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        radius_parsed = input_parsers.parse_float_graph(radius)
        strength_parsed = input_parsers.parse_float_graph(strength)
        result = _internal.composition_sharpen_internal(composition_parsed, radius_parsed, strength_parsed)

        return Composition(result)

    def sobel_edge_detection(self) -> Composition:
        """Composition Sobel Edge Detection

        Applies Sobel edge detection to an image.
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_sobel_edge_detection_internal(composition_parsed)

        return Composition(result)

    def spacial_effect_shader(self, function_body, helpers, max_displacement, inputs, working_color_representation) -> Composition:
        """Composition Spacial Effect Shader

        Runs a custom shader over an input that can spatially displace pixels by up to a maximum displacement.
    
        Args:
            function_body: Graph of String
            helpers: Graph of String
            max_displacement: Graph of Float
            inputs: Graph of Dictionary
            working_color_representation: Graph of ColorRepresentation
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        function_body_parsed = input_parsers.parse_string_graph(function_body)
        helpers_parsed = input_parsers.parse_string_graph(helpers)
        max_displacement_parsed = input_parsers.parse_float_graph(max_displacement)
        inputs_parsed = input_parsers.parse_graph(inputs)
        working_color_representation_parsed = input_parsers.parse_graph(working_color_representation)
        result = _internal.composition_spacial_effect_shader_internal(composition_parsed, function_body_parsed, helpers_parsed, max_displacement_parsed, inputs_parsed, working_color_representation_parsed)

        return Composition(result)

    def swirl(self, center, radius, amount) -> Composition:
        """Composition Swirl

        Applies a swirl distortion to this composition
    
        Args:
            center: Graph of Vector2f
            radius: Graph of Float
            amount: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        center_parsed = input_parsers.parse_graph(center)
        radius_parsed = input_parsers.parse_float_graph(radius)
        amount_parsed = input_parsers.parse_float_graph(amount)
        result = _internal.composition_swirl_internal(composition_parsed, center_parsed, radius_parsed, amount_parsed)

        return Composition(result)

    def target_white_kelvin(self, kelvin) -> Composition:
        """Composition Target White Kelvin

        Sets the image white point to the value specified in Kelvin. The profile connection white point is D50, so you will only see changes as you move away from that.
    
        Args:
            kelvin: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        kelvin_parsed = input_parsers.parse_float_graph(kelvin)
        result = _internal.composition_target_white_kelvin_internal(composition_parsed, kelvin_parsed)

        return Composition(result)

    def to_ok_lab_hist(self) -> ok_lab_hist.OkLabHist:
        """Composition to OkLab Histogram

        Creates an OkLab Histogram from the colors in a Composition.
    
        Returns:
            Graph: A graph node producing a OkLabHist.
        """
        composition_parsed = input_parsers.parse_graph(self)
        result = _internal.composition_to_ok_lab_hist_internal(composition_parsed)

        from .ok_lab_hist import OkLabHist
        return OkLabHist(result)

    def transform(self, transform) -> Composition:
        """Composition Transform

        Applies a 2D transform to a Composition.
    
        Args:
            transform: Graph of Transform2
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        transform_parsed = input_parsers.parse_graph(transform)
        result = _internal.composition_transform_internal(composition_parsed, transform_parsed)

        return Composition(result)

    def vibrance_adjustment(self, strength) -> Composition:
        """Composition Vibrance Adjustment

        Adjusts the vibrance of an image by a given strength. Internally, boosts chroma in OkLab color space adaptively, applying more boost to less saturated colors.
    
        Args:
            strength: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        strength_parsed = input_parsers.parse_float_graph(strength)
        result = _internal.composition_vibrance_adjustment_internal(composition_parsed, strength_parsed)

        return Composition(result)

    def vignette(self, center, radius_x, radius_y, softness, strength) -> Composition:
        """Composition Vignette

        darkens the area outside an ellipse - center is the bright spot in pixel coordinates, radius_x and radius_y are the ellipse semi-axes in pixels where the falloff starts, softness is the width of the fade-out band in pixels, and strength (0-1) defines how dark the edges become at maximum.
    
        Args:
            center: Graph of Vector2f
            radius_x: Graph of Float
            radius_y: Graph of Float
            softness: Graph of Float
            strength: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        center_parsed = input_parsers.parse_graph(center)
        radius_x_parsed = input_parsers.parse_float_graph(radius_x)
        radius_y_parsed = input_parsers.parse_float_graph(radius_y)
        softness_parsed = input_parsers.parse_float_graph(softness)
        strength_parsed = input_parsers.parse_float_graph(strength)
        result = _internal.composition_vignette_internal(composition_parsed, center_parsed, radius_x_parsed, radius_y_parsed, softness_parsed, strength_parsed)

        return Composition(result)

    def zoom_blur(self, center, strength, falloff, effect_radius) -> Composition:
        """Composition Zoom Blur

        Performs a zoom blur on this composition
    
        Args:
            center: Graph of Vector2f
            strength: Graph of Float
            falloff: Graph of Float
            effect_radius: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Composition.
        """
        composition_parsed = input_parsers.parse_graph(self)
        center_parsed = input_parsers.parse_graph(center)
        strength_parsed = input_parsers.parse_float_graph(strength)
        falloff_parsed = input_parsers.parse_float_graph(falloff)
        effect_radius_parsed = input_parsers.parse_float_graph(effect_radius)
        result = _internal.composition_zoom_blur_internal(composition_parsed, center_parsed, strength_parsed, falloff_parsed, effect_radius_parsed)

        return Composition(result)

