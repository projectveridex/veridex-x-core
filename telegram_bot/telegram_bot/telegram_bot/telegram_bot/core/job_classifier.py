"""
==========================================
VERIDEX X
JOB CLASSIFIER
==========================================
"""

def classify(opportunity):

    text = (
        f"{opportunity.title} {opportunity.description}"
    ).lower()

    if "wordpress" in text:
        return "wordpress"

    if "landing page" in text:
        return "landing_page"

    if "bug" in text:
        return "bug_fix"

    if "research" in text:
        return "research"

    if "write" in text or "content" in text:
        return "writing"

    return "general"
