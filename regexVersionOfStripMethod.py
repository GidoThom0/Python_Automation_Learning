import re

def stripMethod(text, stripChar = ''):
    stripRegex = re.compile(r'''(
        \s*?
        (\S{1})
        (.*)
        \s*?
        )''', re.VERBOSE)
    
    returnString = ''
    if stripChar == '':
        returnString += stripRegex.search(text).group(2)
        returnString += stripRegex.search(text).group(3)
    else:
        returnString = ''
        for char in stripRegex.search(text).group(2, 3):
            if char not in stripChar:
                returnString += char
    
    return returnString


string = input('Enter a string: ')
stripChar = input('Enter characters to strip: ')
print(stripMethod(string, stripChar))
