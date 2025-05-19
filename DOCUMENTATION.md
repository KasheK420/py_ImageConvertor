<!-- DOCUMENTATION.md -->

# Developer Documentation

## Architecture

- **main.py**  
  - Entry point; sets up `tk.Tk()` root and `ImageConverterApp`.
- **ImageConverterApp**  
  - UI class using `ttk.Frame`.
  - Methods:
    - `select_images()`
    - `select_output()`
    - `convert()`

## Key Classes & Functions

### `ImageConverterApp(master: tk.Tk)`
- Inherits from `ttk.Frame`
- Attributes:
  - `files: List[str]`
  - `output_dir: str`
  - `format_var: tk.StringVar`
- UI built in `_build_ui()` using `ttk.Style`.
- Conversion logic in `convert()`:
  1. Validate inputs
  2. Loop files, open via PIL
  3. Save as ICO (with sizes) or other format
  4. Error handling via `messagebox`

### `main()`
- Initializes root window.
- Instantiates and packs `ImageConverterApp`.
- Starts `mainloop()`.

## Extending

- **Add Formats**: Extend combobox values and handle new extensions in `convert()`.  
- **Custom Icon**: Place your `.ico` in project root and uncomment `master.iconbitmap('icon.ico')`.  
- **Theme**: Switch `style.theme_use("clam")` to any installed ttk theme.

## Doc Comments

All public methods and classes are annotated with Doxygen-style `@brief`, `@param` and `@author`.
