import os, send2trash
from pathlib import Path

def deleteLargeFiles(
    minFileSize: float,    # MB
    targetDir: Path
):
    for foldername, subfolders, filenames in os.walk(targetDir):
        print(f'Looking in {foldername} for files in excess of {minFileSize}MB to send to trash...')

        for filename in filenames:
            filePath = os.path.join(foldername, filename)
            if os.path.getsize(filePath) >= int(minFileSize * 1000000):
                print(f'Deleting {filename}')
                send2trash.send2trash(filePath)

    print('Done!')
            
deleteLargeFiles(
    0.001,
    Path(r'C:\Users\Gido\OneDrive - Westbrooke Capital partners\Desktop\python_program_testing\selectiveCopying')
)