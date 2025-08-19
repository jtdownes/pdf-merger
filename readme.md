# PDF Merger Tool

A privacy-focused PDF merger desktop application built with Tkinter, tkinterdnd2, and PyPDF2. Allows users to seamlessly drag-and-drop or select PDF files, then merge them into a single PDF saved at a location of their choosing, all without uploading sensitive data online.

## Features
- Drag-and-drop PDF files into the app.
- Merge selected PDFs into a single file.
- Easy-to-use interface built with Tkinter.

## Requirements
- Python 3.8 or later
- Dependencies: Install via `pip install -r requirements.txt`

## Installation and Usage
1. Clone this repository:
   ```
   git clone https://github.com/jtdownes/pdf-merger.git
   cd pdf-merger-tool
   ```
2. Create and activate a virtual environment (recommended):
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   python app.py
   ```
5. Drag PDF files into the window and click "Merge PDFs" to combine them.

## Notes
- This app requires Tkinter, which is included with most Python installations.
- If you encounter issues with drag-and-drop (tkinterdnd2), ensure you have the latest Python and dependencies.

## Contributing
Feel free to open issues or pull requests!

Made by Josh Downes
