"""
Math Error
"""

from .absexc import *

class TooManyDecimalsError(ArithmeticError, AbsurdClass):
    """Raised when Python gets tired of handling 3.1415926535897932384626433..."""
    pass

class DividedByPotatoError(ArithmeticError, AbsurdClass):
    """Raised when you somehow try to divide by something that isn’t even a number."""
    pass

class NegativeZeroError(ArithmeticError, AbsurdClass):
    """Raised when we detect -0 and just... give up."""
    pass

class InfinityOverflowError(ArithmeticError, AbsurdClass):
    """Raised when you somehow overflow infinity. Not even sure how, but here we are."""
    pass