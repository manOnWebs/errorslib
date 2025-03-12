"""
AI Error
"""

from .absexc import *

class AIHasHadEnoughError(AIError):
    """Raised when GitHub Copilot refuses to help you because your code is a lost cause."""
    pass

class ChatbotExistentialCrisisError(AIError):
    """Raised when an AI assistant starts questioning its own existence mid-conversation."""
    pass