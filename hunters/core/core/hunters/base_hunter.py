"""
==========================================
VERIDEX X
BASE HUNTER
==========================================
"""

class BaseHunter:

    def __init__(self, name):

        self.name = name

    def scan(self):

        raise NotImplementedError(
            f"{self.name} has not implemented scan()."
        )

    def normalize(self, opportunity):

        return {
            "source": opportunity.get("source"),
            "title": opportunity.get("title"),
            "description": opportunity.get("description"),
            "crypto_payment": opportunity.get("crypto_payment", False),
            "low_competition": opportunity.get("low_competition", False),
            "high_frequency": opportunity.get("high_frequency", False),
            "good_payment": opportunity.get("good_payment", False),
            "easy_to_complete": opportunity.get("easy_to_complete", False)
        }
