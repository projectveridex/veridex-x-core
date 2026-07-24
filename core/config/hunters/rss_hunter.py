"""
==========================================
VERIDEX X
RSS HUNTER
==========================================
"""

from core.opportunity import Opportunity


def scan_rss():

    return [

        Opportunity(

            source="RSS",

            title="Public Opportunity Feed",

            description="New opportunity discovered through RSS.",

            crypto_payment=False,

            low_competition=True,

            high_frequency=True,

            good_payment=True,

            easy_to_complete=True

        )

    ]
