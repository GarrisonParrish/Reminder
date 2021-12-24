"""Frame for opening a reminder """

import tkinter as tk
from tkinter.constants import LEFT
from main.read_write import read_to_reminder
from main.reminder import Reminder

class OpenReminderFrame(tk.Frame):
    """Display the given reminder."""
    def __init__(self, master, reminder_name):
        tk.Frame.__init__(self, master)
        # Read .json file into Reminder object
        self.filepath = "data/" + reminder_name + ".json"
        self.reminder = read_to_reminder(self.filepath)
        # Title of reminder
        self.title_label = tk.Label(
            self,
            text=reminder_name,
            font=("Helvetica", 20)
        )
        self.title_label.pack()
        # Metadata for reminder
        self.metadata_label = tk.Label(self, text=self.reminder.getMetadata())
        self.metadata_label.pack()
        # Notes for reminder
        self.notes_label = tk.Label(self, text=self.reminder.getNotes(), width=30, justify=LEFT)
        self.notes_label.pack()

        # Frame for nav buttons
        self.nav_button_frame = tk.Frame(self, pady=10)
        # New reminder button
        self.nav_button_frame.new_button = tk.Button(
            self.nav_button_frame,
            text="New",
            command=self.new_reminder,
            padx=15
        )
        self.nav_button_frame.new_button.pack(side=LEFT)
        # Back button
        self.nav_button_frame.back_button = tk.Button(
            self.nav_button_frame,
            text="Back",
            command=self.back,
            padx=15
        )
        self.nav_button_frame.back_button.pack(side=LEFT)
        self.nav_button_frame.pack()
    
    def new_reminder(self):
        """Switch to input reminder frame."""
        from gui.input_reminder_frame import InputReminderFrame
        self.master.switch_frame(InputReminderFrame)
    
    def back(self):
        """Go back to home frame."""
        from gui.home_frame import HomeFrame
        self.master.switch_frame(HomeFrame)