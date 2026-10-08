# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: a89cebe4d28c9b9f585539f144eb4c9823fed54f1058a06e31c5bec9991fef50
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class Font(Object):
    """a font"""

    def execute(self, context):
        return self._inner.execute(context)

    @staticmethod
    def from_path(path) -> Font:
        """Font from Path

        Loads a font file from a file path or URL, and parses it into a Font.

        Args:
            path: Graph of String

        Returns:
            Graph: A graph node producing a Font.
        """
        path_parsed = input_parsers.parse_string_graph(path)
        result = _internal.font_from_path_internal(path_parsed)
        return Font(result)
