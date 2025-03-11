# elib/__init__.py

# Import base errors
from .codeerror import CodeError
from .deverror import DevError
from .dunnoerror import DunnoError
from .hardwareerror import HardwareError
from .logicerror import LogicError
from .usererror import UserError

# Import all subclasses from their respective modules
from .absexc import (AbsurdException)

from .usererror import *

from .deverror import *

from .codeerror import *

from .hardwareerror import *

from .logicerror import *

from .dunnoerror import *

# Define what gets imported when doing "from elib import *"
__all__ = [
    # Base Exception Classes
    "UserError",
    "DevError",
    "CodeError",
    "HardwareError",
    "LogicError",
    "DunnoError",
    "AbsurdException",
    "AbsurdWarning",
    "AbsurdClass",
    "Cat",
    "Cats",
    "Dog",
    "AppleError",
    "CatError",
    "CatWarning",
    "DogError",
    "DogWarning",
    "CatAstrophicError",
    "CatastrophicDogError",

    # User Errors
    "UserIsAnIdiotError",
    "UserIsNotAnIdiotError",
    "PICNICError",
    "FeatureNotABugError",
    "UserIsUsingWindowsError",
    "UserIsUsingMacOSError",
    "UserIsAppleSheepError",
    "UserIsUsingLinuxError",
    "UserIsUsingOSError",
    "UserIsUsingOSWarning",
    "RTFMError",

    # Developer Errors
    "AuthorError",
    "AuthorIsAnIdiotError",
    "DebuggingTimeError",
    "DidntImplementError",
    "ForgotToImplementError",

    # Code Errors
    "CodeIsFuckedUpError",
    "OvercomplicatedSolutionError",
    "UndercomplicatedSolutionError",
    "OopsIDidItAgainError",
    "NotAGoodError",

    # Hardware Errors
    "WTFNoBiosError",
    "WTFNoOS",
    "NoInternetError",
    "NoKeyboardError",
    "iGPUExistsError",
    "WiFiError",
    "WifiWarning",
    "ISPThrottlingAgainError",
    "NeighborStoleWiFiError",
    "WhyIsTheModemOnFireError",

    # Pet Errors
    "CatBecameRouterError",
    "CatBecameModemError",
    "CatBecameISPError",
    "CatBecameFirewallError",
    "DogBecameRouterError",
    "DogBecameModemError",
    "DogBecameISPError",
    "DogBecameFirewallError",
    "DogAteTheEthernetCableError",
    "DogAndCatAteTheEthernetCableErrorAgain",
    "DogAndCatAteTheRouterError",
    "DogAndCatAteTheISPError",
    "CatAteTheISPError",
    "CatsAteTheISPError",
    "CatsAreTheISPError",
    "DogAndCatAreTheISPError",
    "CatAteTheEthernetCableError",
    "CatsAteTheEthernetCableError",
    "CatsAteThePCAgainError",
    "CatsAteTheWorldAgainError",
    "CatsBecameThePythonInterpreterAgain",

    # Logic Errors
    "NotAnError",
    "ParadoxError",
    "ThisErrorShouldNeverHappenError",
    "ThisErrorIsInevitableError",

    # WTF Errors
    "WTFError",
    "IdiotError",
]
