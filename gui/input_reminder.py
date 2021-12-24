"""Input reminder application window."""

import tkinter as tk
from tkinter import StringVar
from main.reminder import Reminder
import re  # Note: regex might be overkill for this purpose
from main.read_write import write_reminder

# NOTE: must always specify parent for each Tkinter class

class InputReminder(tk.Frame):
    def __init__(self, master):
        """Create window to input reminder."""
        tk.Frame.__init__(self, master)
        # NOTE: Always include self as parent
        self.header = tk.Label(self, text="Reminder")  # header label
        # Add to the window and size window as small as possible to match label
        self.header.pack()

        # Label for title entry
        self.title_label = tk.Label(self, text="Enter title")
        self.title_label.pack()
        # Entry for title
        self.title = StringVar(self)
        self.title_entry = tk.Entry(self, textvariable=self.title)
        self.title_entry.pack()

        # Label for metadata tag entry
        self.metadata_label = tk.Label(self, text="Enter comma-separated metadata tags")
        self.metadata_label.pack()
        # Entry for meta tag
        self.metadata = StringVar(self)
        self.metadata_entry = tk.Entry(self, textvariable=self.metadata)
        self.metadata_entry.pack()

        # Label for notes entry
        self.notes_label = tk.Label(self, text="Enter notes")
        self.notes_label.pack()
        # Textbox for notes
        self.notes_textbox = tk.Text(self, height=10, width=50, wrap="word")
        self.notes_textbox.pack()
        # Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_reminder)
        self.submit_button.pack() 
        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.exit)
        self.exit_button.pack()

    def validate(self, input):
        """Validate entry for null input."""
        if input == "":
            return False
        else:
            return True

    def submit_reminder(self):
        """Submit entry data to a reminder and write to disk."""
        if not self.validate(self.title.get()):
            return
        # Note: metadata is comma-separated, turn into list
        metadata_list: list[str] = re.split(",|, ", self.metadata.get())
        # Create a Reminder object containing form data
        r: Reminder = Reminder(self.title.get(), metadata_list, self.notes_textbox.get('1.0', 'end'))
        # Clear entries
        self.title.set("")
        self.metadata.set("")
        self.notes_textbox.delete('1.0', 'end')
        # Write the reminder to a json file
        write_reminder(r)
        self.exit()
    
    def exit(self):
        """Destroy the current window."""
        from gui.start_frame import StartFrame
        self.master.switch_frame(StartFrame)