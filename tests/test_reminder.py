import pytest
from main.reminder import *


def test_title():
    r: Reminder = Reminder("Take out trash", [], "Go take out the trash.")
    assert r.getTitle() == "Take out trash"


def test_metadata():
    r: Reminder = Reminder("Take out trash", [], "Go take out the trash.")
    assert r.getMetadata() == []


def test_notes():
    r: Reminder = Reminder("Take out trash", [], "Go take out the trash.")
    assert r.getNotes() == "Go take out the trash."


def test_set_title():
    r: Reminder = Reminder("Take out trash", [], "Go take out the trash.")
    r.setTitle("Clean the bathroom")
    assert r.getTitle() == "Clean the bathroom"