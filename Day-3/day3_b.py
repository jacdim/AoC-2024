import re
from day3_a import lines

# initialize total sum
total = 0

# initialize matches array
matches = []

# regex pattern for capturing intructions
pattern = r"(do\(\)|don't\(\)|mul\((-?\d+),(-?\d+)\))"

for line in lines:
    # find all instructions in order
    instructions = re.findall(pattern, line)
    for instruction in instructions:
        matches.append(instruction)

# state variable for enabling calculation
enabled = True
for match in matches:
    if 'do()' in match[0]:
        enabled = True
    elif "don't()" in match[0]:
        enabled = False
    elif enabled and ('mul(' in match[0]):
        total += (int(match[1]) * int(match[2]))

print(total)
