"""
==========================================
VERIDEX X
REAL RSS HUNTER
==========================================
"""

import feedparser

from core.opportunity import Opportunity


RSS_FEEDS = [

    "https://hnrss.org/jobs",

    "https://hnrss.org/newest"

]


def scan_rss():

    opportunities = []

    for url in RSS_FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:

            opportunities.append(

                Opportunity(

                    source="RSS",

                    title=entry.title,

                    description=getattr(entry, "summary", ""),

                    crypto_payment=False,

                    low_competition=True,

                    high_frequency=True,

                    good_payment=True,

                    easy_to_complete=True

                )

            )

    return opportunities
