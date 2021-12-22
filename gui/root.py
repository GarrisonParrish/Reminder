"""Root application window."""

import tkinter as tk
from gui.input_reminder import InputReminder

# Run with 'python -m gui.root'

class App(tk.Tk):
    """Inherits from tk.Tk class."""
    def __init__(self):
        # Initialize superclass
        super().__init__()
        # Root window dimensions
        self.title("Reminder App")
        self.geometry("300x100")

        # label
        self.label = tk.Label(self, text="Input reminder")
        # Button
        self.button = tk.Button(self, text="Input a reminder!", command=self.input_reminder)
        # Pack elements
        self.label.pack()
        self.button.pack()
    
    def input_reminder(self):
        self.child_window = InputReminder()


if __name__ == "__main__":
    app = App()
    app.mainloop()