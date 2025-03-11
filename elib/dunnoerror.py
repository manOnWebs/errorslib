"""
WTF?
"""

from .absexc import *

class DunnoError(AbsurdException):
    """You have to ask 'wtf?' sometimes."""
    pass

class DunnoWarning(AbsurdWarning):
    """You have to ask 'why?' sometimes."""
    pass


class WTFError(DunnoError):
    """there's no other error that can describe what's going on."""
    pass

class IdiotError(DunnoError):
    """your problem exists between your window and the nearest exit."""
    pass
