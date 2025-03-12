"""
HR Error
"""

from .absexc import *

class FiredInternError(HRError, InternError):
    """Intern made one too many mistakes. Now they’re updating their LinkedIn."""
    pass

class WorkplaceHostilityError(HRError):
    """Raised when the team is forced to use JIRA and morale absolutely plummets."""
    pass

class PointlessMandatoryTrainingError(HRError):
    """HR has scheduled a 'mandatory' training on something no one needs."""
    pass

class UselessTeamBuildingExerciseError(HRError):
    """HR made you do trust falls instead of fixing actual workplace issues."""
    pass

class NoRemoteWorkAllowedError(HRError):
    """Raised when HR insists that developers work in-office, despite 100% of the job being online."""
    pass

class NoRaisesThisYearError(HRError):
    """HR announces that ‘we’re like a family,’ right before telling you there’s no budget for raises. The fuck?"""
    pass

class BuzzwordOverloadError(HRError):
    """HR has sent an email filled with 'synergy,' 'alignment,' and 'growth mindset.'"""
    pass

class FiredForTellingTheTruthError(HRError):
    """You told management their idea was bad. Now you’re unemployed."""
    pass

class OpenOfficePlanError(HRError):
    """HR decided an open office plan was a good idea. Productivity drops to 0%."""
    pass

class WeValueWorkLifeBalanceError(HRError):
    """HR says they care about work-life balance while forcing you to work weekends for half of your day"""
    pass