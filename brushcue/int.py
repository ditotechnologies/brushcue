# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: bd72d99ef24ec69ab2f77ee23ee9a905cd9b49a2fe451d19ab36198eb76a58ab
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import bool

    from . import float

    from . import string



class Int(_GraphWrapper):
    """An integer"""

    def execute(self, context):

        return self._inner.execute(context).as_int()


    def abs(self) -> Int:
        """Int Absolute Value

        Returns the absolute value of an int
    
        Returns:
            Graph: A graph node producing a Int.
        """
        number_parsed = input_parsers.parse_int_graph(self)
        result = _internal.int_abs_internal(number_parsed)

        return Int(result)

    def add(self, int_2) -> Int:
        """Int Add

        Adds to ints together
    
        Args:
            int_2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Int.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_add_internal(int_1_parsed, int_2_parsed)

        return Int(result)

    def equals(self, int_2) -> bool.Bool:
        """Int Equals

        Checks if two ints are equal
    
        Args:
            int_2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_equals_internal(int_1_parsed, int_2_parsed)

        from .bool import Bool
        return Bool(result)

    def greater_than(self, int_2) -> bool.Bool:
        """Int Greater Than

        Checks if the first int is greater than the second int
    
        Args:
            int_2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_greater_than_internal(int_1_parsed, int_2_parsed)

        from .bool import Bool
        return Bool(result)

    def greater_than_or_equal(self, int_2) -> bool.Bool:
        """Int Greater Than Or Equal

        Checks if the first int is greater than or equal to the second int
    
        Args:
            int_2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_greater_than_or_equal_internal(int_1_parsed, int_2_parsed)

        from .bool import Bool
        return Bool(result)

    @staticmethod
    def if_(bool, input_1, input_2) -> Int:
        """Int If

        If the boolean is true returns input 1, otherwise input 2. Type: Int
    
        Args:
            bool: Graph of Bool
            input_1: Graph of Int
            input_2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Int.
        """
        bool_parsed = input_parsers.parse_bool_graph(bool)
        input_1_parsed = input_parsers.parse_int_graph(input_1)
        input_2_parsed = input_parsers.parse_int_graph(input_2)
        result = _internal.int_if_internal(bool_parsed, input_1_parsed, input_2_parsed)

        return Int(result)

    def less_than(self, int_2) -> bool.Bool:
        """Int Less Than

        Checks if the first int is less than the second int
    
        Args:
            int_2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_less_than_internal(int_1_parsed, int_2_parsed)

        from .bool import Bool
        return Bool(result)

    def less_than_or_equal(self, int_2) -> bool.Bool:
        """Int Less Than Or Equal

        Checks if the first int is less than or equal to the second int
    
        Args:
            int_2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Bool.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_less_than_or_equal_internal(int_1_parsed, int_2_parsed)

        from .bool import Bool
        return Bool(result)

    def max(self, int2) -> Int:
        """Int Max

        Returns the maximum int.
    
        Args:
            int2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Int.
        """
        int1_parsed = input_parsers.parse_int_graph(self)
        int2_parsed = input_parsers.parse_int_graph(int2)
        result = _internal.int_max_internal(int1_parsed, int2_parsed)

        return Int(result)

    def min(self, int2) -> Int:
        """Int Min

        Returns the minimum int.
    
        Args:
            int2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Int.
        """
        int1_parsed = input_parsers.parse_int_graph(self)
        int2_parsed = input_parsers.parse_int_graph(int2)
        result = _internal.int_min_internal(int1_parsed, int2_parsed)

        return Int(result)

    def multiply(self, int_2) -> Int:
        """Int Multiply

        Multiplies two integers together
    
        Args:
            int_2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Int.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_multiply_internal(int_1_parsed, int_2_parsed)

        return Int(result)

    def passthrough(self) -> Int:
        """Int Passthrough

        Responds with the value provided. Doing nothing to it.
    
        Returns:
            Graph: A graph node producing a Int.
        """
        value_parsed = input_parsers.parse_int_graph(self)
        result = _internal.int_passthrough_internal(value_parsed)

        return Int(result)

    def subtract(self, int_2) -> Int:
        """Int Subtract

        Subtracts one int from another
    
        Args:
            int_2: Graph of Int
            
    
        Returns:
            Graph: A graph node producing a Int.
        """
        int_1_parsed = input_parsers.parse_int_graph(self)
        int_2_parsed = input_parsers.parse_int_graph(int_2)
        result = _internal.int_subtract_internal(int_1_parsed, int_2_parsed)

        return Int(result)

    def to_float(self) -> float.Float:
        """Int To Float

        Converts an Int to a Float
    
        Returns:
            Graph: A graph node producing a Float.
        """
        int_parsed = input_parsers.parse_int_graph(self)
        result = _internal.int_to_float_internal(int_parsed)

        from .float import Float
        return Float(result)

    def monet_network_download_url_from_asset_id(self) -> string.String:
        """Monet Network Download URL from Asset ID

        Creates a Download URL from asset ID in the Monet Network
    
        Returns:
            Graph: A graph node producing a String.
        """
        asset_id_parsed = input_parsers.parse_int_graph(self)
        result = _internal.monet_network_download_u_r_l_from_asset_i_d_internal(asset_id_parsed)

        from .string import String
        return String(result)

