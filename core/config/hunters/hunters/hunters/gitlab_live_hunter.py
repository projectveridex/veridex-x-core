"""
==========================================
VERIDEX X
LIVE GITLAB HUNTER
==========================================
"""

import requests

from core.opportunity import Opportunity

URL = "https://gitlab.com/api/v4/projects?simple=true&per_page=20"


def scan_gitlab_live():

    opportunities = []

    try:

        response = requests.get(URL, timeout=20)

        if response.status_code != 200:
            return opportunities

        projects = response.json()

        for project in projects:

            opportunities.append(

                Opportunity(

                    source="GitLab",

                    title=project.get("name", "Unknown Project"),

                    description=project.get("description") or "",

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
