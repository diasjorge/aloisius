# Copyright 2017 The contributors. All rights reserved.
#
# See LICENSE file for full license.

__all__ = []


def export(defn):
    globals()[defn.__name__] = defn
    __all__.append(defn.__name__)
    return defn


from .stack_collection import StackCollection  # noqa: E402
from .stack import Stack  # noqa: E402,F401

stacks = StackCollection()
