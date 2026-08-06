# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: d9e6f5bf2acdd98499d0e76020430b33bef531397f996940ca8e8cf45fed3894
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class Dictionary(_GraphWrapper):
    """A key value lookup between a name and a type in the graph"""

    def execute(self, context):

        return self._inner.execute(context)


    def add_bool_to_dictionary(self, key, value) -> Dictionary:
        """Bool Add To Dictionary

        Adds a Bool to a Dictionary
    
        Args:
            key: Graph of String
            value: Graph of Bool
            
    
        Returns:
            Graph: A graph node producing a Dictionary.
        """
        dictionary_parsed = input_parsers.parse_graph(self)
        key_parsed = input_parsers.parse_string_graph(key)
        value_parsed = input_parsers.parse_bool_graph(value)
        result = _internal.bool_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

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

    def add_float_to_dictionary(self, key, value) -> Dictionary:
        """Float Add To Dictionary

        Adds a Float to a Dictionary
    
        Args:
            key: Graph of String
            value: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Dictionary.
        """
        dictionary_parsed = input_parsers.parse_graph(self)
        key_parsed = input_parsers.parse_string_graph(key)
        value_parsed = input_parsers.parse_float_graph(value)
        result = _internal.float_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

        return Dictionary(result)

    def add_int_to_dictionary(self, key, value) -> Dictionary:
        """Int Add To Dictionary

        Adds a Int to a Dictionary
    
        Args:
            key: Graph of String
            value: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Dictionary.
        """
        dictionary_parsed = input_parsers.parse_graph(self)
        key_parsed = input_parsers.parse_string_graph(key)
        value_parsed = input_parsers.parse_int_graph(value)
        result = _internal.int_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

        return Dictionary(result)

    def add_profiled_color_to_dictionary(self, key, value) -> Dictionary:
        """Profiled Color Add To Dictionary

        Adds a Profiled Color to a Dictionary
    
        Args:
            key: Graph of String
            value: Graph of ProfiledColor
            
    
        Returns:
            Graph: A graph node producing a Dictionary.
        """
        dictionary_parsed = input_parsers.parse_graph(self)
        key_parsed = input_parsers.parse_string_graph(key)
        value_parsed = input_parsers.parse_graph(value)
        result = _internal.profiled_color_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

        return Dictionary(result)

    def add_r_g_b_color_to_dictionary(self, key, value) -> Dictionary:
        """RGB Color Add To Dictionary

        Adds a RGB Color to a Dictionary
    
        Args:
            key: Graph of String
            value: Graph of RGBColor
            
    
        Returns:
            Graph: A graph node producing a Dictionary.
        """
        dictionary_parsed = input_parsers.parse_graph(self)
        key_parsed = input_parsers.parse_string_graph(key)
        value_parsed = input_parsers.parse_graph(value)
        result = _internal.r_g_b_color_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

        return Dictionary(result)

    def add_vector2f_to_dictionary(self, key, value) -> Dictionary:
        """Vector 2 Float Add To Dictionary

        Adds a Vector 2 Float to a Dictionary
    
        Args:
            key: Graph of String
            value: Graph of Vector2f
            
    
        Returns:
            Graph: A graph node producing a Dictionary.
        """
        dictionary_parsed = input_parsers.parse_graph(self)
        key_parsed = input_parsers.parse_string_graph(key)
        value_parsed = input_parsers.parse_graph(value)
        result = _internal.vector2f_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

        return Dictionary(result)

    def add_vector2i_to_dictionary(self, key, value) -> Dictionary:
        """Vector 2 Int Add To Dictionary

        Adds a Vector 2 Int to a Dictionary
    
        Args:
            key: Graph of String
            value: Graph of Vector2i
            
    
        Returns:
            Graph: A graph node producing a Dictionary.
        """
        dictionary_parsed = input_parsers.parse_graph(self)
        key_parsed = input_parsers.parse_string_graph(key)
        value_parsed = input_parsers.parse_graph(value)
        result = _internal.vector2i_add_to_dictionary_internal(dictionary_parsed, key_parsed, value_parsed)

        return Dictionary(result)

