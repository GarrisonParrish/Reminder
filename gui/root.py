"""Root application window."""

import tkinter as tk
from gui.input_reminder import InputReminder

# Run with 'python -m gui.root'

class App(tk.Frame):
    """Inherits from tk.Frame"""
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.geometry("300x100")

        # label
        self.label = tk.Label(self.frame, text="Input reminder")
        # Button
        self.button = tk.Button(self.frame, text="Input a reminder!", command=self.input_reminder)
        # Pack elements
        self.label.pack()
        self.button.pack()
        self.frame.pack()
    
    def input_reminder(self):
        self.child_window = InputReminder()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Reminder App")
    app = App(root)
    root.mainloop()