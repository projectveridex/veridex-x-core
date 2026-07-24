"""
==========================================
VERIDEX X
CODEBERG HUNTER
==========================================
"""

from hunters.base_hunter import BaseHunter


class CodebergHunter(BaseHunter):

    def __init__(self):

        super().__init__("Codeberg")

    def scan(self):

        jobs = []

        opportunity = {
            "source": "Codeberg",
            "title": "Open Source Contribution",
            "description": "Public repository looking for contributors.",
            "crypto_payment": False,
            "low_competition": True,
            "high_frequency": True,
            "good_payment": False,
            "easy_to_complete": True
        }

        jobs.append(self.normalize(opportunity))

        return jobs
