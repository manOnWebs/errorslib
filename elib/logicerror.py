"""
Logic Error
"""

from .absexc import *
from .dunnoerror import *

# ==============================
# Logic Errors
# ==============================

class ParadoxError(LogicError, WTFError):
    """Oh no! paradox."""
    pass

class NotAnError(LogicError, ParadoxError):
    """There is no error."""  # Wait, this is technically a paradox.
    pass

class ThisErrorShouldNeverHappenError(LogicError, DunnoError):
    """this error should never happen."""
    pass

class ThisErrorIsInevitableError(LogicError):
    """this error is inevitable."""
    pass

class Y2k38Error(TimeError, LogicError):
    """Raised when it's Y2k38. Oops"""
    pass