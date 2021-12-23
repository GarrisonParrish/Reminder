"""Main window for application."""

import tkinter as tk
from gui.start_frame import StartFrame

# Run with 'python -m gui.main_app'

class MainApp(tk.Tk):
    """Main application window. Inherits from tk.Tk."""
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = None
        self.switch_frame(StartFrame)
    
    def switch_frame(self, frame_class):
        """Switch current frame in application window."""
        # Call class constructor, giving self as parent/master
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        # pack new frame
        self.frame = new_frame
        self.frame.pack()


if __name__ == "__main__":
    root = MainApp()
    root.title("Reminder App")
    root.mainloop()