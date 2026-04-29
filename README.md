# Brushcue

![PyPI - Version](https://img.shields.io/pypi/v/brushcue) 

Brushcue is a GPU-accelerated image editing library for Python. Every operation is a composable graph node — adjust color and tone, apply filters and blurs, composite images with a full set of blend modes, transform and crop, run ML-powered segmentation, or write custom GPU shaders. Chain nodes together and call `.execute()` once to run the whole pipeline.

### Examples of things you can make

<table><tr>
<td align="center"><img src="https://www.brushcue.com/tools/rgb-color-shift/animation.webp" width="180"></td>
<td align="center"><img src="https://www.brushcue.com/tools/pixelate/animation.webp" width="180"></td>
<td align="center"><img src="https://www.brushcue.com/tools/zoom-blur/animation.webp" width="180"></td>
<td align="center"><img src="https://www.brushcue.com/tools/camera-moving-distortion/animation.webp" width="180"></td>
</tr></table>

## Install

```bash
pip install brushcue
```

If a GPU is not available on your system, a CPU-only build is also available. We recommend trying the standard `brushcue` package first — on many Linux environments, GPU emulation is supported and it will work without a physical GPU. If that is not an option, the CPU build can be used, though certain operations may fail without GPU support.

```bash
pip install brushcue-cpu
```

## Documentation

The full documentation is available [here](https://www.brushcue.com/docs/py).

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

## Examples

All the [BrushCue tools](https://www.brushcue.com/tools) are available as examples to learn how to use our API. 

- [Add Frame](https://www.brushcue.com/docs/py/examples/add-frame)
- [Blue Channel](https://www.brushcue.com/docs/py/examples/blue-channel)
- [Box Blur](https://www.brushcue.com/docs/py/examples/box-blur)
- [Brightness Adjust](https://www.brushcue.com/docs/py/examples/brightness-adjust)
- [Brightness Contrast Adjust](https://www.brushcue.com/docs/py/examples/brightness-contrast-adjust)
- [Camera Moving Distortion](https://www.brushcue.com/docs/py/examples/camera-moving-distortion)
- [Chroma Offset](https://www.brushcue.com/docs/py/examples/chroma-offset)
- [Coachella Aesthetic](https://www.brushcue.com/docs/py/examples/coachella-aesthetic)
- [Color Invert](https://www.brushcue.com/docs/py/examples/color-invert)
- [Color Rectangle](https://www.brushcue.com/docs/py/examples/color-rectangle)
- [Color Threshold](https://www.brushcue.com/docs/py/examples/color-threshold)
- [Convert To BT 709](https://www.brushcue.com/docs/py/examples/convert-to-bt-709)
- [Convert To Display P3](https://www.brushcue.com/docs/py/examples/convert-to-display-p3)
- [Convert To sRGB](https://www.brushcue.com/docs/py/examples/convert-to-srgb)
- [Exposure Adjust](https://www.brushcue.com/docs/py/examples/exposure-adjust)
- [Film Grain](https://www.brushcue.com/docs/py/examples/film-grain)
- [Film Noir](https://www.brushcue.com/docs/py/examples/film-noir)
- [Gaussian Blur](https://www.brushcue.com/docs/py/examples/gaussian-blur)
- [Grayscale](https://www.brushcue.com/docs/py/examples/grayscale)
- [Green Channel](https://www.brushcue.com/docs/py/examples/green-channel)
- [Halftone](https://www.brushcue.com/docs/py/examples/halftone)
- [High Contrast Grayscale](https://www.brushcue.com/docs/py/examples/high-contrast-grayscale)
- [Horizontal Mirror](https://www.brushcue.com/docs/py/examples/horizontal-mirror)
- [Kaleidoscope](https://www.brushcue.com/docs/py/examples/kaleidoscope)
- [Kelvin Tuner](https://www.brushcue.com/docs/py/examples/kelvin-tuner)
- [Lightness Threshold](https://www.brushcue.com/docs/py/examples/lightness-threshold)
- [Linear Transform](https://www.brushcue.com/docs/py/examples/linear-transform)
- [Liquify](https://www.brushcue.com/docs/py/examples/liquify)
- [Median Filter](https://www.brushcue.com/docs/py/examples/median-filter)
- [Oval](https://www.brushcue.com/docs/py/examples/oval)
- [Pixelate](https://www.brushcue.com/docs/py/examples/pixelate)
- [Red Channel](https://www.brushcue.com/docs/py/examples/red-channel)
- [RGB Color Mix Aesthetic](https://www.brushcue.com/docs/py/examples/rgb-color-mix-aesthetic)
- [RGB Color Shift](https://www.brushcue.com/docs/py/examples/rgb-color-shift)
- [Rose Tint](https://www.brushcue.com/docs/py/examples/rose-tint)
- [Rotate 180](https://www.brushcue.com/docs/py/examples/rotate-180)
- [Rotate 90 Clockwise](https://www.brushcue.com/docs/py/examples/rotate-90-clockwise)
- [Rotate 90 Counter Clockwise](https://www.brushcue.com/docs/py/examples/rotate-90-counter-clockwise)
- [Saturation Adjust](https://www.brushcue.com/docs/py/examples/saturation-adjust)
- [Scale By Factor](https://www.brushcue.com/docs/py/examples/scale-by-factor)
- [Sepia](https://www.brushcue.com/docs/py/examples/sepia)
- [Shadow Tint](https://www.brushcue.com/docs/py/examples/shadow-tint)
- [Shredder](https://www.brushcue.com/docs/py/examples/shredder)
- [Sobel Edge Detection](https://www.brushcue.com/docs/py/examples/sobel-edge-detection)
- [Sparkle Vignette](https://www.brushcue.com/docs/py/examples/sparkle-vignette)
- [Swirl](https://www.brushcue.com/docs/py/examples/swirl)
- [Vertical Mirror](https://www.brushcue.com/docs/py/examples/vertical-mirror)
- [Vibrancy](https://www.brushcue.com/docs/py/examples/vibrancy)
- [Vignette](https://www.brushcue.com/docs/py/examples/vignette)
- [Warmth Adjust](https://www.brushcue.com/docs/py/examples/warmth-adjust)
- [Zoom Blur](https://www.brushcue.com/docs/py/examples/zoom-blur)
