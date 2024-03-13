import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import importlib.util

class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.initialize_ui()
        self.selected_files = []
        self.output_directory = ""

    def initialize_ui(self):
        self.root.title("File Selector")
        self.root.geometry("400x400")

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

        self.select_output_dir_button = tk.Button(
            self.root, text="Select Output Directory", command=self.select_output_directory)
        self.select_output_dir_button.pack(side=tk.TOP, pady=10)

        self.output_dir_label = tk.Label(
            self.root, text="No Output Directory Selected", wraplength=300)
        self.output_dir_label.pack(side=tk.TOP, pady=10)

        self.run_button = tk.Button(
            self.root, text="Run", command=self.run_selected_files, state=tk.DISABLED)
        self.run_button.pack(side=tk.BOTTOM, pady=10)

    def select_files(self):
        filenames = filedialog.askopenfilenames(
            filetypes=[("Text files", "*.txt")])
        self.selected_files = filenames
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for name in filenames:
            # Insert just the file name
            self.listbox.insert(tk.END, name.split('/')[-1])
        self.update_run_button_state()

    def select_output_directory(self):
        self.output_directory = filedialog.askdirectory()
        if self.output_directory:
            self.output_dir_label.config(text=self.output_directory)
        self.update_run_button_state()

    def run_selected_files(self):
        # Execute pip command to install dependencies
        subprocess.run(["pip", "install", "scipy", "xlwt"])

        # Execute the main script if it exists
        module_name = 'FileReaderExcel'
        module_file_path = f'{module_name}.py'
        if os.path.exists(module_file_path):
            spec = importlib.util.spec_from_file_location(
                module_name, module_file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.main(self.selected_files, self.output_directory)
        else:
            print(f"Error: {module_file_path} does not exist.")

    def update_run_button_state(self):
        if self.selected_files and self.output_directory:
            self.run_button.config(state=tk.NORMAL)
        else:
            self.run_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()
