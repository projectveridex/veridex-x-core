"""
==========================================
VERIDEX X
PIPELINE TEST
==========================================
"""

from core.controller import run_veridex


def main():

    print("Running VERIDEX pipeline...\n")

    queue = run_veridex()

    print(f"Pipeline finished.")

    print(f"Jobs waiting for approval: {len(queue)}")

    if queue:

        print("\nFirst opportunity:")

        print(queue[0]["opportunity"].title)


if __name__ == "__main__":

    main()
