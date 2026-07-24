"""
==========================================
VERIDEX X
LOGGER
==========================================
"""

from datetime import datetime


def log(message):

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{timestamp}] {message}")


def log_scan(source, total):

    log(f"{source} scanned. Opportunities: {total}")


def log_submission(title):

    log(f"Submitted proposal for: {title}")


def log_completion(title):

    log(f"Completed: {title}")


def log_error(error):

    log(f"ERROR: {error}")
