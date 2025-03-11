"""
Logic Error
"""

from .absexc import *
from .dunnoerror import *

class LogicError(AbsurdException):
    """Logic fucking died"""
    pass

class LogicWarning(AbsurdWarning):
    """Logic injured itself"""
    pass

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