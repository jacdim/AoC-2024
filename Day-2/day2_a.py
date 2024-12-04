# --- Day 2: Red-Nosed Reports ---

reports = []

def checkSafety(report):
    # check if strictly increasing or decreasing
    areIncreasing = (report == sorted(report))
    areDecreasing = (report == sorted(report, reverse=True))

    # if neither increasing nor decreasing, return false
    if not areIncreasing and not areDecreasing:
        return False

    i = 1
    while(i < len(report)):
        # if gap between two numbers is larger than 3 or smaller than 1, return false
        if((abs(report[i] - report[i-1]) > 3) or (abs(report[i] - report[i-1]) < 1)):
            return False
        i += 1
    return True


    

with open('Day-2/day_2_input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        cleanedLine = line.strip('\n').split()
        intArray = [int(val) for val in cleanedLine]
        reports.append(intArray)

    checkedReports = []
    for report in reports:
        checkedReports.append(checkSafety(report))

    print(checkedReports.count(True))
