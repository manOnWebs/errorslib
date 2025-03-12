"""
Intern Error
"""

from .absexc import *

class DoesntKnowGitError(InternError):
    """Intern has force-pushed to main. Everything is on fire."""
    pass

class AccidentallyDroppedDBError(InternError):
    """Intern has run `DROP DATABASE production;` because they thought it was a test environment."""
    pass

class InfiniteLoopError(InternError):
    """Intern wrote a loop that will never exit and our servers are space heaters now."""
    pass

class PushedSecretsToGitHubError(InternError):
    """Intern force-pushed AWS keys to main accidentally. Now all of our data is stolen."""
    pass

class ForgotToAskError(InternError):
    """Intern spent 3 days debugging something that could have been solved by asking a question."""
    pass

class AskedTooManyQuestionsError(InternError):
    """Intern has asked 47 questions in the last 10 minutes and you regret encouraging them."""
    pass

class TooMuchStackOverflowError(InternError):
    """Intern copied way too much code from Stack Overflow, and none of it makes sense."""
    pass

class TooMuchChatGPTError(InternError):
    """Intern copied way too much code from ChatGPT and now the entire codebase is broken!"""
    pass