import tkinter as tk
from tkinter import ttk
from reqst import download_file
from tqdms import download_with_progress
from rerun import resume_download
from intergrityVerify import verify_integrity

# GUI code
class DownloadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Download Client")
        self.root.maxsize(600, 400)
        window_height = 400
        window_width = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.pack(pady=10)

        self.download_button = ttk.Button(root, text="Start Download", command=self.start_download)
        self.download_button.pack(pady=10)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

    def start_download(self):
        url = self.url_entry.get()
        if url:
            destination = url.split('/')[-1]
            download_with_progress(url, destination)

def run_gui():
    root = tk.Tk()
    # app = DownloadApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
