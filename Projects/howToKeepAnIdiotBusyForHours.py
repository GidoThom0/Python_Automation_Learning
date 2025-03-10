import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?'
    response = pyip.inputYesNo(prompt)
    if response == 'no' or response == 'No' or response == 'NO' or response == 'n' or response == 'N':
        break
    elif response == 'yes' or response == 'Yes' or response == 'YES' or response == 'y' or response == 'Y':
        continue
    else:
        print(response + ' is not a valid response.')

print('Thank you. Have a nice day.')