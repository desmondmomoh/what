# WHAT - CLI File Type Identifier

WHAT is a lightweight Python command-line tool designed for security analysts and penetration testers to identify the true type of a file using its **Magic Numbers** (file signatures), bypassing deceptive file extensions.

## Why This Matters in Pentesting
Attackers often disguise malicious payloads by changing their extensions (e.g., renaming a dangerous `.exe` or script to `.jpg`). This tool bypasses the extension entirely by reading the raw binary headers to verify the file's authentic layout.

## Features
* **Zero Dependencies:** Uses strictly built-in Python modules (`sys`).
* **Safe Binary Reading:** Opens files in raw read-binary (`rb`) mode to prevent file corruption.
* **Robust Error Handling:** Gracefully handles missing arguments, non-existent files, and permission restrictions without crashing.

## Usage
Run the script from your terminal and provide the path to the target file as an argument:

```bash
python what.py <path_to_file>
