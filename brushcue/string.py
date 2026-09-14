# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 91ecda873ba3357dab1e9bb91a151f794c5e8b9ca6bc37b554fa85615be488eb
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import void


class String(Object):
    """a string"""

    def execute(self, context):
        return self._inner.execute(context).as_string()

    def upload_file_path(self, url, content_type) -> void.Void:
        """Upload File Path

        Reads a file from a local path on disk and uploads its contents to a URL via PUT request

        Args:
            url: Graph of String
            content_type: Graph of String

        Returns:
            Graph: A graph node producing a Void.
        """
        path_parsed = input_parsers.parse_string_graph(self)
        url_parsed = input_parsers.parse_string_graph(url)
        content_type_parsed = input_parsers.parse_string_graph(content_type)
        result = _internal.upload_file_path_internal(path_parsed, url_parsed, content_type_parsed)
        from .void import Void
        return Void(result)
