"""
==========================================
VERIDEX X
OPPORTUNITY MODEL
==========================================
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Opportunity:

    source: str
    title: str
    description: str

    crypto_payment: bool = False
    low_competition: bool = False
    high_frequency: bool = False
    good_payment: bool = False
    easy_to_complete: bool = False

    score: int = 0

    created_at: str = datetime.utcnow().isoformat()

    status: str = "NEW"

    approved: bool = False

    submitted: bool = False

    completed: bool = False
