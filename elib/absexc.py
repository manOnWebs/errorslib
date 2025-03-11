"""Absurd Exceptions!"""

class AbsurdClass:
    """errorslib base class!"""
    pass

class AbsurdException(Exception, AbsurdClass):
    """errorslib base error class!"""
    pass

class AbsurdWarning(Warning, AbsurdClass):
    """errorslib base warning class!"""
    pass