"""Frame for homepage."""

import tkinter as tk
from tkinter import StringVar
from tkinter.constants import LEFT
from main.constants import EXCLUDE_SUFFIX, SELECT_REMINDER_PROMPT
from main.read_write import read_filenames

class HomeFrame(tk.Frame):
    """View reminders and sort."""
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.options = read_filenames("data", EXCLUDE_SUFFIX)
        self.clicked = StringVar()
        self.clicked.set(SELECT_REMINDER_PROMPT)

        # Frame for sort menu
        self.sort_frame = tk.Frame(self, pady=10, padx=10)
        # Dropdown menu
        self.sort_frame.dropdown = tk.OptionMenu(self.sort_frame, self.clicked, *self.options)
        self.sort_frame.dropdown.pack(side=LEFT)
        # Button to open reminder
        self.sort_frame.button = tk.Button(self.sort_frame, text="Open", command=self.open_reminder)
        self.sort_frame.button.pack(side=LEFT)
        self.sort_frame.pack()

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
        # Exit app button
        self.nav_button_frame.exit_button = tk.Button(
            self.nav_button_frame,
            text="Exit",
            command=self.exit,
            padx=15
        )
        self.nav_button_frame.exit_button.pack(side=LEFT)
        self.nav_button_frame.pack()

    
    def open_reminder(self):
        """Open the currently selected reminder from the dropdown menu."""
        # Create a frame to view content of selected reminder
        if self.clicked.get() == SELECT_REMINDER_PROMPT:
            return
        else:
            from gui.open_reminder_frame import OpenReminderFrame
            self.master.switch_frame(OpenReminderFrame, self.clicked.get())
    
    def new_reminder(self):
        """Switch to input reminder frame."""
        from gui.input_reminder_frame import InputReminderFrame
        self.master.switch_frame(InputReminderFrame)
    
    def exit(self):
        """Return to start frame"""
        from gui.start_frame import StartFrame
        self.master.switch_frame(StartFrame)