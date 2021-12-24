"""Methods for converting Reminder to JSON, reading to and writing from disk."""

# TODO: Once UX has been finalized, refactor code to eliminate redundant methods

import json
from main.constants import REMINDER_FILETYPE
from main.reminder import Reminder
from os import listdir

def main() -> None:
    # r: Reminder = Reminder("Fold laundry", ["fold", "laundry"], "I need to fold the laundry.")
    # write_reminder(r)
    # print("Done!")
    print(read_filenames("data"))


def write_reminder(r: Reminder):
    """Convert Reminder to dictionary and write to JSON file."""
    data = {}  # dictionary that will be written to a JSON file

    data["title"] = r.getTitle()
    data["metadata"] = r.getMetadata()
    data["notes"] = r.getNotes()

    write_dict_to_json(data)


def write_dict_to_json(data: dict) -> None:
    """Writes reminder input to a JSON file."""
    # Title for JSON file
    file_title: str = ""
    if data["title"] != "":
        file_title = data["title"]  # title of reminder
    elif len(data["metadata"]) > 0:
        file_title = data["metadata"][0]  # first meta tag
    else:
        file_title = "NO_TITLE"
    # write to an indent-formatted JSON file
    with open(f'data/{file_title}.json', "w") as outfile:
        json.dump(data, outfile, indent=4)
    outfile.close()


def read_to_reminder(filepath: str) -> Reminder:
    """Given a filepath to a JSON file, returns a Reminder with file data."""
    result: dict = read_json(filepath)
    return dict_to_reminder(result)


def read_json(filepath: str) -> dict:
    """Given a valid path to a JSON file, reads that file into a dictionary."""
    openfile = open(filepath, "r")
    result: dict = json.load(openfile)
    openfile.close()
    return result


def dict_to_reminder(data: dict) -> Reminder:
    """Converts a dictionary to a Reminder object."""
    return Reminder(data["title"], data["metadata"], data["notes"])


def input_reminder() -> dict:
    """Prompt user for input and returns input as a dictionary."""
    data = {}  # dictionary that will be written to a JSON file
    input_name: str = input("Title for this reminder: ")
    input_metadata: list[str] = []

    do_input_metadata: bool = True
    while do_input_metadata:
        input_meta_tag: str = input("Input meta tag: ")
        if input_meta_tag == "":
            # terminate loop if STOP was entered
            do_input_metadata = False
        else:
            input_metadata.append(input_meta_tag)
    input_notes: str = input("Notes for this reminder: ")

    data["title"] = input_name
    data["metadata"] = input_metadata
    data["notes"] = input_notes

    return data

def read_filenames(directory_path: str):
    """Given a path to a directory, returns a list of all filenames in the directory."""
    entries_list = listdir(directory_path)
    return_list: list[str] = []
    for item in entries_list:
        if REMINDER_FILETYPE in item:
            # item is a .json file
            filename: str = item.removesuffix(REMINDER_FILETYPE)
            return_list.append(filename)
    return return_list

if __name__ == "__main__":
    main()