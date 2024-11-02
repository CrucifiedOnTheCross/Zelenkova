import random

file = open('input.txt')
lines = file.readlines()
file.close()

print(random.choice(lines))
