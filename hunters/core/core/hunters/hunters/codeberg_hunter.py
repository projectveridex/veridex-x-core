"""
VERIDEX X
Codeberg Hunter
"""

from core.opportunity import Opportunity


def scan_codeberg():

    return [

        Opportunity(

            source="Codeberg",

            title="Codeberg Contribution",

            description="Community repository looking for help.",

            crypto_payment=False,

            low_competition=True,

            high_frequency=True,

            good_payment=False,

            easy_to_complete=True

        )

    ]
