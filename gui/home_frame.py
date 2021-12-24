"""Frame for homepage."""

import tkinter as tk
from tkinter import StringVar
from tkinter.constants import LEFT
from main.read_write import read_filenames

class HomeFrame(tk.Frame):
    """View reminders and sort."""
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.options = read_filenames("data")
        self.clicked = StringVar()
        self.clicked.set(self.options[0])

        # Frame for sort menu
        self.sort_frame = tk.Frame(self, pady=10, padx=10)
        # Dropdown menu
        self.sort_frame.dropdown = tk.OptionMenu(self.sort_frame, self.clicked, *self.options)
        self.sort_frame.dropdown.pack(side=LEFT)
        # Button to add a category
        self.sort_frame.button = tk.Button(self.sort_frame, text="Update label", command=self.add_category)
        self.sort_frame.button.pack(side=LEFT)
        # Entry to specify new category
        self.new_category = StringVar()
        self.sort_frame.new_category_entry = tk.Entry(self.sort_frame, textvariable=self.new_category)
        self.sort_frame.new_category_entry.pack(side=LEFT)

        self.sort_frame.pack()

        self.label = tk.Label(self, text="Hello")
        self.label.pack()

        # Frame for buttons
        self.button_frame = tk.Frame(self, pady=10)
        # New reminder button
        self.button_frame.new_button = tk.Button(
            self.button_frame,
            text="New",
            command=self.new_reminder,
            padx=15
        )
        self.button_frame.new_button.pack(side=LEFT)
        # Exit app button
        self.button_frame.exit_button = tk.Button(
            self.button_frame,
            text="Exit",
            command=self.exit,
            padx=15
        )
        self.button_frame.exit_button.pack(side=LEFT)
        self.button_frame.pack()
    
    def add_category(self):
        """Add a category to the dropdown menu."""
        self.options.append(self.new_category.get())
    
    def new_reminder(self):
        """Switch to input reminder frame."""
        from gui.input_reminder_frame import InputReminderFrame
        self.master.switch_frame(InputReminderFrame)
    
    def exit(self):
        """Return to start frame"""
        from gui.start_frame import StartFrame
        self.master.switch_frame(StartFrame)