import tkinter as tk


class Frame1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, text="Hello")
        self.label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    frame1 = Frame1(root)
    frame1.pack()
    root.mainloop()