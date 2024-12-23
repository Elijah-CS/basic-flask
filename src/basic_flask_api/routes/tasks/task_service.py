import time

import logging

logger = logging.getLogger("task_service")

def do_something(seconds):
    print("Starting something")
    time.sleep(seconds)
    print("Ending something")