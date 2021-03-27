#python-challenge

In both the PyBank and PyPoll projects I created a repo on github and cloned to my PC. Using gitbash I used the function mkdir to created the required directories/folders and nested them under the python-challenge main folder. I used the function touch to create the python and text files. I copied over the Resources folder/files over to my working python-challenge directory. I pushed changes to my repo on github via gitbash using git add ., git commit -m "", git push.

I used Visual Studio to record the code and ran the code on gitbash by calling up the python file: 'python main.py'. The code did not run properly on VS and I learned from many classmates they had the same issue. I started with the import os as a module to create file paths across operating systems and import csv for reading CSV files. I created the csv and txt paths to join the os to access the csv and txt files for reading and/or writing.

In the PyBank challenge the script outputs on the Financial_Analysis.txt and in the terminal to capture the total number of months, total amount of "Profit/Losses" over the entire period, calculates the changes in "Profit/Losses" over the entire period, and the average of those changes, greatest increase in profits (date and amount) over the entire period, greatest decrease in losses (date and amount) over the entire period. 

The highlights in the PyBank challenge were writing the for loop to find the total net profit changes and conditional statements for finding the greatest increase/decrease in net profit changes. 

The loop called on the data in the [1] position (Profit/Lossses) and subtracted one row from the previous row (previous_net) and then appended that data to the changes in profit list (previous variable was an empty list []) and stored the sum of all the changes to net profit as net_profit_change. 

for row in csvreader:
                
        total_profit += int(row[1]) 
        net_profit_change = int(row[1]) - previous_net 
        changes_in_profit.append (net_profit_change) 
        previous_net = int(row[1]) 

  Another highlight in the PyBank challenge was finding the greatest increase and decrease in profit. I first assigned values to the greatest increase and greatest decrease variables outside the loop. I choose to assign ["1900
  ", 0] to greatest increase I set the greatest decrease variable value to ["1900", 9999999999999999]. Then inside the loop I created a conditional statement that if the net profit change is > the greatest_increase then print the date then the net profit change. Did the same conditional statement for the greatest decrease shown below:           
        
        if net_profit_change > greatest_increase[1]:  
            greatest_increase[0] = row[0] 
            greatest_increase[1] = net_profit_change 
        
        
        if net_profit_change < greatest_decrease[1]:  
            greatest_decrease[0] = row[0] 
            greatest_decrease[1] = net_profit_change 


In the PyPoll challenge the script outputs on the Election_Analysis.txt and in the terminal to capture the total number of votes, a complete list of candidates and their individual total votes, the percentage of votes each candidate won along with the total number of votes each candiate won, and then finding the winner based on the greatest number of votes.

The most notable highlights in the PyPoll challenge were: 

I created empty lists variables for storing candidate and voters information in the for loop I appended the lists to columns (instead of rows!), used in the len method to count the total votes:

for column in csvreader:
        candidates.append(column[2])
        voters.append(column[0])

total_votes = (len(voters))

I used the .count function to count the number of times specific candidates names were listed in the data

Khan = int(candidates.count("Khan"))
Correy = int(candidates.count("Correy"))
Li = int(candidates.count("Li"))
OTooley = int(candidates.count("O'Tooley"))

I found the winner with the most popular votes by using the greater conditional statement going through the four different winner scenarios pulling the individual candidates total vote count.

if Khan > Correy > Li > OTooley:
    Winner = "Khan"
elif Correy > Khan > Li > OTooley:
    Winner = "Correy"
elif Li > Khan > Correy > OTooley:
    Winner = "Li"
elif OTooley > Li > Correy > Khan:
    Winner = "O'Tooley"

At the beginning of the assignment, I felt overwhelmed and went back to all the 03-Python Activities to get my bearings and used a bunch of the code in the activities in the assignments. I was fortunate to have an amazing tutor that was extremely helpful with the PyBank challenge and I gained the confidence I needed to finish the PyPoll assignment. As I progressed with the assignments I conferred heavily with my classmates in study group sessions and of course googled my way around and used overstock.com a lot. 