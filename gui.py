import tkinter as tk
from tkinter import filedialog


def open_file_dialog():
    filepath = filedialog.askopenfilename()
    if filepath:
        print(f"File selected: {filepath}")
    else:
        print("No file selected.")


# Set up the GUI
root = tk.Tk()
root.title("File Selector")

# Create a button to open the file dialog
open_file_btn = tk.Button(root, text="Open File", command=open_file_dialog)
open_file_btn.pack(pady=20)

# Start the GUI event loop
root.mainloop()
