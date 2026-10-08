# (c) Dito Technologies LLC. Auto-generated. Do not modify directly.
# hash: e1ca8b5a033204557277abf620db9c63abf15dbb11110180bbf119c987b5057a
# generated from templates/py_type.jinja

from __future__ import annotations

from .object import Object


class Character(Object):
    """a single user-perceived character"""

    def execute(self, context):
        return self._inner.execute(context)
