#Election Results
    #------------------
#The total number of votes cast
    #Total Votes: 3521001
    #-------------------
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
    #Khan: 63.000% (2218231)
    #Correy: 20.000% (704200)
    #Li: 14.000% (492940)
    #O"Tooley: 3.000% (105630)
    #------------------------
#The winner of the election based on popular vote.
    #Winner: Khan
    #-------------------------------------
import os
import csv

# Counter is used for the bonus solution
from collections import Counter

csvpath = os.path.join("Resources", "election_data.csv")

candidates = []
voters = []

with open(csvpath, newline='') as csvfile:
            #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
            # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    first_data = next(csvreader)   

    for column in csvreader:
        candidates.append(column[2])
        voters.append(column[0])

total_votes = (len(voters))
#count each candidate in the list
Khan = int(candidates.count("Khan"))
Correy = int(candidates.count("Correy"))
Li = int(candidates.count("Li"))
O_Tooley = int(candidates.count("O'Tooley"))

print(Khan)


print ("Election Results")
print ("-----------------------------------------------")
print(f"Total Votes: {total_votes}")