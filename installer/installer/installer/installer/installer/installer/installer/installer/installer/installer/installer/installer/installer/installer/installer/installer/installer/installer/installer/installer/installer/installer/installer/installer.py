import tkinter as tk
from tkinter import messagebox
import requests
import os

class InstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Installer")

        self.instructions_label = tk.Label(root, text="This is the Randyt official installer. Enter the download path and click Continue:")
        self.instructions_label.pack()

        self.path_entry = tk.Entry(root, width=50)
        self.path_entry.pack()

        self.continue_button = tk.Button(root, text="Continue", command=self.download_program)
        self.continue_button.pack()

        self.cancel_button = tk.Button(root, text="Cancel", command=self.root.quit)
        self.cancel_button.pack()
        self.info_text = tk.Text(root, wrap=tk.WORD, height=5, width=50)
        self.info_text.insert(tk.END, "Read our programs license here: https://github.com/therandomspoon/randyt/blob/main/LICENSE. This project is entirely open-source.")
        self.info_text.pack()#
        self.info_text.config(state=tk.DISABLED)

    def download_program(self):
        download_path = self.path_entry.get()
        if not download_path:
            messagebox.showerror("Error", "Please enter a download path.")
            return

        program_url = "https://github.com/therandomspoon/randyt/raw/main/exe-download/randyt.exe"  # Replace with the actual download link
        program_filename = os.path.basename(program_url)
        local_filepath = os.path.join(download_path, program_filename)

        try:
            response = requests.get(program_url, stream=True)
            response.raise_for_status()

            with open(local_filepath, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            messagebox.showinfo("Success", f"Program downloaded to {local_filepath}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Download failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()
