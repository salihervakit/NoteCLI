from project import addNote, selectChoice, getNotes, removeNewline
import datetime

def openFile():
    try:
        f = open("test_notes.txt", "w+", encoding="UTF-8")
        return f
    except IOError as e:
        print(f"Error opening file: {e}")
    

def test_getNotes():
    f = openFile()
    addNote(f, "test")
    assert getNotes(f) == [[f'\x1b[96m1. test, {getDate()}\x1b[0m']]
    addNote(f, "asdasd")
    assert getNotes(f) == [[f'\x1b[96m1. test, {getDate()}\x1b[0m'], [f'\x1b[96m2. asdasd, {getDate()}\x1b[0m']]

def test_selectChoice():
    assert selectChoice(1, None) == "\033[93mInvalid choice. Please enter a number between 1 and 7.\033[0m"
    assert selectChoice("8", None) == "\033[93mInvalid choice. Please enter a number between 1 and 7.\033[0m"

def test_removeNewline():
    assert removeNewline([" test", "test 2 "]) == ["test", "test 2"]

def getDate():
    date = datetime.datetime.now()
    date = f"{date.strftime('%x')} {date.strftime('%H:%M')}"
    return date