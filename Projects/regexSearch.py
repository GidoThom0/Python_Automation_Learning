from pathlib import Path
import re

# Prompt user for folder path and regular expression
folder_path = Path(input('Enter folder path: '))
regular_expression = input('Enter the regular expression: ')

# Compile the regular expression for later use
pattern = re.compile(regular_expression)

# Iterate through all .txt files in the folder
for txt_file in folder_path.glob('*.txt'):
    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            # Read each line in the file
            for line_num, line in enumerate(file, start=1):
                # If the line matches the regular expression, print the result
                if pattern.search(line):
                    print(f'File: {txt_file.name}, Line {line_num}: {line.strip()}')
    except Exception as e:
        print(f"Error reading {txt_file}: {e}")