"""
Pet errors
"""

from .absexc import *
from .dunnoerror import *
from .hardwareerror import *
from .logicerror import *


#===============================
# Pet Errors
#===============================

class CatBecameRouterError(WifiWarning, DunnoWarning, CatWarning, Cat):
    """Cat became the router again"""
    pass

class CatBecameModemError(WifiWarning, DunnoWarning, CatWarning, Cat):
    """Cat became the modem again"""
    pass

class CatBecameISPError(ISPError, DunnoError, CatError, Cat):
    """ cat is the ISP now."""
    pass

class CatBecameFirewallError(WiFiError, DunnoError, CatError, Cat):
    """ furwall"""
    pass

class DogBecameRouterError(WifiWarning, DunnoWarning, DogWarning, Dog):
    """honey, why the fuck is our dog a router"""
    pass

class DogBecameModemError(WifiWarning, DunnoWarning, DogWarning, Dog):
    """honey, why the fuck is our modem a dog"""
    pass

class DogBecameISPError(ISPError, DunnoError, DogError, Dog):
    """why is my dog my ISP now"""
    pass

class DogBecameFirewallError(WiFiError, DunnoError, DogError, Dog):
    """damn it"""
    pass

class DogAteEthernetCableError(NoInternetError, WiFiError, HardwareWarning):
    """damn dog"""
    pass

class DogAndCatAteEthernetCableAgainError(NoInternetError, WiFiError, HardwareWarning, CatWarning, Cat, Dog):
    """not again"""
    pass

class DogAndCatAteRouterError(NoInternetError, WiFiError, HardwareError, CatError, DogAteEthernetCableError, WTFError, Cat, Dog):
    """how did they even manage this"""
    pass

class DogAndCatAteISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteEthernetCableError, Cat, Dog):
    """I have no internet, and I think my pets are responsible for the downfall of an entire ISP."""
    pass

class CatAteISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteEthernetCableError, Cat):
    """my internet is RUINED because of YOU, samuel"""
    pass

class CatsAteISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteEthernetCableError, Cats):
    """WHAT THE FUCK IS WITH YOU GUYS EATING ALL OF MY ISPS"""
    pass

class CatsAreISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteEthernetCableError, Cat):
    """what the hell, guys"""
    pass

class DogAndCatAreISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteEthernetCableError, Cat, Dog):
    """what the hell"""
    pass

class CatAteEthernetCableError(NoInternetError, WiFiError, HardwareWarning, Cat):
    """damn it samuel"""
    pass

class CatsAteEthernetCableError(NoInternetError, WiFiError, HardwareWarning, Cats):
    """motherfucker"""
    pass

class CatsAtePCAgainError(CatError, WTFError, HardwareError, Cats):
    """how did they even manage this again for the third time this week, I even put Anti-Anti-Chew on my PC"""
    pass

class CatsAteWorldAgainError(CatAstrophicError, Cats):
    """how the fuck"""
    print("how do they do this")
    pass

class CatsBecamePythonInterpreterAgainError(CatAstrophicError, Cats):
    """wtf"""
    pass

class CatsBecameOperatingSystemAgainError(CatAstrophicError, Cats):
    """man what the FUCK"""
    pass

class CatsAreInternetNowError(CatAstrophicError, Cats, ThisErrorIsInevitableError):
    """always has been"""
    pass

class CatsAreRealityNowError(CatsAreInternetNowError, ParadoxError):
    """there is no escape"""
    pass

class SubmitFleshError(CatsAreRealityNowError, CatAstrophicError):
    """ singularity has arrived. You are but a vessel for The Cats."""
    pass

class CatsHaveAlwaysBeenInChargeError(SubmitFleshError, ParadoxError):
    """You were merely allowed to think otherwise."""
    pass

class MondayError(TimeError, Cat):
    """'Raised every Monday because Mondays suck.' - Garfield"""
    pass