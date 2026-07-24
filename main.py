"""
==========================================
VERIDEX X
BOOT ENGINE
==========================================
"""

from config.settings import MODE
from ui.chat_panel import start_chat
from core.scheduler import start_scheduler


def startup():

    print("""
==========================================
VERIDEX X ONLINE
==========================================
""")

    if MODE.upper() == "AUTO":

        start_scheduler()

    else:

        start_chat()


if __name__ == "__main__":
    startup()
