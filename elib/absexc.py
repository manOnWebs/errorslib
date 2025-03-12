"""Base classes"""

# ==============================
# Base Exception Classes
# ==============================

class AbsurdClass:
    """errorslib base class!"""
    pass

class AbsurdException(Exception, AbsurdClass):
    """errorslib base error class!"""
    pass

class AbsurdWarning(Warning, AbsurdClass):
    """errorslib base warning class!"""
    pass

class UserError(AbsurdException):
    """User needs to RTFM."""
    pass

class DevError(AbsurdException):
    """Developer needs to RTFM."""
    pass

class ManagerError(AbsurdException):
    """The manager needs to know that they can't just FUCKING ask for “one more feature” at the last minute"""
    pass

class CodeError(AbsurdException):
    """ code needs to RTFM."""
    pass

class HardwareError(AbsurdException):
    """Problem in computer, not chair"""
    pass

class LogicError(AbsurdException):
    """Logic fucking died"""
    pass

class DunnoError(AbsurdException):
    """You have to ask 'wtf?' sometimes."""
    pass

class UserWarning(AbsurdWarning):
    """User may need to RTFM."""
    pass

class DevWarning(AbsurdWarning):
    """Developer may need to RTFM."""
    pass

class CodeWarning(AbsurdWarning):
    """ code may need to RTFM"""
    pass

class HardwareWarning(AbsurdWarning):
    """Fixable issue in computer, not chair"""
    pass

class LogicWarning(AbsurdWarning):
    """Logic injured itself"""
    pass

class DunnoWarning(AbsurdWarning):
    """You have to ask 'why?' sometimes."""
    pass

class Cat(AbsurdClass):
    """Felis catus"""
    pass

class Cats(Cat):
    """Multiple Felis catus'"""
    pass

class Dog(AbsurdClass):
    """Canis familiaris"""
    pass

class Dogs(Dog):
    """Mutlipe Canis familiaris'"""
    pass

class CatWarning(AbsurdWarning, Cat):
    """Cat did something"""
    pass

class CatError(AbsurdException, Cat):
    """Cat did something MAJOR"""
    pass

class CatAstrophicError(AbsurdClass, CatError, SystemExit, SystemError, Cat):
    """Cat did something Cat-astrophic! Get it?... okay, I'm not funny."""
    pass

class DogWarning(AbsurdWarning, Dog):
    """Dog did something"""
    pass

class DogError(AbsurdException, Dog):
    """Dog did something MAJOR"""
    pass

class CatastrophicDogError(AbsurdClass, DogError, SystemExit, SystemError, Dog):
    """Dog did something CATASTROPHIC"""
    pass

class AIError(AbsurdException):
    """Base class for all AI errors"""
    pass

class KeyboardError(AbsurdException):
    """Base class for all keyboard errors"""
    pass

class TimeError(AbsurdException):
    """Base class for all time errors"""
    pass

class InternError(AbsurdException):
    """Intern has done something questionable."""
    pass

class SalesError(AbsurdException):
    """Sales team has promised something that doesn’t exist."""
    pass

class HRError(ManagerError):
    """HR has done something more questionable."""
    pass