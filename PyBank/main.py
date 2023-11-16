import os
import csv

budget_csvpath = os.path.join("Resources", "budget_data.csv")

months = []
profit = []

count_months = 0
net_profit = 0

with open(budget_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    
    for row in csvreader:
        count_months += 1
        net_profit = net_profit + int(row[1])
        
        

print(f"Total Months: {count_months}")
print(f"Total_Profit: {net_profit}")
