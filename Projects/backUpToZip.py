#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increment

import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)    # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFilename = os.path.join(os.path.dirname(folder), f"{os.path.basename(folder)}_{number}.zip")
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print(f'Creating {zipFilename}')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Create the ZIP file with compression
    print(f'Creating {zipFilename}...')
    with zipfile.ZipFile(zipFilename, 'w', zipfile.ZIP_DEFLATED) as backupZip:
        
        # Walk the entire folder tree and compress files
        for foldername, subfolders, filenames in os.walk(folder):
            print(f'Adding files in {foldername}...')

            for filename in filenames:
                filePath = os.path.join(foldername, filename)
                relativePath = os.path.relpath(filePath, folder)  # Store relative path in ZIP
                backupZip.write(filePath, arcname=relativePath)
    
    backupZip.close()
    print('Done.')

# Example usage
# backupToZip('C:\\Users\\Gido\\delicious')