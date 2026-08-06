# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: ec1f44a1567630bac3e61ca8c88eed2617566065da7678f943988ea0b0a0d685
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import profiled_color



class ProfiledColorList(_GraphWrapper):
    """List of Profiled Colors"""

    def execute(self, context):

        return self._inner.execute(context)


    def first(self) -> profiled_color.ProfiledColor:
        """Profiled Color List First

        First Item of Profiled Color List
    
        Returns:
            Graph: A graph node producing a ProfiledColor.
        """
        list_parsed = input_parsers.parse_graph(self)
        result = _internal.profiled_color_list_first_internal(list_parsed)

        from .profiled_color import ProfiledColor
        return ProfiledColor(result)

