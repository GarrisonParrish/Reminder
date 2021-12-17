"""Main application."""

import json
import time  # time... goes on...
import pync  # allows program to send user notifications to Mac OS operating system

def main() -> None:
    data: dict = input_reminder()
    write_input(data)
    print(data)
    
    # test with file 'hello_world.json'
    returned_data: dict = read_input('/Users/garrisonparrish/Python Applications/reminder-app/data/hello_world.json')




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


def write_input(reminder_dict: dict) -> None:
    """Writes reminder input to a JSON file."""
    file_title: str = "title"
    if reminder_dict["title"] != "":
        file_title = reminder_dict["title"]  # title of reminder
    elif reminder_dict["metadata"] != []:
        file_title = reminder_dict["metadata"][0]  # first meta tag
    else:
        file_title = "NO_TITLE"

    with open(f'/Users/garrisonparrish/Python Applications/reminder-app/data/{file_title}.json', "w") as outfile:
        # write to an indent-formatted JSON file with a custom titles
        json.dump(reminder_dict, outfile, indent=4)
    outfile.close()


def read_input(filepath: str) -> dict:
    """Given a valid path to a JSON file, reads that file into a dictionary."""
    openfile = open(filepath, "r")
    result: dict = json.load(openfile)
    openfile.close()
    return result


if __name__ == "__main__":
    main()