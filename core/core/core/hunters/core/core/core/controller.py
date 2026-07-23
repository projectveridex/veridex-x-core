"""
VERIDEX X
Main Controller
"""

from core.hunter_manager import run_hunters
from core.database import get_opportunities
from core.analyzer import analyze_opportunity


def run_veridex():
    print("Starting VERIDEX X...")

    run_hunters()

    opportunities = get_opportunities()

    print("\nAnalyzing opportunities...\n")

    for opportunity in opportunities:
        result = analyze_opportunity(opportunity)

        print("----------------------------")
        print("Source:", result["opportunity"]["source"])
        print("Title:", result["opportunity"]["title"])
        print("Score:", result["score"])
        print("Priority:", result["priority"])
        print("Payment:", result["payment"]["status"])
        print("----------------------------")


if __name__ == "__main__":
    run_veridex()
