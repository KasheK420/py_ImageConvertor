import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image #type: ignore

class ImageConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Converter")
        self.geometry("400x200")
        self.resizable(False, False)

        # Selected files and output folder
        self.files = []
        self.output_dir = ''

        # Widgets
        ttk.Button(self, text="Select Images", command=self.select_images).pack(pady=10)
        ttk.Button(self, text="Select Output Folder", command=self.select_output).pack(pady=10)

        format_frame = ttk.Frame(self)
        format_frame.pack(pady=10)
        ttk.Label(format_frame, text="Convert to:").pack(side=tk.LEFT)
        self.format_var = tk.StringVar(value="ico")
        ttk.Combobox(format_frame, textvariable=self.format_var, values=['ico', 'jpg', 'png', 'bmp', 'gif'], state='readonly', width=5).pack(side=tk.LEFT, padx=5)

        ttk.Button(self, text="Convert", command=self.convert).pack(pady=10)

    def select_images(self):
        paths = filedialog.askopenfilenames(
            title="Select images",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if paths:
            self.files = list(paths)

    def select_output(self):
        folder = filedialog.askdirectory(title="Select output folder")
        if folder:
            self.output_dir = folder

    def convert(self):
        if not self.files:
            messagebox.showwarning("No files", "Please select at least one image.")
            return
        if not self.output_dir:
            messagebox.showwarning("No output folder", "Please select an output folder.")
            return

        target_ext = self.format_var.get().lower()
        for file in self.files:
            try:
                img = Image.open(file)
                base = os.path.splitext(os.path.basename(file))[0]
                out_path = os.path.join(self.output_dir, f"{base}.{target_ext}")

                # ICO must be saved with sizes for Windows
                if target_ext == 'ico':
                    sizes = [(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]
                    img.save(out_path, format='ICO', sizes=sizes)
                else:
                    # Convert mode for formats like JPEG
                    if target_ext in ['jpg', 'jpeg'] and img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                    img.save(out_path, format=target_ext.upper())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert {file}: {e}")
                return

        messagebox.showinfo("Done", f"Converted {len(self.files)} file(s) to {target_ext.upper()}.")

if __name__ == '__main__':
    app = ImageConverterApp()
    app.mainloop()

# To build into an .exe, install PyInstaller:
# pip install pyinstaller pillow
# Then run:
# pyinstaller --onefile --windowed image_converter.py
