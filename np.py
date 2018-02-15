#!/bin/python

import notes

def main():
    print("Hello, there!")
    choice = input("\n\n1) Add note\n2) Edit note\n3) Delete note\n\nWhat ya like to do?\n> ")

    n = notes.Notes
    if choice == "1":
        # Get all the data
        title = input("Title: ")
        note = input("Note:\n> ")
        while note != "":
            note = input("> ")
        n_time = input("Notification time [d:m:y] ")
        if n_time == "":
            n_time = None

        n.add_note(title, note, n_time)
    elif choice == "2":
        n.edit_note()
    elif choice == "3":
        n.delete_note()

if __name__ == "__main__":
    main()

