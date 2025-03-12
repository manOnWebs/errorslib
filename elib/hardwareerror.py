"""
Hardware Error
"""

from .absexc import *
from .dunnoerror import WTFError, DunnoError

# ==============================
# Hardware/System Errors
# ==============================

class ComputerError(AbsurdException):
    """Problem in computer, not chair"""
    pass

class WTFNoBiosError(HardwareError):
    """how!?"""
    pass

class WTFNoOS(HardwareError):
    """how!?"""
    pass

class WiFiError(HardwareError):
    """WiFi done died again"""
    pass

class WifiWarning(HardwareWarning):
    """Ooopsies"""
    pass

class NoInternetError(WiFiError):
    """there is no internet."""
    pass

class ISPError(WiFiError):
    """those mfs"""
    pass

class WiFiError(HardwareError):
    """WiFi done died again"""
    pass

class WifiWarning(HardwareWarning):
    """Ooopsies"""
    pass

class ISPThrottlingAgainError(ISPError):
    """Damn it, AT&T"""
    pass

class NeighborStoleWiFiError(WiFiError):
    """Fucking John"""
    pass

class WhyIsModemOnFireError(WiFiError, WTFError, HardwareError):
    """What the Fuck why is it on FIRE"""
    pass

class NoKeyboardError(HardwareWarning):
    """Keyboard not found. Press any key to continue..."""
    pass

class iGPUExistsError(HardwareError):
    """the iGPU exists and is being used."""
    pass

class KeyboardIsJudgingYouError(KeyboardError, UserError):
    """Raised when you smash random keys and expect Pylance to understand."""

class CapsLockOnTooLongError(KeyboardError, UserError):
    """Raised when Python detects you coding like a screaming lunatic."""
    pass

class InfiniteUndoRegretError(UserError):
    """Raised when you keep pressing Ctrl+Z and end up deleting everything you ever loved."""
    pass

class WiFiSucksError(WiFiError):
    """Raised when your connection is so bad Python won't even try."""
    pass