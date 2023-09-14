import json
import os.path
from datetime import datetime

def create_note():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M%S')
    note_id = len(notes) + 1
    note_title = input("Title: ")
    note_body = input("Body: ")

    note = {
        "id": note_id,
        "title": note_title,
        "body": note_body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes()
    print("The note has been created!")

def read_notes():
    for note in notes:
        print(f"ID: {note['id']} Заголовок: {note['title']} Текст: {note['body']} Дата\Время: {note['timestamp']}")

def edit_notes():
    note_id = int(input("ID for edit "))

    for note in notes:
        if note["id"] == note_id:
            title = input("Input new note's title ")
            body = input("Input new note's text ")
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            note["title"] = title
            note["body"] = body
            note["timestamp"] = timestamp
            save_notes()
            print("The note has been successfully edited!")
            return

    print("The note wasn't found!")

def delete_note():
    note_id = int(input("Select note ID for deletion "))
    note_index = -1

    for index, note in enumerate(notes):
        if note['id'] == note_id:
            note_index = index
            break
    if note_index != -1:
        del notes[note_index]
        save_notes()
        print("Note has been deleted")
    else:
        print("No found note")

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes.extend(json.load(file))

def main():
    while True:
        print("1. Add Note")
        print("2. Edit Note")
        print("3. Delete Note")
        print("4. Show Notes")
        print("5. Exit")

        choice = input("Select the option ")

        if choice == "1":
            create_note()
        elif choice == "2":
            edit_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            read_notes()
        elif choice == "5":
            break
        else:
            print("Incorrect input. Try again")

notes = []
load_notes()

main()