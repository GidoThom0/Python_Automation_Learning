from pathlib import Path
import re

# Get the file path
filePath = Path(input('Set file path to file: '))

# Read file content
content = filePath.read_text()

# Define the placeholders to replace
placeholders = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]

# Find all occurrences of placeholders in order
matches = re.findall(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', content)


if not matches:
    print("No placeholders found in the file.")
else:
    print(f"Found {len(matches)} placeholders: {matches}")

    # Replace each placeholder in order of appearance
    for match in matches:
        replacement = input(f"Enter a {match.lower()}: ")  # Ask user for input
        content = content.replace(match, replacement, 1)  # Replace one at a time

    # Write the updated content back to the file
    filePath.write_text(content)

    print("Replacement complete!")
