"""
VERIDEX X
Hunter Manager
"""

from hunters.github_hunter import scan_github
from core.database import add_opportunity


def run_hunters():
    print("Starting hunters...")

    github_results = scan_github()

    for opportunity in github_results:
        add_opportunity(opportunity)

    print("Hunters completed.")
    print("Opportunities collected:", len(github_results))
