# Reminder app

A simple app to set reminders and create a todo list. 

## Format
Reminders have a title and metadata. User can add as many tags as they want to the metadata section.
Reminders have a notes section as a string.

format:

``
{   
    "title": "Dinner with Fake-chan",
    "metadata": [
        "imaginary", "not real", "dating",
    ],
    "notes": "I can't wait to have dinner with Fake-chan! She's so nice and sweet, I love spending time with her!"
}
``

### TODO:
- Search by keywords (title and metadata in any order)
- Set time to send a push notification to system
- Some way to measure time when computer is off (compare to system time?)
- Add support for notifications when time is reached ( use pync.notify() )
- GUI
- Once UX has been finalized, refactor code to eliminate redundant methods
- Add edit/delete reminder options

### Note: 
Added re library (regular expressions) so metadata entries can be separated with commas with or without a space following the comma. May be overkill and will likely slow down the program.

### Note: 
in its current state, the app takes entry data, creates a Reminder object with this data, and writes to a .json file. Writing to a .json file involves converting the Reminder data back into a dictionary and then writing that dictionary. Currently it would be easier simply to create a dict and use that, but the Reminder object will come in handy when more features (edit, delete, sort) are added.

### Note:
Currently the gui classes inherit from tk.Frame. Objects inheriting from Frame must be given a root/master, such as tk.Tk(). MainApp fulfills the role of tk.Tk, acting as the main application window and calling a method when the current frame needs to be switched. When a frame needs to be switched, it imports the Frame subclass that defines the new frame and calls its master, MainApp, to switch the frame. MainApp.switch_frame creates the new frame, destroys the old frame, and packs the new frame.

### Note: 
main/read_write.py is kind of a mess. Consider making it into a class to better follow the Model-View-Controller format.

### Note:
Editing the reminder uses InputReminderFrame, but the title, metadata, and notes are set to the values specified in the constructor call.