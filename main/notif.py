import time
import pync


def notify() -> None:
    pync.notify('Hello World', title='Python')
    # pync.notify("Hello World!")
    # pync.notify('Hello World', open='http://github.com/')
    # pync.notify('Hello World', activate='com.apple.Safari')


def notify_delay(interval: int) -> None:
    """Waits a specified number of seconds - interval: wait time (seconds)"""
    time.sleep(interval)
    # get title from json file
    pync.notify("Hello", title='Python')

def main() -> None:
    notify()


if __name__ == "__main__":
    main()