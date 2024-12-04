from day2_a import reports, checkSafety, checkedReports

for report in reports:
    if(checkSafety(report) != True):
        for i in range(0, len(report)):
            newReport = report[:i] + report[i + 1:]
            if(checkSafety(newReport) == True):
                checkedReports.append(True)
                break

print(checkedReports.count(True))
