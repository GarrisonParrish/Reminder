"""Push notification methods."""

import time
import pync  # allows program to send user notifications to Mac OS operating system
from main.reminder import Reminder
# from read_write import read_to_reminder


def notify(r: Reminder) -> None:
    pync.notify(r.getNotes(), title="Reminder", subtitle=r.getTitle())


def notify_delay(r: Reminder, interval: int) -> None:
    """Waits a specified number of seconds - interval: wait time (seconds)"""
    time.sleep(interval)
    # get title from json file
    pync.notify(r.getNotes(), title="Reminder", subtitle=r.getTitle())



# notify(read_to_reminder("data/Get a unicorn.json"))