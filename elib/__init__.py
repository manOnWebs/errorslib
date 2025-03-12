# elib/__init__.py

# Import base errors
from .codeerror import CodeError
from .deverror import DevError
from .dunnoerror import DunnoError
from .hardwareerror import HardwareError
from .logicerror import LogicError
from .usererror import UserError

# Import all subclasses from their respective modules
from .absexc import *
from .usererror import *
from .deverror import *
from .codeerror import *
from .hardwareerror import *
from .logicerror import *
from .dunnoerror import *
from .aierror import *
from .hrerror import *
from .internerror import *
from .managererror import *
from .matherror import *
from .saleserror import *
from .uselesserror import *

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
    "Dogs",
    "AppleError",
    "CatError",
    "CatWarning",
    "DogError",
    "DogWarning",
    "CatAstrophicError",
    "CatastrophicDogError",
    "AIError",
    "KeyboardError",
    "TimeError",
    "InternError",
    "SalesError",
    "HRError",

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
    "WhyIsModemOnFireError",

    # Pet Errors
    "CatBecameRouterError",
    "CatBecameModemError",
    "CatBecameISPError",
    "CatBecameFirewallError",
    "DogBecameRouterError",
    "DogBecameModemError",
    "DogBecameISPError",
    "DogBecameFirewallError",
    "DogAteEthernetCableError",
    "DogAndCatAteEthernetCableAgainError",
    "DogAndCatAteRouterError",
    "DogAndCatAteISPError",
    "CatAteISPError",
    "CatsAteISPError",
    "CatsAreISPError",
    "DogAndCatAreISPError",
    "CatAteEthernetCableError",
    "CatsAteEthernetCableError",
    "CatsAtePCAgainError",
    "CatsAteWorldAgainError",
    "CatsBecamePythonInterpreterAgainError",
    "CatsBecameOperatingSystemAgainError",
    "SubmitFleshError",
    "CatsHaveAlwaysBeenInChargeError",

    # Logic Errors
    "NotAnError",
    "ParadoxError",
    "ThisErrorShouldNeverHappenError",
    "ThisErrorIsInevitableError",

    # WTF Errors
    "WTFError",
    "IdiotError",

    # AI Errors
    "AIHasHadEnoughError",
    "ChatbotExistentialCrisisError",

    # HR Errors
    "FiredInternError",
    "WorkplaceHostilityError",
    "PointlessMandatoryTrainingError",
    "UselessTeamBuildingExerciseError",
    "NoRemoteWorkAllowedError",
    "NoRaisesThisYearError",
    "BuzzwordOverloadError",
    "FiredForTellingTheTruthError",
    "OpenOfficePlanError",
    "WeValueWorkLifeBalanceError",

    # Intern Errors
    "DoesntKnowGitError",
    "AccidentallyDroppedDBError",
    "InfiniteLoopError",
    "PushedSecretsToGitHubError",
    "ForgotToAskError",
    "AskedTooManyQuestionsError",
    "TooMuchStackOverflowError",
    "TooMuchChatGPTError",

    # Manager Errors
    "UnrealisticDeadlineError",
    "ScopeCreepError",
    "JustOneMoreFeatureError",
    "NoDocumentationBudgetError",
    "MeetingOverloadError",
    "AgileGoneWrongError",
    "MicroManagerError",
    "NoUnitTestsError",
    "ThatShouldBeEasyError",

    # Math Errors
    "TooManyDecimalsError",
    "DividedByPotatoError",
    "NegativeZeroError",
    "InfinityOverflowError",

    # Sales Errors
    "SoldFeatureThatDoesntExistError",
    "PromisedImpossibleDeadlineError",
    "GaveAdminAccessToClientError",
    "OverpromisedUnderquotedError",
    "IgnoredTechnicalLimitationsError",

    # More useless errors
    "ExistentialCrisisError",
    "SyntaxPoliceError",
    "TooManyPrintStatementsError",
    "RubberDuckOverflowError",
    "CodeSoBadItWorksError",
    "SpaghettiCodeDetectedError",
]
