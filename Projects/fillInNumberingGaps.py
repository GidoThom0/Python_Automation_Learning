import os, re
from pathlib import Path

def fillNumberGaps(
    givenPrefix: str,
    fileType: str,
    targetDir: Path
):
    previousNumber = '0'
    for dirpath, _, filenames in os.walk(targetDir):
        for filename in filenames:
            root, extension = os.path.splitext(filename)

            # Ignore if the fileType is incorrect
            if extension.lower() != '.' + fileType.lower():
                continue

            # Ignore if the prefix is incorrect
            if not root.startswith(givenPrefix):
                continue

            currentNumber = root[len(givenPrefix):]  # Extract the number part

            if not currentNumber.isdigit():
                continue  # Skip if it's not a number

            # First number
            if int(previousNumber) == 0:
                previousNumber = currentNumber
                continue

            if int(currentNumber) - int(previousNumber) > 1:
                currentNumber = str(int(previousNumber) + 1)

                # Ensure number has the same length (leading zeros)
                while len(currentNumber) < len(previousNumber):
                    currentNumber = '0' + currentNumber

                new_filename = givenPrefix + currentNumber + extension
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))
                print(f"Renamed: {filename} -> {new_filename}")

            previousNumber = currentNumber  # Update previous number

fillNumberGaps(
    'spam',
    'txt',
    Path(r'C:\Users\Gido\OneDrive - Westbrooke Capital partners\Desktop\python_program_testing\fill_number_gaps')
)