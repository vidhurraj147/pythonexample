
python = 'python'

for letter in python:
    if letter == 'h':
        break
    else:
        print("letter is ",letter)

print("===========================")

for letter in python:
    if letter == 'h':
        continue
    else:
        print("Letter is ",letter)