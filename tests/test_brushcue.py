import tempfile
import os
import brushcue


def test_monet_women_with_parasol_grayscale():
    ctx = brushcue.Context()
    image = brushcue.composition_monet_women_with_parasol()
    grayscale = brushcue.composition_grayscale(image)
    result = grayscale.execute(ctx)
    composition = result.as_composition()
    data_bytes = composition.to_image_bytes(ctx)
    assert len(data_bytes) > 0


def test_load_composition_grayscale():
    ctx = brushcue.Context()
    monet = brushcue.composition_monet_women_with_parasol()
    monet_bytes = monet.execute(ctx).as_composition().to_image_bytes(ctx)
    image = brushcue.load_composition(bytes(monet_bytes))
    grayscale = brushcue.composition_grayscale(image)
    result = grayscale.execute(ctx)
    composition = result.as_composition()
    data_bytes = composition.to_image_bytes(ctx)
    assert len(data_bytes) > 0


def test_load_composition_from_file_grayscale():
    ctx = brushcue.Context()
    monet_bytes = brushcue.composition_monet_women_with_parasol().execute(ctx).as_composition().to_image_bytes(ctx)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        f.write(bytes(monet_bytes))
        path = f.name
    try:
        image = brushcue.load_composition(path)
        grayscale = brushcue.composition_grayscale(image)
        result = grayscale.execute(ctx)
        composition = result.as_composition()
        data_bytes = composition.to_image_bytes(ctx)
        assert len(data_bytes) > 0
    finally:
        os.unlink(path)


def test_rgba_color_result_as_tuple():
    ctx = brushcue.Context()
    result = brushcue.r_g_b_a_color_constant(0.1, 0.2, 0.3, 0.4).execute(ctx)
    assert all(
        abs(actual - expected) < 0.000001
        for actual, expected in zip(result.as_rgba_color(), (0.1, 0.2, 0.3, 0.4))
    )
