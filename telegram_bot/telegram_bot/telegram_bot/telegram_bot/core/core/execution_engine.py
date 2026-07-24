"""
==========================================
VERIDEX X
EXECUTION ENGINE
==========================================
"""

from core.job_classifier import classify


def execute(approved_job):

    opportunity = approved_job["opportunity"]

    job_type = classify(opportunity)

    return {

        "job_type": job_type,

        "status": "READY",

        "next_step": f"Load {job_type} workflow"

    }
