import os
import csv

budget_csvpath = os.path.join("Resources", "budget_data.csv")

months = []
revenue_change = []
monthofchange = []
countmonths = 0
totalrevenue = 0
previousrevenue = 0

with open(budget_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    
    for row in csvreader:
        countmonths += 1
        totalrevenue = totalrevenue + int(row[1])
        
        if previousrevenue != 0:
            changeinrevenue = int(row[1]) - previousrevenue
            revenue_change += [changeinrevenue]
            monthofchange += [row[0]]
        previousrevenue = int(row[1])
        

avgrevenue = round(sum(revenue_change) / len(revenue_change), 2)

maxchange = max(revenue_change)
minchange = min(revenue_change)

bestmonth_index = revenue_change.index(maxchange)
bestmonth = monthofchange[bestmonth_index]

worstmonth_index = revenue_change.index(minchange)
worstmonth = monthofchange[worstmonth_index]

print(f"Total Months: {countmonths}")
print(f"Total_Profit: ${totalrevenue}")
print(f"Average Revenue Change: ${avgrevenue}")
print(f"Greatest Increase in Profits: {bestmonth} ${maxchange}")
print(f"Greatest Decrease in Profits: {worstmonth} ${minchange}")
