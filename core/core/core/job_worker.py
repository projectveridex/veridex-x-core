"""
==========================================
VERIDEX X
JOB WORKER
==========================================
"""


class JobWorker:

    def __init__(self):

        self.active_jobs = []

    def start(self, opportunity):

        self.active_jobs.append(opportunity)

        print(f"Starting work on: {opportunity.title}")

    def finish(self, opportunity):

        if opportunity in self.active_jobs:

            self.active_jobs.remove(opportunity)

            print(f"Finished: {opportunity.title}")

    def running(self):

        return self.active_jobs
