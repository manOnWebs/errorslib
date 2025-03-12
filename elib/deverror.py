"""
Developer Error
"""

from .absexc import *

# ==============================
# Developer-Related Errors
# ==============================

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

class StackOverflowCopyPasteError(DevError):
    """Raised when copied Stack Overflow code doesn't actually work but you have no idea why."""
    pass

class WorksOnMyMachineError(DevError):
    """Code runs fine on the dev's laptop but crashes everywhere else."""
    pass

class CommentedOutCodeError(DevError):
    """Raised when half the codebase is commented out, and no one knows why."""
    pass

class RefactoredUntilBrokeError(DevError):
    """Code was refactored so much that it no longer works."""
    pass

class RegexGoneWrongError(DevError):
    """Raised when a regex meant to solve a small problem causes **catastrophic** issues."""
    pass

class CodeTooUglyError(DevError):
    """Raised when your code is so unreadable that any user needs to file for visual harassment"""
    pass

class TooManyCommentsError(DevError):
    """Raised when we decide that you're explaining too much.... it's just if-else, Steve."""
    pass

class NotEnoughCommentsError(DevError):
    """Raised when we judge you for writing cryptic, undocumented spaghetti."""
    pass

class VariableNameCringeError(DevError):
    """Raised when we refuse to execute because you named a variable xX_DeathKiller42_Xx."""
    pass