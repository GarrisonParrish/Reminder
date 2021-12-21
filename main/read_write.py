"""Methods for converting Reminder to JSON, reading to and writing from disk."""

import json
from reminder import *

def main() -> None:
    # r: Reminder = Reminder("Fold laundry", ["fold", "laundry"], "I need to fold the laundry.")
    # write_reminder(r)
    # print("Done!")
    returned_data: dict = read_json('data/Fold laundry.json')
    print(returned_data)


def write_reminder(r: Reminder):
    """Convert Reminder to dictionary and write to JSON file."""
    data = {}  # dictionary that will be written to a JSON file

    data["title"] = r.getTitle()
    data["metadata"] = r.getMetadata()
    data["notes"] = r.getNotes()

    write_dict_to_json(data)


def write_dict_to_json(reminder_dict: dict) -> None:
    """Writes reminder input to a JSON file."""
    # Title for JSON file
    file_title: str = ""
    if reminder_dict["title"] != "":
        file_title = reminder_dict["title"]  # title of reminder
    elif len(reminder_dict["metadata"]) > 0:
        file_title = reminder_dict["metadata"][0]  # first meta tag
    else:
        file_title = "NO_TITLE"
    # write to an indent-formatted JSON file
    with open(f'data/{file_title}.json', "w") as outfile:
        json.dump(reminder_dict, outfile, indent=4)
    outfile.close()


def read_json(filepath: str) -> dict:
    """Given a valid path to a JSON file, reads that file into a dictionary."""
    openfile = open(filepath, "r")
    result: dict = json.load(openfile)
    openfile.close()
    return result


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


if __name__ == "__main__":
    main()