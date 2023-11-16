import os
import csv

election_csvpath = os.path.join("Resources", "election_data.csv")

totalvotes = 0
Stockhamvotes = 0
DeGettevotes = 0
Doanevotes = 0

with open(election_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    for row in csvreader:
        totalvotes = totalvotes + 1
        
        if row[2] == "Stockham":
            Stockhamvotes +=1
        elif row[2] == "DeGette":
            DeGettevotes +=1
        elif row[2] == "Doane":
            Doanevotes +=1

print(f"Total Votes: {totalvotes}")
