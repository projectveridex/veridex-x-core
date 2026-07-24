"""
==========================================
VERIDEX X
OPEN COLLECTIVE HUNTER
==========================================
"""

from core.opportunity import Opportunity


def scan_open_collective():

    return [

        Opportunity(

            source="OpenCollective",

            title="Funded Community Task",

            description="Community looking for contributors.",

            crypto_payment=True,

            low_competition=True,

            high_frequency=False,

            good_payment=True,

            easy_to_complete=False

        )

    ]
