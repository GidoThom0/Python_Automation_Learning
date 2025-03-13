import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address_string = ' '.join(sys.argv[1:])
else:
    address_string = pyperclip.paste()
# Open Google Maps to desired place
webbrowser.open(f'https://www.google.co.za/maps/place/{address_string}')



