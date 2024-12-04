# --- Day 1: Historian Hysteria ---

leftColumn = []
rightColumn = []
orderedPairs = []

with open('Day-1/day1_input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        leftColumn.append(line.split()[0])
        rightColumn.append(line.split()[1])
    leftColumn.sort()
    rightColumn.sort()
    for l,r in zip(leftColumn, rightColumn):
        orderedPairs.append((l,r))

    totalSum = 0
    for tuple in orderedPairs:
        totalSum += (abs(int(tuple[0]) - int(tuple[1])))


    print(totalSum)