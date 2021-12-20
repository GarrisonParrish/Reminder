"""Test the Reminder class."""

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


def test_set_metadata():
    r: Reminder = Reminder("Take out trash", [], "Go take out the trash.")
    meta_list = ["trash", "outside"]
    r.setMetadata(meta_list)
    assert r.getMetadata() == ["trash", "outside"]

def test_set_notes():
    r: Reminder = Reminder("Take out trash", [], "Go take out the trash.")
    r.setNotes("Take the trash outside.")
    assert r.getNotes() == "Take the trash outside."

def test_append_metatag():
    r: Reminder = Reminder("Take out trash", ["trash", "outside"], "Go take out the trash.")
    r.appendMetaTag("garbage")
    assert r.getMetadata() == ["trash", "outside", "garbage"]

def test_pop_metatag():
    r: Reminder = Reminder("Take out trash", ["trash", "outside", "garbage"], "Go take out the trash.")
    r.popMetaTag()
    assert r.getMetadata() == ["trash", "outside"]

def test_pop_meta_tag_at_index():
    r: Reminder = Reminder("Take out trash", ["trash", "outside", "garbage"], "Go take out the trash.")
    r.popMetaTagAtIndex(1)
    assert r.getMetadata() == ["trash", "garbage"]

def test_replace_meta_tag_at_index():
    r: Reminder = Reminder("Take out trash", ["trash", "outside", "garbage"], "Go take out the trash.")
    r.replaceMetaTagAtIndex(1, "out")
    assert r.getMetadata() == ["trash", "out", "garbage"]

def test_replace_meta_tag_by_name_01():
    r: Reminder = Reminder("", ["trash", "outside", "garbage"], "")
    r.replaceMetaTagByName("outside", "out")
    assert r.getMetadata() == ["trash", "out", "garbage"]

def test_replace_meta_tag_by_name_02():
    r: Reminder = Reminder("", ["trash", "trash", "out"], "")
    r.replaceMetaTagByName("trash", "garbage")
    assert r.getMetadata() == ["garbage", "garbage", "out"]