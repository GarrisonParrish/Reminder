import time
import pync


def main() -> None:
    # notify_delay(10, "Take out trash")
    notify("", "")


def notify(reminder_title: str, reminder_notes: str) -> None:
    # pync.notify(reminder_notes, title=reminder_title)
    pync.notify("Hello World!", subtitle="Hey there")  # appIcon does not appear to work
    # pync.notify('Hello World', open='http://github.com/')
    # pync.notify('Hello World', activate='com.apple.Safari')


def notify_delay(interval: int, reminder_str: str) -> None:
    """Waits a specified number of seconds - interval: wait time (seconds)"""
    time.sleep(interval)
    # get title from json file
    pync.notify(reminder_str, title="Reminder")


if __name__ == "__main__":
    main()