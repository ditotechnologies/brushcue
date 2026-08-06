# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: ebe160abbbd8766ffa304e93b0b9ae3fb955e1cb73fda153da9a9b715eb25e05
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper



class Bool(_GraphWrapper):
    """A bool"""

    def execute(self, context):

        return self._inner.execute(context).as_bool()


    def and_(self, bool2) -> Bool:
        """And

        Returns true if both inputs are true.
    
        Args:
            bool2: Graph of Bool
            
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        bool1_parsed = input_parsers.parse_bool_graph(self)
        bool2_parsed = input_parsers.parse_bool_graph(bool2)
        result = _internal.and_internal(bool1_parsed, bool2_parsed)

        return Bool(result)

    def if_(self, input_1, input_2) -> Bool:
        """Bool If

        If the boolean is true returns input 1, otherwise input 2. Type: Bool
    
        Args:
            input_1: Graph of Bool
            input_2: Graph of Bool
            
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        bool_parsed = input_parsers.parse_bool_graph(self)
        input_1_parsed = input_parsers.parse_bool_graph(input_1)
        input_2_parsed = input_parsers.parse_bool_graph(input_2)
        result = _internal.bool_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

        return Bool(result)

    def not_(self) -> Bool:
        """Not

        Returns the opposite of a boolean
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        bool_parsed = input_parsers.parse_bool_graph(self)
        result = _internal.not_internal(bool_parsed)

        return Bool(result)

    def or_(self, bool2) -> Bool:
        """Or

        Returns true if either inputs are true.
    
        Args:
            bool2: Graph of Bool
            
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        bool1_parsed = input_parsers.parse_bool_graph(self)
        bool2_parsed = input_parsers.parse_bool_graph(bool2)
        result = _internal.or_internal(bool1_parsed, bool2_parsed)

        return Bool(result)

    def xor(self, bool2) -> Bool:
        """Exclusive Or

        Returns true if either the inputs are true. But false if both are true.
    
        Args:
            bool2: Graph of Bool
            
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        bool1_parsed = input_parsers.parse_bool_graph(self)
        bool2_parsed = input_parsers.parse_bool_graph(bool2)
        result = _internal.xor_internal(bool1_parsed, bool2_parsed)

        return Bool(result)

