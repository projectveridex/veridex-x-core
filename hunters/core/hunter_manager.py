"""
VERIDEX X
MASTER HUNTER MANAGER
"""

from hunters.github_live_hunter import scan_github_live
from hunters.gitlab_live_hunter import scan_gitlab_live
from hunters.rss_hunter import scan_rss


def run_hunters():

    opportunities = []

    opportunities.extend(scan_github_live())

    opportunities.extend(scan_gitlab_live())

    opportunities.extend(scan_rss())

    print(f"Collected {len(opportunities)} live opportunities.")

    return opportunities
