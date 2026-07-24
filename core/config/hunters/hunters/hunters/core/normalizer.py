"""
==========================================
VERIDEX X
NORMALIZER
==========================================
"""

from core.opportunity import Opportunity


def normalize(raw, source):

    return Opportunity(

        source=source,

        title=raw.get("title", ""),

        description=raw.get("description", ""),

        crypto_payment=raw.get("crypto_payment", False),

        low_competition=raw.get("low_competition", False),

        high_frequency=raw.get("high_frequency", False),

        good_payment=raw.get("good_payment", False),

        easy_to_complete=raw.get("easy_to_complete", False)

    )
