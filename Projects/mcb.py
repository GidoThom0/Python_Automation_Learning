#! python3
# # mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve
import pyperclip
import sys
from pathlib import Path

# Define the storage path
p = Path('../Other/mcb')

# Open the shelve database
mcbShelf = shelve.open(str(p))  # Convert Path to string for compatibility

# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print(f"Saved clipboard content as '{sys.argv[2]}'.")
    
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]
            print(f"Deleted saved entry '{sys.argv[2]}'.")
        else:
            print(f"'{sys.argv[2]}' not found in saved clipboard.")

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print("Copied list of saved keywords to clipboard.")
    
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print("Deleted all saved clipboard entries.")

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f"Copied saved content for '{sys.argv[1]}' to clipboard.")
    else:
        print(f"'{sys.argv[1]}' not found in saved clipboard.")

mcbShelf.close()
