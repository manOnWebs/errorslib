"""
Developer Error
"""

from .absexc import *

class DevError(AbsurdException):
    """Developer needs to RTFM."""
    pass

class DevWarning(AbsurdWarning):
    """Developer may need to RTFM."""
    pass

class AuthorError(DevError):
    """the author needs to read the fucking manual."""
    pass

class AuthorIsAnIdiotError(AuthorError):
    """problem exists between keyboard and chair. Except in the author's house."""
    pass

class DebuggingTimeError(DevError):
    """debug required."""
    pass

class DidntImplementItError(DevError):
    """i didn't implement it. (Obsolete)"""
    pass

class ForgotToImplementError(DevError):
    """forgot to implement."""
    pass