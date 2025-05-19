# main.py
"""
@file    main.py
@author  Lukáš Majoros
@date    2025-05-19
@brief   Simple modern image‐converter GUI (PNG/JPG/BMP/GIF ↔ ICO, JPG, PNG, BMP, GIF)

This module provides ImageConverterApp, a Tkinter/ttk application that
lets you batch‐convert image files via a minimal, modern interface.

@example
    python main.py
    # -> select images, target format, output folder, click Convert.
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image

__version__ = "1.0.0"


class ImageConverterApp(ttk.Frame):
    """
    @class ImageConverterApp
    @brief Main application frame

    Initializes UI elements and handles user interactions:
      - File selection
      - Output folder selection
      - Format picker
      - Conversion
    """

    def __init__(self, master: tk.Tk):
        """
        @brief Constructor: sets up the window and widgets.

        @param master Parent Tk window.
        """
        super().__init__(master, padding=20)
        master.title("🖼️ Image Converter")
        master.geometry("450x250")
        master.resizable(False, False)
        master.iconbitmap('icon.ico')

        self.files = []         #: List[str]  Selected input file paths
        self.output_dir = ""    #: str        Selected output folder

        self._build_ui()
        self.pack(expand=True, fill="both")

    def _build_ui(self):
        """@brief Build and layout all UI widgets."""
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6)
        style.configure("TCombobox", padding=4)
        style.configure("TLabel", padding=4)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=5)

        ttk.Button(btn_frame, text="📂 Select Images", command=self.select_images).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="📁 Output Folder", command=self.select_output).pack(side="left", padx=5)

        fmt_frame = ttk.Frame(self)
        fmt_frame.pack(fill="x", pady=10)
        ttk.Label(fmt_frame, text="Convert to:").pack(side="left")
        self.format_var = tk.StringVar(value="ico")
        ttk.Combobox(
            fmt_frame, textvariable=self.format_var,
            values=["ico", "jpg", "png", "bmp", "gif"],
            state="readonly", width=8
        ).pack(side="left", padx=8)

        ttk.Button(self, text="⚡ Convert", command=self.convert).pack(pady=15)

    def select_images(self):
        """
        @brief Open file dialog to choose one or more images.

        Supported: PNG, JPG, JPEG, BMP, GIF.
        """
        paths = filedialog.askopenfilenames(
            title="Select images",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")],
        )
        if paths:
            self.files = list(paths)

    def select_output(self):
        """
        @brief Open folder dialog to choose output directory.
        """
        folder = filedialog.askdirectory(title="Select output folder")
        if folder:
            self.output_dir = folder

    def convert(self):
        """
        @brief Perform the batch image conversion.

        Checks inputs, converts each file to the target format,
        writes to the chosen output folder, and reports success/failure.
        """
        if not self.files:
            messagebox.showwarning("No files selected", "Please select at least one image.")
            return
        if not self.output_dir:
            messagebox.showwarning("No output folder", "Please select an output folder.")
            return

        target_ext = self.format_var.get().lower()
        success_count = 0

        for src in self.files:
            try:
                img = Image.open(src)
                base = os.path.splitext(os.path.basename(src))[0]
                dst = os.path.join(self.output_dir, f"{base}.{target_ext}")

                if target_ext == "ico":
                    sizes = [(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]
                    img.save(dst, format="ICO", sizes=sizes)
                else:
                    if target_ext in ("jpg","jpeg") and img.mode in ("RGBA","P"):
                        img = img.convert("RGB")
                    img.save(dst, format=target_ext.upper())

                success_count += 1

            except Exception as e:
                messagebox.showerror("Conversion Error", f"Could not convert\n{src}\n\n{e}")
                return

        messagebox.showinfo(
            "Conversion Complete",
            f"Converted {success_count} file(s) to {target_ext.upper()}."
        )


def main():
    """
    @brief Entry point. Creates the root window and runs the app loop.
    """
    root = tk.Tk()
    ImageConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
