with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    if len(line.split()) > 1:
        print(line, end='')
