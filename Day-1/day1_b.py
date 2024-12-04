#  --- Day 2 ---

leftColumn = []
rightColumn = []

totalSimilarityScore = 0

with open('Day-1/day1_input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        leftColumn.append(int(line.split()[0]))
        rightColumn.append(int(line.split()[1]))
    for i in leftColumn:
        totalSimilarityScore += (rightColumn.count(i) * i)

    print(totalSimilarityScore)
    