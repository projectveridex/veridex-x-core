"""
==========================================
VERIDEX X
LEARNING ENGINE
==========================================
"""


class LearningEngine:

    def __init__(self):

        self.total_jobs = 0
        self.accepted = 0
        self.rejected = 0
        self.completed = 0

    def record_submission(self):

        self.total_jobs += 1

    def record_acceptance(self):

        self.accepted += 1

    def record_rejection(self):

        self.rejected += 1

    def record_completion(self):

        self.completed += 1

    def stats(self):

        return {
            "jobs": self.total_jobs,
            "accepted": self.accepted,
            "rejected": self.rejected,
            "completed": self.completed
        }
