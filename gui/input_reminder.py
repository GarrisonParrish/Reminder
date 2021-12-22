"""Input reminder application window."""

import tkinter as tk
from tkinter import StringVar
from main.reminder import Reminder
import re  # Note: regex might be overkill for this purpose
from main.read_write import write_reminder



class InputReminder(tk.Tk):
    """Separate window to input reminder."""
    def __init__(self):
        # Initialize superclass
        super().__init__()
        ###############################################################
        self.title("Reminder App")

        self.header = tk.Label(text="Reminder")  # header label
        # Add to the window and size window as small as possible to match label
        self.header.pack()

        # Label for title entry
        self.title_label = tk.Label(text="Enter title")
        self.title_label.pack()
        # Entry for title
        self.title = StringVar()
        self.title_entry = tk.Entry(self, textvariable=self.title)
        self.title_entry.pack()

        # Label for metadata tag entry
        self.metadata_label = tk.Label(text="Enter comma-separated metadata tags")
        self.metadata_label.pack()
        # Entry for meta tag
        self.metadata = StringVar()
        self.metadata_entry = tk.Entry(self, textvariable=self.metadata)
        self.metadata_entry.pack()

        # Label for notes entry
        self.notes_label = tk.Label(text="Enter notes")
        self.notes_label.pack()
        # Entry for notes
        self.notes = StringVar()
        self.notes_entry = tk.Entry(self, textvariable=self.notes)
        self.notes_entry.pack()

        # Button for submitting reminder
        # TODO: 
        # Get title, metadata, and notes, put in Reminder
        # Write reminder to json file
        # clear entry fields
        self.submit_button = tk.Button(self, text="Submit Reminder", default="active", command=self.submit_reminder)
        self.submit_button.pack()

    def validate(self, input: StringVar):
        if input == "":
            return False
        else:
            return True


    def submit_reminder(self):
        if not self.validate(self.title.get()):
            return
        # Note: metadata is comma-separated, turn into list
        metadata_list: list[str] = re.split(",|, ", self.metadata.get())
        # Create a Reminder object containing form data
        r: Reminder = Reminder(self.title.get(), metadata_list, self.notes.get())
        # Clear entries
        self.title.set("")
        self.metadata.set("")
        self.notes.set("")
        # Write the reminder to a json file
        write_reminder(r)