"""
More useless errors
"""

from .absexc import *

class ExistentialCrisisError(AbsurdException):
    """Your code is making you question your career choices."""
    pass

class SyntaxPoliceError(AbsurdException):
    """Code looks illegal, but actually works. Somehow."""
    pass

class TooManyPrintStatementsError(AbsurdException):
    """You tried to debug using 500 `print()` statements and now you can’t find anything."""
    pass

class RubberDuckOverflowError(AbsurdException):
    """Raised when you have too many rubber ducks for debugging and still don’t understand the problem."""
    pass

class CodeSoBadItWorksError(AbsurdException):
    """Your code **shouldn't** work, but it does. And that scares you."""
    pass

class SpaghettiCodeDetectedError(AbsurdException):
    """Raised when the codebase is so messy, it’s legally classified as pasta."""
    pass