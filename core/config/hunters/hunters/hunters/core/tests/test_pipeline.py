from core.controller import run_veridex
from core.pipeline_status import report


def main():

    print("Starting VERIDEX validation...\n")

    queue = run_veridex()

    report()

    print(f"Approval Queue: {len(queue)}")


if __name__ == "__main__":

    main()
