"""Countdown timer."""

import time
from reminder import *
from notif import *


def main():
    # start_timer()
    # read JSON reminder object into dict
    test_reminder = read_input('/Users/garrisonparrish/Python Applications/reminder-app/data/clean keyboard.json')
    print(test_reminder)

    test_reminder_title = test_reminder["title"]
    print(test_reminder_title)

    test_reminder_notes = test_reminder["notes"]
    print(test_reminder_notes)

    start_timer(test_reminder_title, test_reminder_notes)


def countdown(time_input: str) -> None:
    """Given a time in seconds, counts down to the time."""
    # Check if input can be cast to integer type
    if time_input.isdigit():
        t = int(time_input)
    else:
        print("Input is not an integer")
        return
    while t:
        mins, secs = divmod(t, 60)  # time_input / 60 => quotient, remainder
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # return to previous line and overwrite
        time.sleep(1)   # wait for 1 second before looping again
        t -= 1
    print("Time is up!")


def start_timer(reminder_title: str, reminder_notes: str) -> None:
    """Input time in seconds and start timer."""
    time_input = input("Input countdown time in seconds: ")
    countdown(time_input)
    print("Timer completed")
    notify(reminder_title, reminder_notes)  # Push notif with reminder title


if __name__ == "__main__":
    main()