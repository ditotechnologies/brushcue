# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 80b51a8ea582e88d6bc9d9d689385f52ef7a84348b647eb7202ec2930e0159c7
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import void



class String(_GraphWrapper):
    """a string"""

    def execute(self, context):

        return self._inner.execute(context).as_string()


    @staticmethod
    def if_(bool, input_1, input_2) -> String:
        """String If

        If the boolean is true returns input 1, otherwise input 2. Type: String
    
        Args:
            bool: Graph of Bool
            input_1: Graph of String
            input_2: Graph of String
            
    
        Returns:
            Graph: A graph node producing a String.
        """
        bool_parsed = input_parsers.parse_bool_graph(bool)
        input_1_parsed = input_parsers.parse_string_graph(input_1)
        input_2_parsed = input_parsers.parse_string_graph(input_2)
        result = _internal.string_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

        return String(result)

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

