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

csvpath = os.path.join("Resources", "election_data.csv")
txtpath = os.path.join("Analysis", "Voter_Analysis.txt")

candidates = []
voters = []

with open(csvpath, newline='') as csvfile:
            #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
            # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #first_data = next(csvreader)   

    #Append the open list variables before the with statement to the corresponding column in the csv. 
    for column in csvreader:
        candidates.append(column[2])
        voters.append(column[0])

#Count the total votes by using len and count (minus the header) all the data in column 0 or the "Voter ID" column
total_votes = (len(voters))

#Count each candidate in the list making variable an integer and then use the count function and count each time a "name" appears 
Khan = int(candidates.count("Khan"))
Correy = int(candidates.count("Correy"))
Li = int(candidates.count("Li"))
OTooley = int(candidates.count("O'Tooley"))
#print(Khan)
#print(Correy)
#print(Li)
#print(O_Tooley)

#Find percentage of votes each candidate won, percent = total_votes divided by the variable counted "name". formated to % by googling! 
Khan_percent = Khan / total_votes
Khan_format_percent = "{:.3%}".format(Khan_percent)

Correy_percent = Correy / total_votes
Correy_format_percent = "{:.3%}".format(Correy_percent)

Li_percent = Li / total_votes
Li_format_percent = "{:.3%}".format(Li_percent)

OTooley_percent = O_Tooley / total_votes
OTooley_format_percent = "{:.3%}".format(O_Tooley_percent)

#print("{:.3%}".format(Khan_percent))

#Find the winner with if/elif, go through each candidate count and if candidate 1 is greater than candidate 2 > cand 3, 4. 
# then print winner "name", do the same on next line with candidate 2 in start position, until all 4 scenarios are looked at
if Khan > Correy > Li > OTooley:
    Winner = "Khan"
elif Correy > Khan > Li > OTooley:
    Winner = "Correy"
elif Li > Khan > Correy > OTooley:
    Winner = "Li"
elif OTooley > Li > Correy > Khan:
    Winner = "O'Tooley"

print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
print(f"Khan: {Khan_format_percent} ({Khan}) ")
print(f"Correy: {Correy_format_percent} ({Correy})")
print(f"Li: {Li_format_percent} ({Li})")
print(f"O'Tooley: {OTooley_format_percent} ({OTooley})")
print("-------------------------------------")
print(f"Winner: {Winner}")
print("-------------------------------------")

f = open(txtpath,"w+")
print("Election Results", file=f)
print("-------------------------------------", file=f)
print(f"Total Votes: {total_votes}", file=f)
print("-------------------------------------", file=f)
print(f"Khan: {Khan_format_percent} ({Khan})", file=f)
print(f"Correy: {Correy_format_percent} ({Correy})", file=f)
print(f"Li: {Li_format_percent} ({Li})", file=f)
print(f"O'Tooley: {OTooley_format_percent} ({OTooley})", file=f)
print("-------------------------------------", file=f)
print(f"Winner: {Winner}", file =f)
print("-------------------------------------", file=f)
f.close