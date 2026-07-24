"""
VERIDEX X
GitLab Hunter
"""

from core.opportunity import Opportunity


def scan_gitlab():

    return [

        Opportunity(

            source="GitLab",

            title="GitLab Open Issue",

            description="Repository requesting contributors.",

            crypto_payment=False,

            low_competition=True,

            high_frequency=True,

            good_payment=False,

            easy_to_complete=True

        )

    ]
