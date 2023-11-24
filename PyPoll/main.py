import os
import csv

election_csvpath = os.path.join("election_data.csv")

totalvotes = 0
# Stockhamvotes = 0
# DeGettevotes = 0
# Doanevotes = 0
# Stockhampercent = 0
# DeGettePercent = 0
# DoanePercent = 0
candidate_votes = {}
candidate_options = []

with open(election_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    for row in csvreader:
        totalvotes = totalvotes + 1

        if row[2] not in candidate_options:
            candidate_options.append(row[2])
            candidate_votes[row[2]] = 1
        else: 
            candidate_votes[row[2]] += 1

    # print(candidate_votes)
        
        # if row[2] == "Charles Casper Stockham":
        #     Stockhamvotes +=1
        # elif row[2] == "Diana DeGette":
        #     DeGettevotes +=1
        # elif row[2] == "Raymon Anthony Doane":
        #     Doanevotes +=1

# Stockhampercent = round((Stockhamvotes/totalvotes)*100, 3)
# DeGettePercent = round((DeGettevotes/totalvotes)*100, 3)
# DoanePercent = round((Doanevotes/totalvotes)*100, 3)
outputresults = "Election Results\n"
outputresults += "-------------------------\n"
outputresults += f"Total Votes: {totalvotes}\n"
outputresults += "-------------------------\n" 
winning_candidate = ""
winning_count = 0
for candidate, votes in candidate_votes.items():
    VotePercent = round((votes/totalvotes)*100, 3)
    outputresults += f"{candidate} {VotePercent}% ({votes})\n"

    if winning_count < votes: 
        winning_candidate = candidate
        winning_count = votes
outputresults += "-------------------------\n" 
outputresults += f"Winner: {winning_candidate}\n"
outputresults += "-------------------------"
print(outputresults)

outputresults_file = "Output/election_data.txt"
with open(outputresults_file,'w') as writer:

    writer.write(outputresults)