"""
Pet errors
"""

from .absexc import *
from .dunnoerror import *
from .hardwareerror import *


class Cat(AbsurdClass):
    """Generic Cat-Class"""
    pass

class Cats(AbsurdClass):
    """Generic Cats-Class"""
    pass

class Dog(AbsurdClass):
    """Generic Dog-Class"""
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

class CatBecameRouterError(WifiWarning, DunnoWarning, CatWarning, Cat):
    """Cat became the router again"""
    pass

class CatBecameModemError(WifiWarning, DunnoWarning, CatWarning, Cat):
    """Cat became the modem again"""
    pass

class CatBecameISPError(ISPError, DunnoError, CatError, Cat):
    """The cat is the ISP now."""
    pass

class CatBecameFirewallError(WiFiError, DunnoError, CatError, Cat):
    """The furwall"""
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

class DogAteTheEthernetCableError(NoInternetError, WiFiError, HardwareWarning):
    """damn dog"""
    pass

class DogAndCatAteTheEthernetCableErrorAgain(NoInternetError, WiFiError, HardwareWarning, CatWarning, Cat, Dog):
    """not again"""
    pass

class DogAndCatAteTheRouterError(NoInternetError, WiFiError, HardwareError, CatError, DogAteTheEthernetCableError, WTFError, Cat, Dog):
    """how did they even manage this"""
    pass

class DogAndCatAteTheISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteTheEthernetCableError, Cat, Dog):
    """I have no internet, and I think my pets are responsible for the downfall of an entire ISP."""
    pass

class CatAteTheISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteTheEthernetCableError, Cat):
    """my internet is RUINED because of YOU, samuel"""
    pass

class CatsAteTheISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteTheEthernetCableError, Cats):
    """WHAT THE FUCK IS WITH YOU GUYS EATING ALL OF MY ISPS"""
    pass

class CatsAreTheISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteTheEthernetCableError, Cat):
    """what the hell, guys"""
    pass

class DogAndCatAreTheISPError(NoInternetError, ISPError, HardwareError, CatError, DogAteTheEthernetCableError, Cat, Dog):
    """what the hell"""
    pass

class CatAteTheEthernetCableError(NoInternetError, WiFiError, HardwareWarning, Cat):
    """damn it samuel"""
    pass

class CatsAteTheEthernetCableError(NoInternetError, WiFiError, HardwareWarning, Cats):
    """motherfucker"""
    pass

class CatsAteThePCAgainError(CatError, WTFError, HardwareError, Cats):
    """How did they even manage this again for the third time this week, I even put Anti-Anti-Chew on my PC"""
    pass

class CatsAteTheWorldAgainError(CatAstrophicError, Cats):
    """how the fuck"""
    print("how do they do this")
    pass

class CatsBecameThePythonInterpreterAgain(CatAstrophicError, Cats):
    """wtf"""
    pass