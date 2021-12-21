"""Test the Reminders class."""

from main.reminder import *

# Run module with 'python -m pytest tests/test_reminders.py'

def test_get_reminders():
    r1: Reminder = Reminder("Clean room", ["clean", "room"], "I need to clean my room.")
    r2: Reminder = Reminder("Wash dishes", ["wash", "dishes"], "I need to wash the dishes.")
    r3: Reminder = Reminder("Mop floor", ["mop", "floor"], "I need to mop the floor.")

    reminders: Reminders = Reminders([r1, r2, r3])
    assert reminders.getReminders() == [r1, r2, r3]

def test_get_reminder_by_index_01():
    r1: Reminder = Reminder("Clean room", ["clean", "room"], "I need to clean my room.")
    r2: Reminder = Reminder("Wash dishes", ["wash", "dishes"], "I need to wash the dishes.")
    r3: Reminder = Reminder("Mop floor", ["mop", "floor"], "I need to mop the floor.")

    reminders: Reminders = Reminders([r1, r2, r3])
    assert reminders.getReminderByIndex(0) == r1

def test_get_reminder_by_index_02():
    r1: Reminder = Reminder("Clean room", ["clean", "room"], "I need to clean my room.")
    r2: Reminder = Reminder("Wash dishes", ["wash", "dishes"], "I need to wash the dishes.")
    r3: Reminder = Reminder("Mop floor", ["mop", "floor"], "I need to mop the floor.")

    reminders: Reminders = Reminders([r1, r2, r3])
    assert reminders.getReminderByIndex(1) == r2

def test_get_reminder_by_title():
    r1: Reminder = Reminder("Clean room", ["clean", "room"], "I need to clean my room.")
    r2: Reminder = Reminder("Wash dishes", ["wash", "dishes"], "I need to wash the dishes.")
    r3: Reminder = Reminder("Mop floor", ["mop", "floor"], "I need to mop the floor.")

    reminders: Reminders = Reminders([r1, r2, r3])
    assert reminders.getReminderByTitle("Wash dishes") == r2

def test_get_reminders_by_meta_tag_01():
    r1: Reminder = Reminder("", ["clean", "room"], "")
    r2: Reminder = Reminder("", ["wash", "dishes"], "")
    r3: Reminder = Reminder("", ["mop", "floor"], "")

    reminders: Reminders = Reminders([r1, r2, r3])
    assert reminders.getRemindersByMetaTag("room") == [r1]

def test_get_reminders_by_meta_tag_02():
    r1: Reminder = Reminder("", ["clean", "room"], "")
    r2: Reminder = Reminder("", ["wash", "dishes"], "")
    r3: Reminder = Reminder("", ["mop", "floor"], "")

    reminders: Reminders = Reminders([r1, r2, r3])
    assert reminders.getRemindersByMetaTag("floor") == [r3]

def test_get_reminders_by_meta_tag_03():
    r1: Reminder = Reminder("", ["clean", "room"], "")
    r2: Reminder = Reminder("", ["wash", "dishes"], "")
    r3: Reminder = Reminder("", ["clean", "mop", "floor"], "")

    reminders: Reminders = Reminders([r1, r2, r3])
    assert reminders.getRemindersByMetaTag("clean") == [r1, r3]

def test_get_reminders_by_meta_tag_04():
    r1: Reminder = Reminder("", ["clean", "room"], "")
    r2: Reminder = Reminder("", ["wash", "dishes"], "")
    r3: Reminder = Reminder("", ["clean", "clean", "floor"], "")

    reminders: Reminders = Reminders([r1, r2, r3])
    assert reminders.getRemindersByMetaTag("clean") == [r1, r3]

def test_add_reminder():
    r1: Reminder = Reminder("Clean room", ["clean", "room"], "I need to clean my room.")
    r2: Reminder = Reminder("Wash dishes", ["wash", "dishes"], "I need to wash the dishes.")
    r3: Reminder = Reminder("Mop floor", ["mop", "floor"], "I need to mop the floor.")
    reminders: Reminders = Reminders([r1, r2, r3])
    r4: Reminder = Reminder("Cook dinner", ["cook", "dinner"], "I need to cook dinner.")
    reminders.addReminder(r4)
    assert reminders.getReminders() == [r1, r2, r3, r4]

def test_remove_reminder():
    r1: Reminder = Reminder("Clean room", ["clean", "room"], "I need to clean my room.")
    r2: Reminder = Reminder("Wash dishes", ["wash", "dishes"], "I need to wash the dishes.")
    r3: Reminder = Reminder("Mop floor", ["mop", "floor"], "I need to mop the floor.")

    reminders: Reminders = Reminders([r1, r2, r3])
    
    reminders.removeReminder(r1)
    assert reminders.getReminders() == [r2, r3]


def test_remove_reminder_by_title():
    r1: Reminder = Reminder("Clean room", ["clean", "room"], "I need to clean my room.")
    r2: Reminder = Reminder("Wash dishes", ["wash", "dishes"], "I need to wash the dishes.")
    r3: Reminder = Reminder("Mop floor", ["mop", "floor"], "I need to mop the floor.")

    reminders: Reminders = Reminders([r1, r2, r3])
    
    reminders.removeReminderByTitle("Wash dishes")
    assert reminders.getReminders() == [r1, r3]