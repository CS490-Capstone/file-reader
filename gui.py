import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import shutil

def run_FileReaderExcel():
    subprocess.Popen(["python", "FileReaderExcel.py"])

def open_file_dialog():
    # Get the directory of the GUI file
    gui_dir = os.path.dirname(__file__)
    filepaths = filedialog.askopenfilenames(initialdir=gui_dir)
    if filepaths:
        print("Files selected:")
        for filepath in filepaths:
            print(filepath)
            # Get the filename from the filepath
            filename = os.path.basename(filepath)
            # Move or copy the file to the GUI directory
            shutil.copy(filepath, os.path.join(gui_dir, filename))
            print(f"File copied to {gui_dir}")
            # Check if the file is a text file
            if filename.lower().endswith('.txt'):
                # Add the filename to the listbox
                file_listbox.insert(tk.END, filename)
    else:
        print("No files selected.")

def open_text_file(event):
    # Get the selected text file from the listbox
    selected_file = file_listbox.get(file_listbox.curselection())
    # Open the text file
    os.system(selected_file)

# Set up the GUI
root = tk.Tk()
root.title("File Selector")

# Set the size of the root window
root.geometry("400x400")  # Width x Height

# Add a label widget for the title
title_label = tk.Label(root, text="File Selector", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create a button to open the file dialog
open_file_btn = tk.Button(root, text="Open File", command=open_file_dialog)
open_file_btn.pack(pady=10)

# Create a listbox to display selected text files
file_listbox = tk.Listbox(root)
file_listbox.pack(pady=10)

# Bind double-click event to open_text_file function
file_listbox.bind("<Double-Button-1>", open_text_file)

# Create a button to run FileReaderExcel.py
run_script_btn = tk.Button(root, text="Run", command=run_FileReaderExcel)
run_script_btn.pack(pady=10)

# Start the GUI event loop
root.mainloop()
