from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import re
import datetime
import os
import json

#region database

DATABASE_FILE = 'db.json'

db = []

if not os.path.isfile(DATABASE_FILE):
    with open(DATABASE_FILE, 'x'):
        print('')

with open(DATABASE_FILE, 'r') as file:
    try:
        db = json.load(file)
    except json.decoder.JSONDecodeError:
        db = []

def save_db():
    with open(DATABASE_FILE, 'w') as file:
        json.dump(db, file)

def dump_db():
    global db
    db = []
    with open(DATABASE_FILE, 'w') as file:
        json.dump(db, file)

#endregion

#region Regex

line_pattern = r'(.*)\t(\d{1,2}/\d{1,2}/\d{2,4} \d{1,2}:\d{1,2}:\d{1,2} \w{2})\t(.*)\t(\d{1,5})\t(.*)\t(.*)'
multi_line_pattern = r'\".*(?!\")'
multi_line_end_pattern = r'\"\n'
timestamp_pattern = "%m/%d/%Y %I:%M:%S %p"

def get_dict_from_line(text):
    text_with_pattern = re.match(line_pattern, text)
    if not text_with_pattern:
        return text 
    
    event_type = text_with_pattern.group(1)
    timestamp = text_with_pattern.group(2)
    timestamp = datetime.datetime.strptime(timestamp, timestamp_pattern)
    source = text_with_pattern.group(3)
    event_id = text_with_pattern.group(4)
    category = text_with_pattern.group(5)
    message = text_with_pattern.group(6)
    
    return {
        'Event Type':event_type,
        'Timestamp':timestamp.strftime(timestamp_pattern),
        'Source':source,
        'Event ID':event_id,
        'Category':category,
        'Message':message
    }

def parse_log_data(file):
    while file.readline():
        line_as_dict = get_dict_from_line(file.readline())
        if type(line_as_dict) == dict:
            db.append(line_as_dict)
    save_db()
#endregion

#region UI

def add_dict_to_screen(dictionary, textwidget):
    for key, value in dictionary.items():
        textwidget.insert(END, f"{key}: {value}\n")
        if key == 'Message':
            textwidget.insert(END, '\n')

def search_json(searchterm, textwidget):
    if searchterm.strip == '':
        for dictionary in db:
            add_dict_to_screen(dictionary, textwidget)
    textwidget.delete('1.0', END)
    results = []
    for dictionary in db:
        for key, value in dictionary.items():
            if searchterm.lower() in key.lower() or searchterm.lower() in str(value).lower():
                add_dict_to_screen(dictionary, textwidget)
    if results:
        textwidget.insert(END, "\n".join(results))
    else:
        textwidget.insert(END, "No results found.")

def load_log():
    print("load log button pressed")
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    try:
        with open(filename, 'r') as file:
            parse_log_data(file)
    except FileNotFoundError:
        if filename == '':
            return
        messagebox.showerror("Failure", "File not found :\\")
        return
    messagebox.showinfo("Success","Successfully loaded file")


def view_log():
    new_window = Toplevel()
    new_window.title('Log Viewer')

    searchframe = Frame(new_window)
    searchframe.pack(pady=10)

    searchlabel = Label(searchframe, text='Search')
    searchlabel.pack(side=LEFT)
    
    searchentry = Entry(searchframe, width=30)
    searchentry.pack(side=LEFT)
    
    searchbutton = Button(searchframe, text="Search", command=lambda: search_json(searchentry.get(), textwidget))
    searchbutton.pack(side=LEFT)
    
    logframe = ttk.Frame(new_window)
    logframe.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    #fuck this scrollbar
    scrollbar = ttk.Scrollbar(logframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    textwidget = Text(logframe, wrap=WORD)
    textwidget.pack(side=LEFT, fill=BOTH, expand=TRUE)
    
    scrollbar.config(command=textwidget.yview)
    textwidget.config(yscrollcommand=scrollbar.set)
    
    for dictionary in db:
        add_dict_to_screen(dictionary, textwidget)

def delete_logs():
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to clear the database?")
    if confirmation:
        dump_db()

root = Tk()
root.geometry("300x300+100+100")

load_button = Button(root, text="Load a log file", command=load_log)
load_button.pack()

view_button = Button(root, text="View log entries", command=view_log)
view_button.pack()

delete_button = Button(root, text="Delete saved log entreis", command=delete_logs)
delete_button.pack()

quit_button = Button(root, text="Quit", command=quit)
quit_button.pack()

root.mainloop()

#endregion