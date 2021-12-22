"""Application window for inputting a reminder."""

import tkinter as tk
from tkinter import StringVar
from reminder import Reminder
import re  # Note: regex might be overkill for this purpose
from read_write import write_reminder

root = tk.Tk()  # GUI window
root.title("Reminder App")

header = tk.Label(text="Reminder")  # header label
# Add to the window and size window as small as possible to match label
header.pack()

# Label for title entry
title_label = tk.Label(text="Enter title")
title_label.pack()
# Entry for title
title = StringVar()
title_entry = tk.Entry(root, textvariable=title)
# Listen for changes to title variable
def title_has_changed():
    print("Title changed")
    title.trace_add("write", title_has_changed)

title_entry.pack()

# Label for metadata tag entry
metadata_label = tk.Label(text="Enter comma-separated metadata tags")
metadata_label.pack()
# Entry for meta tag
metadata = StringVar()
metadata_entry = tk.Entry(root, textvariable=metadata)
# Listen for changes to meta_tag variable
def metadata_has_changed():
    print("Meta changed")
    metadata.trace_add("write", metadata_has_changed)

metadata_entry.pack()

# Label for notes entry
notes_label = tk.Label(text="Enter notes")
notes_label.pack()
# Entry for notes
notes = StringVar()
notes_entry = tk.Entry(root, textvariable=notes)
# Listen for changes to notes variable
def notes_has_changed():
    print("Notes changed")
    notes.trace_add("write", notes_has_changed)
notes_entry.pack()

# Button for submitting reminder
# TODO: 
# Get title, metadata, and notes, put in Reminder
# Write reminder to json file
# clear entry fields

def validate(input: StringVar):
    if input == "":
        return False
    else:
        return True


def submit_reminder():
    if not validate(title.get()):
        return
    # Note: metadata is comma-separated, turn into list
    metadata_list: list[str] = re.split(",|, ", metadata.get())
    # Create a Reminder object containing form data
    r: Reminder = Reminder(title.get(), metadata_list, notes.get())
    # Clear entries
    title.set("")
    metadata.set("")
    notes.set("")
    # Write the reminder to a json file
    write_reminder(r)
    

submit_button = tk.Button(root, text="Submit Reminder", default="active", command=submit_reminder)
submit_button.pack()

root.mainloop()  # Run the GUI loop