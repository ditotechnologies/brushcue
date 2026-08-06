# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 0f117eba9069efb9105166e63ee2200614f37e34adb4f1db94580e19ba06ba5d
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import float



class Vector3f(_GraphWrapper):
    """A vector with three elements of Float"""

    def execute(self, context):

        return self._inner.execute(context).as_vector3f()


    def add(self, rhs) -> Vector3f:
        """Vector 3 Float Add

        Add two Vector 3s of Floats
    
        Args:
            rhs: Graph of Vector3f
            
    
        Returns:
            Graph: A graph node producing a Vector3f.
        """
        lhs_parsed = input_parsers.parse_graph(self)
        rhs_parsed = input_parsers.parse_graph(rhs)
        result = _internal.vector3f_add_internal(lhs_parsed, rhs_parsed)

        return Vector3f(result)

    @staticmethod
    def from_components(x, y, z) -> Vector3f:
        """Vector 3 Float from Components

        Given an x, y and z creates a vector floats.
    
        Args:
            x: Graph of Float
            y: Graph of Float
            z: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Vector3f.
        """
        x_parsed = input_parsers.parse_float_graph(x)
        y_parsed = input_parsers.parse_float_graph(y)
        z_parsed = input_parsers.parse_float_graph(z)
        result = _internal.vector3f_from_components_internal(x_parsed, y_parsed, z_parsed)

        return Vector3f(result)

    def normalize(self) -> Vector3f:
        """Vector 3 Normalize

        Normalizes a Vector 3 Float. Converting it's length to 1.
    
        Returns:
            Graph: A graph node producing a Vector3f.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector3f_normalize_internal(vector_parsed)

        return Vector3f(result)

    def x(self) -> float.Float:
        """Vector 3D Float X

        Gets the value in the x component for the provided vector
    
        Returns:
            Graph: A graph node producing a Float.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector3f_x_internal(vector_parsed)

        from .float import Float
        return Float(result)

    def y(self) -> float.Float:
        """Vector 3D Y Float

        Gets the value in the y component for the provided vector
    
        Returns:
            Graph: A graph node producing a Float.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector3f_y_internal(vector_parsed)

        from .float import Float
        return Float(result)

    def z(self) -> float.Float:
        """Vector 3D Float Z

        Gets the value in the z component for the provided vector
    
        Returns:
            Graph: A graph node producing a Float.
        """
        vector_parsed = input_parsers.parse_graph(self)
        result = _internal.vector3f_z_internal(vector_parsed)

        from .float import Float
        return Float(result)

