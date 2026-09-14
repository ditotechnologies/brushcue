# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: 74afce0d9fc0e51f4dc9930292656f26d58e2a05e7f48d773d8f346f8fa96700
# generated from templates/py_type.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from . import _py as _internal, input_parsers
from .object import Object

if TYPE_CHECKING:
    from . import float


class LMSA(Object):
    """An LMS color with an alpha component."""

    def execute(self, context):
        return self._inner.execute(context).as_lmsa_color()

    def alpha(self) -> float.Float:
        """LMS Color Alpha

        Gets the alpha component of an LMS color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        lmsa_parsed = input_parsers.parse_graph(self)
        result = _internal.l_m_s_a_alpha_internal(lmsa_parsed)
        from .float import Float
        return Float(result)

    def l(self) -> float.Float:
        """LMS Color L

        Gets the L component of an LMS color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        lmsa_parsed = input_parsers.parse_graph(self)
        result = _internal.l_m_s_a_l_internal(lmsa_parsed)
        from .float import Float
        return Float(result)

    def m(self) -> float.Float:
        """LMS Color M

        Gets the M component of an LMS color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        lmsa_parsed = input_parsers.parse_graph(self)
        result = _internal.l_m_s_a_m_internal(lmsa_parsed)
        from .float import Float
        return Float(result)

    def s(self) -> float.Float:
        """LMS Color S

        Gets the S component of an LMS color with alpha.

        Returns:
            Graph: A graph node producing a Float.
        """
        lmsa_parsed = input_parsers.parse_graph(self)
        result = _internal.l_m_s_a_s_internal(lmsa_parsed)
        from .float import Float
        return Float(result)
