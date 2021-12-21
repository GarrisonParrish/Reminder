"""Reminder class and Reminders container class."""


class Reminder:
    """Reminder with title, metadata tag list, and notes."""
    def __init__(self, title: str, metadata: list[str], notes: str):
        self.title = title
        self.metadata = metadata
        self.notes = notes

    def getTitle(self):
        """Get reminder title string."""
        return self.title

    def getMetadata(self):
        """Get reminder metadata list."""
        return self.metadata

    def getNotes(self):
        """Get reminder notes string."""
        return self.notes
    
    def setTitle(self, title: str):
        """Set reminder title."""
        self.title = title
    
    def setMetadata(self, metadata: list[str]):
        """Set reminder metadata list."""
        self.metadata = metadata
    
    def appendMetaTag(self, tag: str):
        """Append meta tag to end of list."""
        self.metadata.append(tag)
    
    def popMetaTag(self):
        """Pop meta tag from end of list."""
        self.metadata.pop()
    
    def popMetaTagAtIndex(self, index: int):
        """Remove meta tag at index."""
        self.metadata.pop(index)

    def replaceMetaTagAtIndex(self, index: int, tag: str):
        """Replace metadata tag string at index in metadata list."""
        self.metadata[index] = tag
    
    def replaceMetaTagByName(self, oldTag: str, newTag: str):
        """Replace old meta tag with new meta tag by name. All duplicates are replaced."""
        for i in range(0, len(self.metadata)):
            if self.metadata[i] == oldTag:
                self.replaceMetaTagAtIndex(i, newTag)

    def setNotes(self, notes: str):
        """Set reminder notes string."""
        self.notes = notes


class Reminders:
    """List of reminders."""
    def __init__(self, reminder_list: list[Reminder]):
        self.reminder_list = reminder_list

    def getReminders(self):
        """Get all reminders in the list."""
        return self.reminder_list

    def getReminderByIndex(self, index: int):
        """Get reminder by index."""
        return self.reminder_list[index]

    def getReminderByTitle(self, title: str):
        """Return first reminder with matching title."""
        for r in self.reminder_list:
            if r.getTitle() == title:
                return r
        # if reminder not found, raise exception
        raise Exception
    
    def getRemindersByMetaTag(self, tag: str):
        """Return list of reminder with metatag."""
        results_list: list[Reminder] = []
        for r in self.reminder_list:
            if tag in r.getMetadata():
                results_list.append(r)
        return results_list
    
    def addReminder(self, r: Reminder):
        """Append reminder to reminder list."""
        self.reminder_list.append(r)
    

    def removeReminder(self, r: Reminder):
        """Remove reminder by reference. All duplicates are removed."""
        filtered_reminders = list(filter(lambda x: r != x, self.reminder_list))
        self.reminder_list = filtered_reminders
    
    def removeReminderByTitle(self, title: str):
        """Remove reminder by reference. All duplicates are removed."""
        filtered_reminders = list(filter(lambda x: title != x.getTitle(), self.reminder_list))
        self.reminder_list = filtered_reminders