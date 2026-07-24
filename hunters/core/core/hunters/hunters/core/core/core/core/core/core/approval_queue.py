"""
==========================================
VERIDEX X
APPROVAL QUEUE
==========================================
"""


class ApprovalQueue:

    def __init__(self):

        self.queue = []

    def add(self, opportunity):

        self.queue.append(opportunity)

    def pending(self):

        return self.queue

    def approve(self):

        if not self.queue:
            return None

        return self.queue.pop(0)
