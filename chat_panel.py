"""
==========================================
VERIDEX X
COMMAND CENTER
==========================================
"""

from core.controller import run_veridex

WELCOME = """
==========================================
        VERIDEX X COMMAND CENTER
==========================================

Commands

scan
jobs
approve
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

            print("\nLaunching VERIDEX Hunters...\n")

            run_veridex()

        elif command == "jobs":

            print("Opening opportunity database...")

        elif command == "approve":

            print("Approval Center coming soon...")

        elif command == "status":

            print("""
System Status

Hunters : READY
Brain   : READY
Database: READY
Crypto  : READY
Controller : READY
""")

        elif command == "help":

            print(WELCOME)

        elif command == "exit":

            print("Goodbye Boss.")
            break

        else:

            print("Unknown command.")
