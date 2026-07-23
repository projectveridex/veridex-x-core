"""
VERIDEX X CORE
Public Opportunity Intelligence Engine
"""

VERSION = "0.1.0"

from core.controller import run_veridex


def startup():
    print("================================")
    print(" VERIDEX X ONLINE ")
    print(" Version:", VERSION)
    print("================================")


if __name__ == "__main__":
    startup()
    run_veridex()
