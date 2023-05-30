# Log Viewer Readme

This code provides a simple log viewer application using the Tkinter library in Python. It allows you to load log files, view log entries, search for specific logs, and delete saved log entries.

## Prerequisites
- Python 3.x
- Tkinter library

## Usage
1. Make sure you have Python 3.x installed on your system.
2. Install the Tkinter library if it's not already installed.
3. Copy and paste the provided code into a Python file (e.g., `log_viewer.py`).
4. Run the Python file using a Python interpreter or an integrated development environment (IDE).

## Features

### Load Log File
- Click the "Load a log file" button to open a file dialog.
- Select a log file (in text format) to load into the application.
- The log file will be parsed and the log entries will be saved in the database.

### View Log Entries
- Click the "View log entries" button to open the log viewer window.
- The log viewer window will display all the log entries from the loaded log file.
- The log entries will be shown in a text widget with a scrollbar for navigation.

### Search Log Entries
- In the log viewer window, you can enter a search term in the search box.
- Click the "Search" button to search for log entries that contain the search term.
- The matching log entries will be displayed in the text widget.
- The search is case-insensitive and matches both the log entry keys and values.

### Delete Saved Log Entries
- Click the "Delete saved log entries" button to clear the entire log database.
- A confirmation dialog will appear to confirm the deletion.
- If confirmed, all the log entries in the database will be deleted.

### Quit
- Click the "Quit" button to exit the application.

## Database
- The log entries are stored in a JSON database file named `db.json`.
- If the `db.json` file does not exist, it will be created automatically.
- The log entries are loaded from the database file when the application starts.
- Changes to the log entries are saved back to the database file when necessary.

## Dependencies
- The code uses the following libraries from the Tkinter module:
  - `filedialog`: Provides file selection dialog.
  - `messagebox`: Displays message boxes for notifications.
  - `ttk`: Provides advanced widget styling.
  - `Entry`, `Frame`, `Label`, `Button`, `Text`: Various GUI elements.
- The code also utilizes the following built-in libraries:
  - `re`: For regular expression pattern matching.
  - `datetime`: For parsing timestamps in log entries.
  - `os`: For file operations and checking file existence.
  - `json`: For reading and writing log entries to the JSON database.

## Notes
- The code assumes that the log file follows a specific format.
- The log file is expected to have tab-separated values per line, containing the following fields:
  - Event Type, Timestamp, Source, Event ID, Category, Message.
- The log entries are parsed using regular expressions (`line_pattern` and `multi_line_pattern`).
- The parsed log entries are converted into dictionaries and stored in the database.
- Modify the regular expressions and parsing logic if the log file format differs.

## License
This code is released under the [MIT License](https://opensource.org/licenses/MIT).
