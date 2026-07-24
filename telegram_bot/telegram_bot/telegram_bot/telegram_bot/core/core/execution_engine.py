"""
==========================================
VERIDEX X
EXECUTION ENGINE
==========================================
"""

from core.job_classifier import classify

from workflows.general import run as general_workflow


def execute(approved_job):

    opportunity = approved_job["opportunity"]

    job_type = classify(opportunity)

    if job_type == "general":

        result = general_workflow(approved_job)

    else:

        result = general_workflow(approved_job)

    return {

        "job_type": job_type,

        "status": result["status"],

        "workflow_steps": result["steps"]

    }
