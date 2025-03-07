from pathlib import Path

p = Path('Text Files', 'spam.txt')
p.parent.mkdir(parents=True, exist_ok=True)  # Creates "Text Files" if it doesn't exist
p.write_text('Hello, World!')

# Open and read the file properly
with open(p, 'r') as helloFile:
    content = helloFile.read()

print(content)



