#! python3
# phoneAndEmailExtractor.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Create phone regex.
phoneRegex = re.compile(r'''(
    ([+]{1}|[(+]{2})?
    (\d{1,2})
    (\()?
    (\s|-|\.)?
    (\d{2,3})
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)?
    (\d{4})            
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    ([a-zA-Z0-9._%+-]+)
    @
    ([a-zA-Z0-9.-]+)
    (\.[a-zA-Z.]{2,6})
    )''', re.VERBOSE)

# Find clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = ''
    if len(groups[2]) == 1:
        phoneNum = ' '.join(['+27', groups[5], groups[7], groups[9]])
    else:
        phoneNum = ' '.join(['+' + groups[2], groups[5], groups[7], groups[9]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[2])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')