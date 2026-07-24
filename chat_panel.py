"""
==========================================
VERIDEX X
COMMAND CENTER
==========================================
"""

WELCOME = """
==========================================
        VERIDEX X COMMAND CENTER
==========================================

Available Commands

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

            print("Scanning opportunity network...")

        elif command == "jobs":

            print("Displaying available opportunities...")

        elif command == "approve":

            print("Approval mode opened.")

        elif command == "status":

            print("System healthy.")

        elif command == "help":

            print(WELCOME)

        elif command == "exit":

            print("Goodbye Boss.")
            break

        else:

            print("Unknown command.")
