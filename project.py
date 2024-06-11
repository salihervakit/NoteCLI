import subprocess
import datetime
import sys
import os

def install_requirements():
    try:
        import terminaltables
    except ImportError:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

install_requirements()

from terminaltables import AsciiTable


def main():
    print("\033[1mWelcome\033[0m")

    try:
        f = open("notes.txt", "a+", encoding="UTF-8")
    except IOError as e:
        print(f"Error opening file: {e}")
        return

    showOptions()

    while True:
        choice = input("Choose an option (1-7): ")

        value = selectChoice(choice, f)
        
        if value:
            print(value)

        print("\033[4mSelect 6 for help.\033[0m")
  

def selectChoice(choice, f):
    match choice:
        case "1":
            note = input("Note to be added: ")
            addNote(f, note)
        case "2":
            printTable(getNotes(f))
        case "3":
            updateNote(f)
        case "4":
            deleteNote(f)
        case "5":
            secret()
        case "6":
            showOptions()
        case "7":
            f.close()
            exit(0)
        case _:
            return "\033[93mInvalid choice. Please enter a number between 1 and 7.\033[0m"


def addNote(f, note):
    date = datetime.datetime.now()
    date = f"{date.strftime('%x')} {date.strftime('%H:%M')}"

    if not note:
        print("\033[93mNote cannot be empty.\033[0m")
        return
    
    try:
        f.write(f"{note}, {date} \n")
        f.flush()
        os.fsync(f.fileno())
    except IOError as e:
        print(f"Error writing to file: {e}")

def getNotes(f):
    f.seek(0)
    notes = f.readlines()
    notesArr = []

    if not notes:
        print("There is no notes to show.")
        return

    for i, note in enumerate(notes, start=1):
        notesArr.append([f"\033[96m{i}. {note.strip()}\033[0m"])

    return notesArr


def updateNote(f):
    f.seek(0)
    notes = removeNewline(f.readlines())

    if not notes:
        print("There is no note to update.")
        return

    printTable(getNotes(f))

    noteIndex = input("Enter the number of the note to be updated: ")
    if not noteIndex.isnumeric():
        print("Please enter a number.")
        return

    noteIndex = int(noteIndex)

    if noteIndex < 1 or noteIndex > len(notes):
        print(f"\033[93mPlease enter a number between 1 and {len(notes)}.\033[0m")
        return

    selectedNote = notes[int(noteIndex)-1]
    selectedNote = selectedNote.split(", ")[0]

    updatedNote = input("Please enter the updated note: ")

    if not updatedNote:
        print("\033[93mNote cannot be empty.\033[0m")
        return

    answer = input((f"Are you sure you want to update the note \"{selectedNote}\" to \"{updatedNote}\" (y/n)\n")).lower()

    if answer == "y" or answer == "yes":
        date = notes[noteIndex-1].split(", ")[1]
        notes[noteIndex-1] = f"{updatedNote}, {date}"
        f.truncate(0)
        for note in notes:
            f.write(note + "\n")
            f.flush()
            os.fsync(f.fileno())

def deleteNote(f):
    f.seek(0)
    notes = removeNewline(f.readlines())

    if not notes:
        print("There is no note to delete.")
        return

    printTable(getNotes(f))
    print("If you want to delete \033[91mALL\033[0m the notes, type 0")

    noteIndex = input("Enter the number of the not to be deleted: ")
    if not noteIndex.isnumeric():
        print("Please enter a number.")
        return

    noteIndex = int(noteIndex)

    if noteIndex < 0 or noteIndex > len(notes):
        print(f"\033[93mPlease enter a number between 0 and {len(notes)}.\033[0m")
        return

    selectedNote = notes[int(noteIndex)-1]

    if noteIndex == 0:
        answer = input("This action will delete \033[91mALL THE NOTES\033[0m. Do you confirm? (y/n) ")
        if answer == "y" or answer == "yes":
            f.truncate(0)
            f.write("")
            f.flush()
            os.fsync(f.fileno())
        return

    answer = input((f"Are you sure you want to \033[91mdelete\033[0m the note \"{selectedNote}\" (y/n) ")).lower()

    if answer == "y" or answer == "yes":
        notes.remove(selectedNote)
        f.truncate(0)
        for note in notes:
            f.write(note + "\n")
            f.flush()
            os.fsync(f.fileno())

def secret():
    os.system("curl parrot.live")

def removeNewline(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].strip()
    return arr

def printTable(data):
    if not data:
        return
    
    table_data = data
    table = AsciiTable(table_data)

    table.inner_heading_row_border = False
    table.inner_row_border = True

    print(table.table)

def showOptions():
    options = [
        ["\033[94m1. Add note\033[0m"],
        ["\033[94m2. Show notes\033[0m"],
        ["\033[94m3. Update note\033[0m"],
        ["\033[94m4. Delete note\033[0m"],
        ["\033[95m5. Secret\033[0m"],
        ["\033[93m6. Help\033[0m"],
        ["\033[91m7. Exit\033[0m"],
    ]

    printTable(options)


if __name__ == "__main__":
    main()