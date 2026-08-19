import os
import tempfile

import brushcue


def test_monet_women_with_parasol_grayscale():
    ctx = brushcue.Context()
    image = brushcue.Composition.monet_women_with_parasol()
    grayscale = image.grayscale()
    composition = grayscale.execute(ctx)
    data_bytes = composition.to_image_bytes(ctx)
    assert len(data_bytes) > 0


def test_load_composition_grayscale():
    ctx = brushcue.Context()
    monet = brushcue.Composition.monet_women_with_parasol()
    monet_bytes = monet.execute(ctx).to_image_bytes(ctx)
    image = brushcue.Composition.load(monet_bytes)
    grayscale = image.grayscale()
    composition = grayscale.execute(ctx)
    data_bytes = composition.to_image_bytes(ctx)
    assert len(data_bytes) > 0


def test_load_composition_from_file_grayscale():
    ctx = brushcue.Context()
    monet_bytes = (
        brushcue.Composition.monet_women_with_parasol()
        .execute(ctx)
        .to_image_bytes(ctx)
    )
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        f.write(monet_bytes)
        path = f.name
    try:
        image = brushcue.Composition.load(path)
        grayscale = image.grayscale()
        composition = grayscale.execute(ctx)
        data_bytes = composition.to_image_bytes(ctx)
        assert len(data_bytes) > 0
    finally:
        os.unlink(path)


def test_rgba_color_result_as_tuple():
    ctx = brushcue.Context()
    result = brushcue.RGBAColor.from_components(0.1, 0.2, 0.3, 0.4).execute(ctx)
    assert all(
        abs(actual - expected) < 0.000001
        for actual, expected in zip(result, (0.1, 0.2, 0.3, 0.4))
    )


def test_profiled_color_to_ok_lab_a_result_as_tuple():
    ctx = brushcue.Context()
    profiled_color = brushcue.ProfiledColor.from_rgba_srgb(
        brushcue.RGBAColor.from_components(1.0, 0.0, 0.0, 0.4)
    )

    result = profiled_color.to_ok_lab_a().execute(ctx)

    assert len(result) == 4
    assert all(isinstance(component, float) for component in result)
    assert abs(result[3] - 0.4) < 0.000001


def test_profiled_color_to_rgb_linear_with_color_profile():
    ctx = brushcue.Context()
    profiled_color = brushcue.ProfiledColor.from_rgba_srgb(
        brushcue.RGBAColor.from_components(0.5, 0.0, 1.0, 0.4)
    )

    result = profiled_color.to_rgb_linear_with_color_profile(
        brushcue.ColorProfile.srgb()
    ).execute(ctx)

    assert abs(result[0] - 0.21404114) < 0.00001
    assert abs(result[1]) < 0.000001
    assert abs(result[2] - 1.0) < 0.000001
    assert abs(result[3] - 0.4) < 0.000001
