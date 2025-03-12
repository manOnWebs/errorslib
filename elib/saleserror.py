"""
Sales Error
"""

from .absexc import *

class SoldFeatureThatDoesntExistError(SalesError):
    """Salesperson sold a feature that doesn’t exist. Now we have to build it. Quickly."""
    pass

class PromisedImpossibleDeadlineError(SalesError):
    """Sales team promised delivery in 2 weeks. It requires 6 months of development."""
    pass

class GaveAdminAccessToClientError(SalesError):
    """Salesperson gave full admin access to a client. Chaos ensues."""
    pass

class OverpromisedUnderquotedError(SalesError):
    """Sales team promised 100 features for the price of 1. We're bankrupt now."""
    pass

class IgnoredTechnicalLimitationsError(SalesError):
    """Sales team promised a feature that defies the laws of physics."""
    pass