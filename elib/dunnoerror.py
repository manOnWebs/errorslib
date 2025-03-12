"""
WTF?
"""

from .absexc import *

# ==============================
# Miscellaneous WTF Errors
# ==============================

class WTFError(DunnoError):
    """there's no other error that can describe what's going on."""
    pass

class IdiotError(DunnoError):
    """your problem exists between your window and the nearest exit."""
    pass

class LeapYearConfusionError(TimeError, DunnoError):
    """Raised when February 29th appears out of nowhere and we panic."""
    pass