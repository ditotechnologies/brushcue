# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 6ebf1cd97b171c9918b87be6ced0e11f1fceda2476ea00daf18675d2426528e0
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from ._graph import _GraphWrapper


if TYPE_CHECKING:

    from . import float



class Curve(_GraphWrapper):
    """A curve that represents a mathematical function in 2D that takes and input and maps to an output."""

    def execute(self, context):

        return self._inner.execute(context)


    def evaluate(self, input) -> float.Float:
        """Curve Evaluate

        Evaluates a curve at a given input value.
    
        Args:
            input: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Float.
        """
        curve_parsed = input_parsers.parse_graph(self)
        input_parsed = input_parsers.parse_float_graph(input)
        result = _internal.curve_evaluate_internal(curve_parsed, input_parsed)

        from .float import Float
        return Float(result)

    @staticmethod
    def gamma(gamma) -> Curve:
        """Curve Gamma

        A gamma curve. The gamma parameter corresponding to y=x^gamma.
    
        Args:
            gamma: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Curve.
        """
        gamma_parsed = input_parsers.parse_float_graph(gamma)
        result = _internal.curve_gamma_internal(gamma_parsed)

        return Curve(result)

    @staticmethod
    def identity() -> Curve:
        """Curve Identity

        An identity curve, y=x
    
        Returns:
            Graph: A graph node producing a Curve.
        """
        result = _internal.curve_identity_internal()

        return Curve(result)

    @staticmethod
    def pivoted_sigmoid(pivot, slope) -> Curve:
        """Curve Pivoted Sigmoid

        A pivoted sigmoid contrast curve that anchors at the pivot and smoothly compresses shadows and highlights, with a slope parameter controlling midtone contrast.
    
        Args:
            pivot: Graph of Float
            slope: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Curve.
        """
        pivot_parsed = input_parsers.parse_float_graph(pivot)
        slope_parsed = input_parsers.parse_float_graph(slope)
        result = _internal.curve_pivoted_sigmoid_internal(pivot_parsed, slope_parsed)

        return Curve(result)

    @staticmethod
    def s_curve(pivot, slope, toe, shoulder) -> Curve:
        """Curve S

        An S-curve remaps values by anchoring contrast at a chosen pivot, increasing or decreasing midtone separation via slope, gently flattening the curve near black with toe to compress or lift shadows, and softly flattening near white with shoulder to roll off highlights, while keeping black and white fixed.
    
        Args:
            pivot: Graph of Float
            slope: Graph of Float
            toe: Graph of Float
            shoulder: Graph of Float
            
    
        Returns:
            Graph: A graph node producing a Curve.
        """
        pivot_parsed = input_parsers.parse_float_graph(pivot)
        slope_parsed = input_parsers.parse_float_graph(slope)
        toe_parsed = input_parsers.parse_float_graph(toe)
        shoulder_parsed = input_parsers.parse_float_graph(shoulder)
        result = _internal.curve_s_curve_internal(pivot_parsed, slope_parsed, toe_parsed, shoulder_parsed)

        return Curve(result)

