# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import

from .constructors import empty, zeros, ones, handle
from . conn import connect
from . import scidb_interp

# --- Initialize ---
from . import ufuncs

# Register scidb AIR interpreter
from blaze.air import interps
interps.register_interp('scidb', scidb_interp)