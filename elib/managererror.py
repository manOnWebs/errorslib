"""
Manager Error
"""

from .absexc import *

class UnrealisticDeadlineError(ManagerError):
    """Manager has set a deadline that assumes developers don't need sleep, food, or sanity."""
    pass

class ScopeCreepError(ManagerError):
    """Project scope has expanded so much that it now requires AI, blockchain, and teleportation."""
    pass

class JustOneMoreFeatureError(ManagerError):
    """Manager asks for 'just one more feature' five minutes before launch."""
    pass

class NoDocumentationBudgetError(ManagerError):
    """Manager refuses to allocate time for documentation, then complains when no one understands the code."""
    pass

class MeetingOverloadError(ManagerError):
    """Developer has spent more time in meetings than actually coding."""
    pass

class AgileGoneWrongError(ManagerError):
    """Agile process has devolved into chaos, daily stand-ups now last 2 hours."""
    pass

class MicroManagerError(ManagerError):
    """Manager wants to review every line of code personally. Even print statements."""
    pass

class NoUnitTestsError(ManagerError):
    """Manager says we don’t need unit tests. We will regret this."""
    pass

class ThatShouldBeEasyError(ManagerError):
    """Manager says, ‘That should be easy’ about something requiring 3 months of R&D."""
    pass