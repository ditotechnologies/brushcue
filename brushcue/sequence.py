# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: dbd8846e662736d80f80451945a6ee24a0e564e52a773e3089caf9224c81df4c
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import bytes
    from . import composition
    from . import float


class Sequence(Object):
    """A sequence with a bunch of operations to render a movie"""

    def execute(self, context):
        return self._inner.execute(context).as_sequence()

    def adjust_speed(self, factor) -> Sequence:
        """Sequence Adjust Speed

        Adjusts the speed of a sequence by a speed factor.

        Args:
            factor: Graph of Float

        Returns:
            Graph: A graph node producing a Sequence.
        """
        sequence_parsed = input_parsers.parse_graph(self)
        factor_parsed = input_parsers.parse_float_graph(factor)
        result = _internal.sequence_adjust_speed_internal(sequence_parsed, factor_parsed)
        return Sequence(result)

    def composition_at_time(self, time) -> composition.Composition:
        """Sequence Composition at Time

        Extracts an composition from a sequence at a particular time

        Args:
            time: Graph of Float

        Returns:
            Graph: A graph node producing a Composition.
        """
        sequence_parsed = input_parsers.parse_graph(self)
        time_parsed = input_parsers.parse_float_graph(time)
        result = _internal.sequence_composition_at_time_internal(sequence_parsed, time_parsed)
        from .composition import Composition
        return Composition(result)

    def concatenate(self, sequence_2) -> Sequence:
        """Sequence Concatenate

        Given two sequences, combines them into one by playing the first one and then the second one.

        Args:
            sequence_2: Graph of Sequence

        Returns:
            Graph: A graph node producing a Sequence.
        """
        sequence_1_parsed = input_parsers.parse_graph(self)
        sequence_2_parsed = input_parsers.parse_graph(sequence_2)
        result = _internal.sequence_concatenate_internal(sequence_1_parsed, sequence_2_parsed)
        return Sequence(result)

    def duration(self) -> float.Float:
        """Sequence Duration

        Gets the duration from a sequence

        Returns:
            Graph: A graph node producing a Float.
        """
        sequence_parsed = input_parsers.parse_graph(self)
        result = _internal.sequence_duration_internal(sequence_parsed)
        from .float import Float
        return Float(result)

    @staticmethod
    def from_composition_and_duration(composition, duration) -> Sequence:
        """Sequence from Composition and Duration

        Give a Composition and a Duration. Returns a Sequence.

        Args:
            composition: Graph of Composition
            duration: Graph of Float

        Returns:
            Graph: A graph node producing a Sequence.
        """
        composition_parsed = input_parsers.parse_graph(composition)
        duration_parsed = input_parsers.parse_float_graph(duration)
        result = _internal.sequence_from_composition_and_duration_internal(composition_parsed, duration_parsed)
        return Sequence(result)

    @staticmethod
    def from_url(url) -> Sequence:
        """Sequence from URL

        Creates a sequence from URL

        Args:
            url: Graph of String

        Returns:
            Graph: A graph node producing a Sequence.
        """
        url_parsed = input_parsers.parse_string_graph(url)
        result = _internal.sequence_from_u_r_l_internal(url_parsed)
        return Sequence(result)

    @staticmethod
    def graph(duration, fn) -> Sequence:
        """Sequence Graph

        Creates a sequence that runs the graph to get the duration and the frame for each time.

        Args:
            duration: Graph of Float
            fn: The function associated with this node.

        Returns:
            Graph: A graph node producing a Sequence.
        """
        duration_parsed = input_parsers.parse_float_graph(duration)
        if not hasattr(fn, "__brushcue_make_graph__"):
            raise TypeError("fn must be annotated with @brushcue_fn")
        dispatched_graphs = fn.__brushcue_make_graph__([
            _internal.TypeDefinition.from_name("Float")
            ])
        result = _internal.sequence_graph_internal(duration_parsed, *dispatched_graphs
            )

        return Sequence(result)

    def reverse(self) -> Sequence:
        """Sequence Reverse

        Given a sequence. Reverses it.

        Returns:
            Graph: A graph node producing a Sequence.
        """
        sequence_parsed = input_parsers.parse_graph(self)
        result = _internal.sequence_reverse_internal(sequence_parsed)
        return Sequence(result)

    def to_mp4(self, frame_rate) -> bytes.Bytes:
        """Sequence To MP4

        Given a sequence. Converts it to MP4 return a local file to where that MP4 is stored.

        Args:
            frame_rate: Graph of Int

        Returns:
            Graph: A graph node producing a Bytes.
        """
        sequence_parsed = input_parsers.parse_graph(self)
        frame_rate_parsed = input_parsers.parse_int_graph(frame_rate)
        result = _internal.sequence_to_mp4_internal(sequence_parsed, frame_rate_parsed)
        from .bytes import Bytes
        return Bytes(result)

    def trim_back(self, amount) -> Sequence:
        """Sequence Trim Back

        Given a sequence. Trims from the back.

        Args:
            amount: Graph of Float

        Returns:
            Graph: A graph node producing a Sequence.
        """
        sequence_parsed = input_parsers.parse_graph(self)
        amount_parsed = input_parsers.parse_float_graph(amount)
        result = _internal.sequence_trim_back_internal(sequence_parsed, amount_parsed)
        return Sequence(result)

    def trim_front(self, amount) -> Sequence:
        """Sequence Trim Front

        Given a sequence. Trims from the front.

        Args:
            amount: Graph of Float

        Returns:
            Graph: A graph node producing a Sequence.
        """
        sequence_parsed = input_parsers.parse_graph(self)
        amount_parsed = input_parsers.parse_float_graph(amount)
        result = _internal.sequence_trim_front_internal(sequence_parsed, amount_parsed)
        return Sequence(result)
