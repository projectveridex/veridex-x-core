"""
VERIDEX X
Opportunity Database Core
"""

opportunities = []


def add_opportunity(opportunity):
    opportunities.append(opportunity)


def get_opportunities():
    return opportunities


def clear_opportunities():
    opportunities.clear()
