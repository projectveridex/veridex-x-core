"""
==========================================
VERIDEX X
MAIN CONTROLLER
==========================================
"""

from core.hunter_manager import run_hunters
from core.duplicate_detector import remove_duplicates
from core.proposal_engine import generate_proposal
from core.approval_queue import ApprovalQueue
from core.learning_engine import LearningEngine
from core.logger import log


approval_queue = ApprovalQueue()
learning = LearningEngine()


def run_veridex():

    log("VERIDEX scan started.")

    opportunities = run_hunters()

    opportunities = remove_duplicates(opportunities)

    log(f"{len(opportunities)} unique opportunities found.")

    for opportunity in opportunities:

        proposal = generate_proposal(opportunity)

        approval_queue.add({
            "opportunity": opportunity,
            "proposal": proposal
        })

        learning.record_submission()

    log(
        f"{len(approval_queue.pending())} opportunities waiting for approval."
    )

    return approval_queue.pending()
