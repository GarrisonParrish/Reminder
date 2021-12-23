"""Root application window."""

import tkinter as tk
from gui.input_reminder import InputReminder

# Run with 'python -m gui.root'

class MainApp(tk.Frame):
    """Inherits from tk.Frame"""
    def __init__(self, master):
        tk.Frame.__init__(self, master) # self is a frame, parent is master
        
    
    def input_reminder(self):
        self.child_window = InputReminder()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Reminder App")
    MainApp(root).pack()
    root.mainloop()