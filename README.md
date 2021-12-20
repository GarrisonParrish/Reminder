# Reminder app

A simple app to set reminders and create a todo list. 

## Format
Reminders have a title and metadata. User can add as many tags as they want to the metadata section.
Reminders have a notes section as a string.

format:

``
{   
    "title": "Dinner with Fake-chan",
    "metadata": [
        "imaginary", "not real", "dating",
    ],
    "notes": "I can't wait to have dinner with Fake-chan! She's so nice and sweet, I love spending time with her!"
}
``

### TODO:
- Write a function to look up a reminder by title
- Expanded lookup function to include metadata
- Super advanced version looks up by keywords (can have title and any metadata in any order)
- Multithreading or something to allow app to run in background
- Some way to measure time when computer is off (compare to system time?)
- Add support for notifications when time is reached ( use pync.notify() )
- GUI