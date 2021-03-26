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



toatl_votes = 0 
dup_candidate = []
candidates = [] 
percent_won = [] 
candidate_votes = 0 
voter = []
voted_for = []

def load_file(filepath):
    
    with open(csvpath, newline='') as csvfile:
            #CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
            # Read the header row first (skip this step if there is now header)
        csv_header = next(csvreader)
        first_data = next(csvreader)   

# Grab the text for a Resume
candidate_list = load_file(csvpath)

# Create a set of unique words from the resume
names = set()

# Loop through the word list and count each word.
for word in candidate_list:
    word_count[word] += 1
print(word_count)

# Bonus using collections.Counter
word_counter = Counter(candidate_list)
print(word_counter)

# Comparing both word count solutions
print(word_count == word_counter)


    for row in csvreader:
            
            total_votes = total_votes + 1 

            voter.append(row[0])
            voted_for.append(row[2])
            candidate_list = row[2]
            candidates.append (candidate_list) 
            candidate_list = list(set(voted_for))

        
#print(candidates)
#print(total_votes)

print ("Election Results")
print ("-----------------------------------------------")
print(f"Total Votes: {total_votes}")

