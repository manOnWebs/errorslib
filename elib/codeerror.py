"""
Code Error
"""

from .absexc import *

# ==============================
# Code-Related Errors
# ==============================

class CodeIsFuckedUpError(CodeError):
    """the code broke."""
    pass

class OvercomplicatedSolutionError(CodeError):
    """the solution is way more complicated than it needs to be."""
    pass

class UndercomplicatedSolutionError(CodeError):
    """the solution is too simple to be correct."""
    pass

class OopsIDidItAgainError(CodeError):
    """this error is a repeat of a previous error."""
    pass

class NotAGoodError(CodeError):
    """this error is a terrible error."""
    pass