import tkinter as tk
from tkinter import StringVar

window = tk.Tk()  # GUI window

header = tk.Label(text="Reminder")  # header label
# Add to the window and size window as small as possible to match label
header.pack()

# Label for title entry
title_label = tk.Label(text="Enter title")
title_label.pack()
# Entry for title
title = StringVar()
title_entry = tk.Entry(window, textvariable=title)
# Listen for changes to title variable
def title_has_changed():
    print("Title changed")
    title.trace_add("write", title_has_changed)

title_entry.pack()

# Label for metadata tag entry
metadata_label = tk.Label(text="Enter meta tag")
metadata_label.pack()
# Entry for meta tag
metadata = StringVar()
metadata_entry = tk.Entry(window, textvariable=metadata)
# Listen for changes to meta_tag variable
def metadata_has_changed():
    print("Meta changed")
    metadata.trace_add("write", metadata_has_changed)

metadata_entry.pack()

# Label for notes entry
notes_label = tk.Label(text="Enter notes")
notes_label.pack()
# Entry for notes
notes = StringVar()
notes_entry = tk.Entry(window, textvariable=notes)
# Listen for changes to notes variable
def notes_has_changed():
    print("Notes changed")
    notes.trace_add("write", notes_has_changed)
notes_entry.pack()

window.mainloop()  # Run the GUI loop