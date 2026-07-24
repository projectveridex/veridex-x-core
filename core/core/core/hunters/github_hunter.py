"""
VERIDEX X
GitHub Hunter
"""

from core.opportunity import Opportunity


def scan_github():

    return [

        Opportunity(

            source="GitHub",

            title="GitHub Public Issue",

            description="Open source repository requesting help.",

            crypto_payment=False,

            low_competition=True,

            high_frequency=True,

            good_payment=False,

            easy_to_complete=True

        )

    ]
