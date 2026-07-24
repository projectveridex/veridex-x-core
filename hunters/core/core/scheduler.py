"""
==========================================
VERIDEX X
AUTO SCHEDULER
==========================================
"""

import time

from core.hunter_manager import run_hunters


SCAN_INTERVAL = 300


def start_scheduler():

    print("""
==========================================
VERIDEX AUTO MODE
==========================================
""")

    while True:

        print("\nStarting Hunter Cycle...\n")

        run_hunters()

        print(f"\nWaiting {SCAN_INTERVAL} seconds...\n")

        time.sleep(SCAN_INTERVAL)
