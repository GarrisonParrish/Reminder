"""Frame for opening a reminder """

import tkinter as tk

class OpenReminderFrame(tk.Frame):
    """Display a reminder that is read from disk."""
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        