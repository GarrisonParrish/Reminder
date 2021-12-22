"""Application window for viewing reminders."""

import tkinter as tk

def new_window():
    w = tk.Toplevel()
    title_label = tk.Label(w, text="Reminders")
    title_label.pack()

HEIGHT = 300
WIDTH = 500

ws = tk.Tk()
ws.title("Reminder App")

button = tk.Button(ws, text="New window", command=new_window)

button.pack()

ws.mainloop()