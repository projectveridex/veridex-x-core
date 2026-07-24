"""
==========================================
VERIDEX X
DUPLICATE DETECTOR
==========================================
"""

import hashlib


def fingerprint(opportunity):

    raw = (
        opportunity.title +
        opportunity.description +
        opportunity.source
    )

    return hashlib.sha256(raw.encode()).hexdigest()


def remove_duplicates(opportunities):

    seen = set()

    unique = []

    for job in opportunities:

        fp = fingerprint(job)

        if fp not in seen:

            seen.add(fp)

            unique.append(job)

    return unique
