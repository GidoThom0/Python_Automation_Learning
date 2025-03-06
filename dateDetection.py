import pyperclip, re, pyinputplus as pyip

# Create date regex.
dateRegex = re.compile(r'''(
    ([0-3]{1}\d{1})
    (/|-)
    ([0-1]{1}\d{1})
    (/|-)
    ([1-2]{1}\d{3})
    )''', re.VERBOSE)

# Find clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in dateRegex.findall(text):
    day = int(groups[1])
    month = int(groups[3])
    year = int(groups[5])

    # leap years 
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 2:
            if day > 29:
                continue
    # non-leap years
    elif month == 2:
        if day > 28:
            continue

    # Common checks
    if month > 12:
            continue
    elif month in [4, 6, 9, 11]:
        if day > 30:
            continue
    else:
        if day > 31:
            continue
    
    date = '/'.join([groups[1], groups[3], groups[5]])
    matches.append(date)

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates found.')


