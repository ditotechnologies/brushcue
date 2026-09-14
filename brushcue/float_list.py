# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 25981bf9a76a659411b462ab35f2c7c1dbeaf56899fcbd8d51870763a575ad08
# generated from templates/py_type.jinja

from __future__ import annotations

from .list import List


class FloatList(List):
    """List of Floats"""

    def __init__(self, inner, resolved_type=None):
        from .float import Float
        super().__init__(inner, Float if resolved_type is None else resolved_type)

    def execute(self, context):
        return self._inner.execute(context).as_float_list()
