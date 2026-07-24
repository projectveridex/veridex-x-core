"""
==========================================
VERIDEX X
LIVE GITHUB HUNTER
==========================================
"""

import requests

from core.opportunity import Opportunity


URL = (
    "https://api.github.com/search/issues"
    "?q=label:\"help wanted\"+state:open&per_page=20"
)


def scan_github_live():

    opportunities = []

    try:

        response = requests.get(
            URL,
            timeout=20,
            headers={
                "Accept": "application/vnd.github+json"
            }
        )

        if response.status_code != 200:
            return opportunities

        data = response.json()

        for item in data.get("items", []):

            opportunities.append(

                Opportunity(

                    source="GitHub",

                    title=item["title"],

                    description=item.get("body", "")[:500],

                    crypto_payment=False,

                    low_competition=True,

                    high_frequency=True,

                    good_payment=False,

                    easy_to_complete=True

                )

            )

    except Exception:

        pass

    return opportunities
