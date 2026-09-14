# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 3692c38c3a60d92aaae826f59898a1a45f6d4e5ae67eac51a2a26656fc8221f6
# generated from templates/py_type.jinja

from __future__ import annotations

from . import _py as _internal, input_parsers
from .object import Object


class Dictionary(Object):
    """A key value lookup between a name and a type in the graph"""

    def execute(self, context):
        return self._inner.execute(context)

    def add(self, key, value) -> Dictionary:
        """Dictionary Add

        Adds a key-value pair to a dictionary

        Args:
            key: Graph of String
            value: Graph of Any

        Returns:
            Graph: A graph node producing a Dictionary.
        """
        dictionary_parsed = input_parsers.parse_graph(self)
        key_parsed = input_parsers.parse_string_graph(key)
        value_parsed = input_parsers.parse_graph(value)
        result = _internal.dictionary_add_internal(dictionary_parsed, key_parsed, value_parsed)
        return Dictionary(result)

    @staticmethod
    def create() -> Dictionary:
        """Dictionary Create

        Creates a new dictionary

        Returns:
            Graph: A graph node producing a Dictionary.
        """
        result = _internal.dictionary_create_internal()
        return Dictionary(result)
