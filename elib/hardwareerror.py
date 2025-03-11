"""
Hardware Error
"""

from .absexc import *
from .dunnoerror import WTFError, DunnoError

class HardwareError(AbsurdException):
    """Problem in computer, not chair"""
    pass

class HardwareWarning(AbsurdWarning):
    """Fixable issue in computer, not chair"""
    pass

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

class WhyIsTheModemOnFireError(WiFiError, WTFError, HardwareError):
    """What the Fuck why is it on FIRE"""
    pass

class NoKeyboardError(HardwareWarning):
    """Keyboard not found. Press any key to continue..."""
    pass

class iGPUExistsError(HardwareError):
    """the iGPU exists and is being used."""
    pass