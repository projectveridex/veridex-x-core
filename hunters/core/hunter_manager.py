"""
==========================================
VERIDEX X
HUNTER MANAGER
==========================================
"""

from hunters.github_hunter import scan_github
from hunters.gitlab_hunter import scan_gitlab

all_opportunities = []


def run_hunters():

    global all_opportunities

    print("Launching Hunters...\n")

    github_jobs = scan_github()
    gitlab_jobs = scan_gitlab()

    all_opportunities = []

    all_opportunities.extend(github_jobs)
    all_opportunities.extend(gitlab_jobs)

    print(f"Total opportunities found: {len(all_opportunities)}")

    return all_opportunities
