"""
==========================================
VERIDEX X
MASTER CONTROLLER
==========================================
"""

from core.hunter_manager import run_hunters
from core.duplicate_detector import remove_duplicates
from core.proposal_engine import generate_proposal
from core.learning_engine import LearningEngine
from core.approval_queue import ApprovalQueue
from core.job_worker import JobWorker
from core.task_planner import TaskPlanner
from core.work_validator import WorkValidator
from core.logger import log
from core.database import add_record

learning = LearningEngine()
approval_queue = ApprovalQueue()
planner = TaskPlanner()
worker = JobWorker()
validator = WorkValidator()

# Stores the latest opportunities found
LAST_SCAN = []


def run_veridex():

    global LAST_SCAN

    log("Starting VERIDEX pipeline...")

    opportunities = run_hunters()

    opportunities = remove_duplicates(opportunities)

    LAST_SCAN = opportunities

    for opportunity in opportunities:

        add_record({
            "title": opportunity.title,
            "source": opportunity.source,
            "status": "NEW"
        })

        plan = planner.plan(opportunity)

        proposal = generate_proposal(opportunity)

        approval_queue.add({
            "opportunity": opportunity,
            "plan": plan,
            "proposal": proposal
        })

        learning.record_submission()

    log(
        f"{len(approval_queue.pending())} jobs waiting for approval."
    )

    return approval_queue.pending()


def get_last_scan():

    return LAST_SCAN
