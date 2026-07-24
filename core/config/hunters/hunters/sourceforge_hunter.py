"""
==========================================
VERIDEX X
SOURCEFORGE HUNTER
==========================================
"""

from core.opportunity import Opportunity


def scan_sourceforge():

    return [

        Opportunity(

            source="SourceForge",

            title="Open Source Task",

            description="Repository requesting contributor.",

            crypto_payment=False,

            low_competition=True,

            high_frequency=False,

            good_payment=False,

            easy_to_complete=True

        )

    ]
