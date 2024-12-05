import re

# regex pattern to match any ocurence of mul(x,x) where x can be any integer
regexPattern = r"mul\(-?\d+,-?\d+\)"

matches = []
total = 0

with open('Day-3/day3_input.txt', 'r') as file:
    lines = file.readlines()
    file.close()

for line in lines:
    for match in re.findall(regexPattern, line):
        matches.append(match)

for match in matches:
    match = match.strip("mul()")
    match = match.split(',')
    total += int(match[0]) * int(match[1])

print(total)


