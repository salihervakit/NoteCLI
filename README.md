# NoteCLI Installation and Usage Guide

## Installation
To install and set up NoteCLI, follow these steps:

1. **Clone the Repository**:
    ```bash 
    git clone https://github.com/salihervakit/notecli.git
    cd notecli
    ```

2. **Create a Virtual Environment (Optional but Recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Libraries**:
    The required libraries will be automatically installed when you run the script. However, you can manually install them by running:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:
    ```bash
    python project.py
    ```


#### Video Demo: <https://youtu.be/3HEzbaJp0j8>
#### Description: NoteCLI is an app based on Python. NoteCLI enables you to take notes, update and delete them. The project uses only 1 3rd party library called **terminaltables**.

We use **terminaltables** for showing notes to the user in a table format instead of plain text for styling purposes. Which makes it easier to read. We also import 2 additional Python libraries, **datetime** and **os**. Datetime is for storing when the note is created, and the **os** is for the *secret* choice.

In our main function after printing "welcome", we try to open (or create if the file doesn't exist) a file. If the operation is successful, we show all the possible options for the user to select. Then program enters an infinite while loop, Asking the user to enter a number between 1-7. It passes this input to the *selectChoice* function and calls the appropriate function based on this input. The *selectChoice* function doesn't return any value for input between 1-7 but returns a string for any other numbers other than between 1 and 7. If the user types 7 the program closes the file and uses *exit()*. In the main, we check if *selectChoice* returned any value, and print it if it returned anything.

"*addNote*" function checks if the user entered an empty string, and returns if so. Then gets the current day/month/year hour/minute. It tries to write the note the user entered and the current date the note was created to the notes.txt. We use file.flush and os.fsync, so it doesn't wait for the program to end, which makes the writing to file immediate.

"*getNotes*" first uses file.seek(0) to avoid any unexpected behaviors. Gets the notes with file.readlines, if there is no note prints a string to the user and returns. If there are notes, then it creates an empty array. We add all those notes with their index and style them with colors in a formatted way to that array, then return it.

"*updateNote*" first uses file.seek(0) to avoid any unexpected behaviors. Gets the notes and saves in a variable. Checks if there is no note and returns if so. If there are notes, then we show the notes with their indexes and prompt the user to write the index to get which note to be updated. If the input is not a number it prints "enter a number" and returns. Now it is confirmed the input is a number, we typecast the input to int. And check if the input is between 1-numberOfNotes, if not it prints to enter a number between 1 and numberOfNotes and returns. Then we want a string from the user to update the selected note, if the user entered an empty string we print "enter a valid note" and return. If it is a valid string, we ask for confirmation if the user wants to update the note, if the user types "y" or "yes", we update it accordingly.

"*deleteNote*" first uses file.seek(0) to avoid any unexpected behaviors. Gets the notes and saves in a variable. Checks if there is no note and returns if so. If there are notes, then we show the notes with their indexes and prompt if the user wants to delete all the notes, they can do it by typing "0". Or if they just want to delete a specific note, they can write the index of the note to delete it. If the input is not a number it prints "enter a number" and returns. Now it is confirmed the input is a number, we typecast the input to int. And check if the input is between 0-numberOfNotes, if not, it prints to enter a number between 0 and numberOfNotes and returns. If the user typed 0, we ask with red letters to avoid any undesired actions, with this confirmation all notes will be deleted. Then user can type "y" or "yes" to confirm. But if the user entered any index other than 0, we show the selected note to the user to be deleted and ask for confirmation if the user wants to delete the note. If the user types "y" or "yes", we delete the specified note.

"*secret*" uses **os** library to use cmd. In cmd, we use *curl parrot.live* command to show a dancing parrot.

"*removeNewLine*" as the name stated, removes the "\n" that every array element has at the end.

"*printTable*" is for showing the notes formatted in a table for styling purposes. It uses **terminaltables** library.

"*showOptions*" shows the user the options that can be selected like adding notes, or updating notes.