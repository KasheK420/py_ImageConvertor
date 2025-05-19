<!-- README.md -->

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  
![Version](https://img.shields.io/badge/version-1.1.0-green)  
![License](https://img.shields.io/badge/license-MIT-lightgrey)  
![Dependencies](https://img.shields.io/badge/requirements-Pillow%2C%20Tkinter-blueviolet)  
![Build](https://img.shields.io/badge/build-PyInstaller-brightgreen)

# Image Converter

Simple minimalistic GUI tool to batch-convert PNG, JPG, BMP, GIF ↔ ICO (and vice versa).

## Features

- Select multiple images at once  
- Choose target format: `ico`, `jpg`, `png`, `bmp`, `gif`  
- Batch export to chosen directory  
- Proper ICO sizing for Windows icons  
- Cross-platform (Windows, macOS, Linux)

## Installation

```bash
# 1. Clone repo
git clone https://github.com/KasheK420/py_ImageConverter.git
cd py_ImageConverter

# 2. Create venv & install
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
pip install --upgrade pip
pip install -r requirements.txt


