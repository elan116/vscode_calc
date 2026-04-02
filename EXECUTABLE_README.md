# Calculator Executable

## Overview
This folder contains `gui.exe` - a standalone Windows executable of the Calculator application. You don't need Python installed to run this file!

## How to Run

Simply double-click `gui.exe` to launch the calculator application.

## Features

- ✅ No Python installation required
- ✅ Stand-alone executable (self-contained)
- ✅ Windows-style GUI interface
- ✅ Full calculator functionality:
  - Basic arithmetic operations (+, -, *, /)
  - Calculation history
  - Clear and delete functions
  - Input validation
  - Error handling

## File Details

- **gui.exe** - Main calculator application (standalone executable)
- **File Size** - Approximately 60-80 MB (includes Python runtime and all dependencies)

## System Requirements

- Windows 7 or later (32-bit or 64-bit)
- No additional software required

## Usage Instructions

1. **Launch**: Double-click `gui.exe`
2. **Calculate**: 
   - Click number buttons (0-9)
   - Click an operator (+, -, *, /)
   - Click another number
   - Click "=" to see the result
3. **View History**: Click the "History" button to see past calculations
4. **Clear**: Click "Clear" to reset
5. **Delete**: Click "Delete" for backspace
6. **Exit**: Click "Exit" to close

## Troubleshooting

**Issue**: "Windows protected your PC" message
- **Solution**: Click "More info" > "Run anyway"

**Issue**: File won't run
- **Solution**: 
  - Right-click the file > Properties
  - Check if it's blocked (Unblock if necessary)
  - Run as Administrator

**Issue**: Antivirus warning
- **Solution**: The .exe is safe to run. This is a PyInstaller-generated executable. You can add it to your antivirus whitelist.

## Distribution

You can freely distribute this `.exe` file to other users. They can run it on any Windows machine without needing Python.

## Building Your Own Executable

To rebuild `gui.exe` from source:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed gui.py
```

The new executable will be in the `dist/` folder.

## Version Information

- Python Version: 3.14+
- Framework: tkinter (built-in with Python)
- PyInstaller Version: 6.19.0
- Build Date: April 2, 2026
