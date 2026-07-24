"""
==========================================
VERIDEX X
HUNTER MANAGER
==========================================
"""

from hunters.github_hunter import scan_github
from hunters.gitlab_hunter import scan_gitlab
from hunters.codeberg_hunter import scan_codeberg
from hunters.rss_hunter import scan_rss
from hunters.sourceforge_hunter import scan_sourceforge
from hunters.open_collective_hunter import scan_open_collective


def run_hunters():

    opportunities = []

    opportunities.extend(scan_github())
    opportunities.extend(scan_gitlab())
    opportunities.extend(scan_codeberg())
    opportunities.extend(scan_rss())
    opportunities.extend(scan_sourceforge())
    opportunities.extend(scan_open_collective())

    print(f"Hunters collected {len(opportunities)} opportunities.")

    return opportunities
