"""
VERIDEX X
Opportunity Analyzer
"""

from core.scoring import score_opportunity, classify
from core.crypto_filter import payment_preference


def analyze_opportunity(opportunity):
    score = score_opportunity(opportunity)

    payment = payment_preference(opportunity)

    result = {
        "opportunity": opportunity,
        "score": score,
        "priority": classify(score),
        "payment": payment
    }

    return result
