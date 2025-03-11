import os, shutil
from pathlib import Path

def copyAndPasteSelectedFiles(
    fileType: str,
    targetDir: Path,
    newDir: Path
):
    for foldername, subfoldernames, filenames in os.walk(targetDir):
        fileType = fileType.lower()
        print(f'Searching {foldername} for any .{fileType} files')

        for filename in filenames:
            root, extension = os.path.splitext(filename)
            if extension == f'.{fileType}':
                filePath = os.path.join(foldername, filename)
                relativePath = os.path.relpath(filePath, targetDir)     # get relative path to copy the relative path to the file

                # Create directories if they don't exist
                destination_path = newDir / relativePath
                destination_path.parent.mkdir(parents=True, exist_ok=True)

                shutil.copy(filePath, newDir / relativePath)
                print(f'Copied {filename} to {newDir / relativePath}')

    print('Done!')

copyAndPasteSelectedFiles(
    'TXt',
    Path(r'C:\Users\Gido\OneDrive - Westbrooke Capital partners\Desktop\python_program_testing\selectiveCopying\input'),
    Path(r'C:\Users\Gido\OneDrive - Westbrooke Capital partners\Desktop\python_program_testing\selectiveCopying\output')
)

                