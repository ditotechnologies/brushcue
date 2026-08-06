# Brushcue

![PyPI - Version](https://img.shields.io/pypi/v/brushcue) 

Brushcue is a GPU-accelerated image editing library for Python. Every operation is a composable graph node — adjust color and tone, apply filters and blurs, composite images with a full set of blend modes, transform and crop, run ML-powered segmentation, or write custom GPU shaders. Chain nodes together and call `.execute()` once to run the whole pipeline.

### Examples of things you can make

<table><tr>
<td align="center"><img src="https://www.brushcue.com/tools/swirl/animation.webp" width="180"></td>
<td align="center"><img src="https://www.brushcue.com/tools/crt-monitor-filter/animation.webp" width="180"></td>
<td align="center"><img src="https://www.brushcue.com/tools/pixelate/animation.webp" width="180"></td>
<td align="center"><img src="https://www.brushcue.com/tools/zoom-blur/animation.webp" width="180"></td>
</tr></table>

## Install

```bash
pip install brushcue
```

## Documentation

The full documentation is available [here](https://www.brushcue.com/docs/py).

## Quickstart

```python
import brushcue

ctx = brushcue.Context()

image = brushcue.Composition.load("photo.png")
grayscale = image.grayscale()

composition = grayscale.execute(ctx)
output_bytes = composition.to_image_bytes(ctx)

with open("output.png", "wb") as f:
    f.write(output_bytes)
```

## Examples

All the [BrushCue tools](https://www.brushcue.com/tools) are available as examples to learn how to use our API. 

- [Adjust Channels](https://www.brushcue.com/docs/py/examples/adjust-channels)
- [Black and White Negative Filter](https://www.brushcue.com/docs/py/examples/black-and-white-negative-filter)
- [Bloom](https://www.brushcue.com/docs/py/examples/bloom)
- [Blue Channel](https://www.brushcue.com/docs/py/examples/blue-channel)
- [Box Blur](https://www.brushcue.com/docs/py/examples/box-blur)
- [Brightness Adjust](https://www.brushcue.com/docs/py/examples/brightness-adjust)
- [Brightness Contrast Adjust](https://www.brushcue.com/docs/py/examples/brightness-contrast-adjust)
- [Camera Moving Distortion](https://www.brushcue.com/docs/py/examples/camera-moving-distortion)
- [Chroma Offset](https://www.brushcue.com/docs/py/examples/chroma-offset)
- [Coachella Aesthetic](https://www.brushcue.com/docs/py/examples/coachella-aesthetic)
- [Color Invert](https://www.brushcue.com/docs/py/examples/color-invert)
- [Color Rectangle](https://www.brushcue.com/docs/py/examples/color-rectangle)
- [Color Reducer](https://www.brushcue.com/docs/py/examples/color-reducer)
- [Color Threshold](https://www.brushcue.com/docs/py/examples/color-threshold)
- [Contrast Adjust](https://www.brushcue.com/docs/py/examples/contrast-adjust)
- [Convert to BT.709](https://www.brushcue.com/docs/py/examples/convert-to-bt-709)
- [Convert to Display P3](https://www.brushcue.com/docs/py/examples/convert-to-display-p3)
- [Convert to sRGB](https://www.brushcue.com/docs/py/examples/convert-to-srgb)
- [CRT Monitor Filter](https://www.brushcue.com/docs/py/examples/crt-monitor-filter)
- [Darken](https://www.brushcue.com/docs/py/examples/darken)
- [Dilate](https://www.brushcue.com/docs/py/examples/dilate)
- [Duotone Effect](https://www.brushcue.com/docs/py/examples/duotone-effect)
- [Erode](https://www.brushcue.com/docs/py/examples/erode)
- [Exposure Adjust](https://www.brushcue.com/docs/py/examples/exposure-adjust)
- [Film Grain](https://www.brushcue.com/docs/py/examples/film-grain)
- [Film Noir](https://www.brushcue.com/docs/py/examples/film-noir)
- [Gaussian Blur](https://www.brushcue.com/docs/py/examples/gaussian-blur)
- [Glitch Filter Animation](https://www.brushcue.com/docs/py/examples/glitch-filter-animation)
- [Grayscale](https://www.brushcue.com/docs/py/examples/grayscale)
- [Green Channel](https://www.brushcue.com/docs/py/examples/green-channel)
- [Halftone](https://www.brushcue.com/docs/py/examples/halftone)
- [High Contrast Grayscale](https://www.brushcue.com/docs/py/examples/high-contrast-grayscale)
- [Horizontal Mirror](https://www.brushcue.com/docs/py/examples/horizontal-mirror)
- [Image to Video](https://www.brushcue.com/docs/py/examples/image-to-video)
- [Kaleidoscope](https://www.brushcue.com/docs/py/examples/kaleidoscope)
- [Kaleidoscope Animation](https://www.brushcue.com/docs/py/examples/kaleidoscope-animation)
- [Kelvin Tuner](https://www.brushcue.com/docs/py/examples/kelvin-tuner)
- [Lighten](https://www.brushcue.com/docs/py/examples/lighten)
- [Lightness Threshold](https://www.brushcue.com/docs/py/examples/lightness-threshold)
- [Linear Transform](https://www.brushcue.com/docs/py/examples/linear-transform)
- [Liquify](https://www.brushcue.com/docs/py/examples/liquify)
- [Median Filter](https://www.brushcue.com/docs/py/examples/median-filter)
- [Negative Filter](https://www.brushcue.com/docs/py/examples/negative-filter)
- [Opacity Scale](https://www.brushcue.com/docs/py/examples/opacity-scale)
- [Pixelate](https://www.brushcue.com/docs/py/examples/pixelate)
- [Pixelate Reveal Animation](https://www.brushcue.com/docs/py/examples/pixelate-reveal-animation)
- [Red Channel](https://www.brushcue.com/docs/py/examples/red-channel)
- [RGB Color Mix Aesthetic](https://www.brushcue.com/docs/py/examples/rgb-color-mix-aesthetic)
- [RGB Color Shift](https://www.brushcue.com/docs/py/examples/rgb-color-shift)
- [Rose Tint](https://www.brushcue.com/docs/py/examples/rose-tint)
- [Rotate 180°](https://www.brushcue.com/docs/py/examples/rotate-180)
- [Rotate 90° Clockwise](https://www.brushcue.com/docs/py/examples/rotate-90-clockwise)
- [Rotate 90° Counterclockwise](https://www.brushcue.com/docs/py/examples/rotate-90-counter-clockwise)
- [Saturation Adjust](https://www.brushcue.com/docs/py/examples/saturation-adjust)
- [Scale by Factor](https://www.brushcue.com/docs/py/examples/scale-by-factor)
- [Sepia](https://www.brushcue.com/docs/py/examples/sepia)
- [Shadow Tint](https://www.brushcue.com/docs/py/examples/shadow-tint)
- [Sharpen](https://www.brushcue.com/docs/py/examples/sharpen)
- [Sobel Edge Detection](https://www.brushcue.com/docs/py/examples/sobel-edge-detection)
- [Solarize](https://www.brushcue.com/docs/py/examples/solarize)
- [Spinning Reveal Animation](https://www.brushcue.com/docs/py/examples/spinning-reveal-animation)
- [Swirl](https://www.brushcue.com/docs/py/examples/swirl)
- [Vertical Mirror](https://www.brushcue.com/docs/py/examples/vertical-mirror)
- [Vibrancy](https://www.brushcue.com/docs/py/examples/vibrancy)
- [Vignette](https://www.brushcue.com/docs/py/examples/vignette)
- [Warmth Adjust](https://www.brushcue.com/docs/py/examples/warmth-adjust)
- [Zoom Blur](https://www.brushcue.com/docs/py/examples/zoom-blur)
