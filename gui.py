import tkinter as tk
from tkinter import filedialog
import importlib.util
import os
import subprocess
import shutil


class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.selected_files = []
        self.delete_files_in_directory()
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("File Selector")
        self.root.geometry("400x300")

        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.list_frame)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.select_button = tk.Button(
            self.root, text="Select Files", command=self.select_files)
        self.select_button.pack(side=tk.TOP, pady=10)

        self.run_button = tk.Button(
            self.root, text="Run", command=self.run_selected_files)
        self.run_button.pack(side=tk.BOTTOM, pady=10)

        # Bind double-click event to open_text_file function
        self.listbox.bind("<Double-Button-1>", self.open_text_file)

    def select_files(self):
        filenames = filedialog.askopenfilenames(
            filetypes=[("Text files", "*.txt")])
        self.selected_files = filenames
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for name in filenames:
            # Insert just the file name
            self.listbox.insert(tk.END, os.path.basename(name))
            # Copy the file to the script's directory
            shutil.copy(name, os.path.join(os.path.dirname(__file__), os.path.basename(name)))

    def run_selected_files(self):
        module_name = 'FileReaderExcel'
        module_file_path = f'{module_name}.py'
        if os.path.exists(module_file_path):
            spec = importlib.util.spec_from_file_location(
                module_name, module_file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            # Call the main function with selected files
            module.main(self.selected_files)
        else:
            print(f"Error: {module_file_path} does not exist.")

    def open_text_file(self, event):
        # Get the selected text file from the listbox
        index = self.listbox.curselection()[0]
        selected_file = self.selected_files[index]
        # Open the text file
        os.startfile(selected_file)

    def delete_files_in_directory(self):
        # Get the directory of the script file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Delete all text files in the directory
        for file_name in os.listdir(script_dir):
            file_path = os.path.join(script_dir, file_name)
            if os.path.isfile(file_path) and file_name.lower().endswith('.txt'):
                os.remove(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()
