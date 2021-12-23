"""Root application window."""

import tkinter as tk
from tkinter.constants import NW
from main.constants import APP_TITLE, FEELS_GOOD_PATH
from PIL import Image, ImageTk

# Run with 'python -m gui.root'

class StartFrame(tk.Frame):
    """Inherits from tk.Frame"""
    def __init__(self, master):
        tk.Frame.__init__(self, master) # self is a frame, parent is master
        self.label = tk.Label(
            self,
            text=APP_TITLE,
            font=("Helvetica", 40)
        )
        self.label.pack(padx=60, pady=40)

        self.canvas = tk.Canvas(self, width= 400, height= 300)
        self.canvas.pack()

        self.image = Image.open(FEELS_GOOD_PATH)
        self.resized_image = self.image.resize((400, 293), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)

        self.canvas.create_image(10, 10, anchor=NW, image=self.new_image)
        
        self.open_button = tk.Button(self, text="New", command=self.open)
        self.open_button.pack()
        self.exit_button = tk.Button(self, text="Exit", command=self.exit)
        self.exit_button.pack()
    
    def open(self):
        """Open the application (go to home page window)"""
        print("Opened!")
        # TODO: implement (destroy current frame, build the home page frame inside the root window)
        from gui.input_reminder import InputReminder
        self.master.switch_frame(InputReminder)
    
    def  exit(self):
        """Exit the application"""
        self.master.destroy()
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Reminder App")
    StartFrame(root).pack()
    root.mainloop()