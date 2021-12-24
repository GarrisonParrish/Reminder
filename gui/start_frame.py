"""Root application window."""

import tkinter as tk
from tkinter.constants import LEFT, NW
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
        
        # Frame for buttons
        self.button_frame = tk.Frame(self, pady=10)
        # Open app button
        self.button_frame.open_button = tk.Button(
            self.button_frame,
            text="Open",
            command=self.open,
            padx=15
        )
        self.button_frame.open_button.pack(side=LEFT)
        # Exit app button
        self.button_frame.exit_button = tk.Button(
            self.button_frame,
            text="Exit",
            command=self.exit,
            padx=15
        )
        self.button_frame.exit_button.pack(side=LEFT)
        self.button_frame.pack()
    
    def open(self):
        """Open the application (go to home page window)"""
        #from gui.input_reminder import InputReminder
        #self.master.switch_frame(InputReminder)
        from gui.home_frame import HomeFrame
        self.master.switch_frame(HomeFrame)
    
    def  exit(self):
        """Exit the application"""
        self.master.destroy()