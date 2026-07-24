"""
==========================================
VERIDEX X
PIPELINE STATUS
==========================================
"""

STATUS = {

    "hunters": False,

    "normalizer": False,

    "database": False,

    "scoring": False,

    "proposal": False,

    "approval_queue": False,

    "telegram": False

}


def mark(step):

    if step in STATUS:

        STATUS[step] = True


def report():

    print("\n========== PIPELINE STATUS ==========")

    for key, value in STATUS.items():

        print(f"{key}: {'OK' if value else 'PENDING'}")

    print("=====================================\n")
