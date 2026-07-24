"""
==========================================
VERIDEX X
COMMAND CENTER
==========================================
"""

from core.controller import (
    run_veridex,
    approval_queue
)

WELCOME = """
==========================================
VERIDEX X COMMAND CENTER
==========================================

Commands

scan
approve
jobs
status
help
exit

==========================================
"""


def start_chat():

    print(WELCOME)

    while True:

        command = input("Boss > ").strip().lower()

        if command == "scan":

            print("\nLaunching VERIDEX...\n")

            run_veridex()

        elif command == "approve":

            item = approval_queue.approve()

            if item is None:

                print("No opportunities waiting.")

            else:

                print("\n======================")
                print("APPROVED")
                print("======================")
                print(item["opportunity"].title)
                print(item["proposal"])

        elif command == "jobs":

            print(
                f"{len(approval_queue.pending())} job(s) waiting."
            )

        elif command == "status":

            print("""
System Status

Hunters : READY
Brain : READY
Queue : READY
Learning : READY
Scheduler : READY
""")

        elif command == "help":

            print(WELCOME)

        elif command == "exit":

            print("Goodbye Boss.")
            break

        else:

            print("Unknown command.")
