"""
User Error
"""

from .absexc import *

class UserError(AbsurdException):
    """User needs to RTFM."""
    pass

class UserWarning(AbsurdWarning):
    """User may need to RTFM."""
    pass

class RTFMError(UserError):
    """read the fucking manual"""
    pass

class UserIsAnIdiotError(UserError, RTFMError):
    """problem exists between keyboard and chair."""
    pass

class UserIsNotAnIdiotError(UserError):
    """problem does not exist between keyboard and chair."""
    pass

class PICNICError(UserError):
    """Problem In Chair, Not In Computer."""
    pass

class FeatureNotABugError(UserError):
    """it's a feature. Not a bug."""
    pass

class UserIsUsingOSError(UserError):
    """the user is using an operating system."""
    pass

class UserIsUsingOSWarning(AbsurdWarning):
    """the user is using an operating system."""
    pass

class UserIsUsingWindowsError(UserIsUsingOSError):
    """the user is using an inferior operating system."""
    pass

class AppleError(Exception):
    """You use Apple..."""
    pass

class UserIsAppleSheepError(UserError, AppleError):
    """the user is an Apple sheep."""
    pass

class UserIsUsingMacOSError(UserIsUsingOSError, UserIsAppleSheepError, AppleError):
    """the user is using an even more inferior operating system."""
    pass

class UserIsUsingLinuxError(UserIsUsingOSWarning):
    """the user is using a superior operating system."""
    pass