"""
VERIDEX X
MASTER HUNTER MANAGER
"""

from hunters.github_live_hunter import scan_github_live
from hunters.gitlab_live_hunter import scan_gitlab_live
from hunters.rss_hunter import scan_rss


def run_hunters():

    opportunities = []

    hunters = [
        ("GitHub", scan_github_live),
        ("GitLab", scan_gitlab_live),
        ("RSS", scan_rss),
    ]

    for name, hunter in hunters:

        try:

            jobs = hunter()

            opportunities.extend(jobs)

            print(f"✅ {name}: {len(jobs)} opportunities")

        except Exception as e:

            print(f"❌ {name} failed: {e}")

    print(f"\n🔥 Total Live Opportunities: {len(opportunities)}")

    return opportunities
