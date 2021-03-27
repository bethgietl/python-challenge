#python-challenge

In both the PyBank and PyPoll projects I created a repo on github and cloned to my PC. Using gitbash I used the function mkdir to created the required directories/folders and nested them under the python-challenge main folder. I used the function touch to create the python and text files. I copied over the Resources folder/files over to my working python-challenge directory. I pushed changes to my repo on github via gitbash using git add ., git commit -m "", git push.

I used Visual Studio to record the code and ran the code on gitbash by calling up the python file: 'python main.py'. The code did not run properly on VS and I learned from many classmates they had the same issue. I started with the import os as a module to create file paths across operating systems and import csv for reading CSV files. I created the csv and txt paths to join the os to access the csv and txt files for reading and/or writing.

In the PyBank challenge the script outputs on the Financial_Analysis.txt and in the terminal to capture the total number of months, total amount of "Profit/Losses" over the entire period, calculates the changes in "Profit/Losses" over the entire period, and the average of those changes, greatest increase in profits (date and amount) over the entire period, greatest decrease in losses (date and amount) over the entire period. 

The highlight in the PyBank challenge was writing the for loop to find the total net profit changes by taking one row and subtracting from the previous row (previous_net) and then appending the stored the sum of all the changes to net profit in a list net_profit_change list
for row in csvreader:
        #start on row 3 so can subtract from above
        total_months = total_months + 1 
        
        total_profit += int(row[1]) 
        net_profit_change = int(row[1]) - previous_net 
        changes_in_profit.append (net_profit_change) 
        previous_net = int(row[1]) 

  Another highlight in the PyBank challenge was finding the greatest increase and decrease in profit. I first assigned values to the greatest increase and greatest decrease variables outside the loop. I choose to assign ["1900
  ", 0] to greatest increase I set the greatest decrease variable value to ["1900", 9999999999999999].Then inside the loop created a conditional statement that if the net profit change is > the greatest_increase then print the date then the net profit change. Did the same conditional statement for the greatest decrease shown below:           
        
        if net_profit_change > greatest_increase[1]:  
            greatest_increase[0] = row[0] 
            greatest_increase[1] = net_profit_change 
        
        
        if net_profit_change < greatest_decrease[1]:  
            greatest_decrease[0] = row[0] 
            greatest_decrease[1] = net_profit_change 


Technology - What does the program need to run? What language? What version? A specific OS? Dependencies: Mention any external libraries the user needs to download. (Those included in the default distribution, like os and csv don't need to be mentioned) Usage Instructions - How does a user run the program? Does one need to be in the same directory as the script? (Recommended for this class when you are reading files) (Optional): Inputs/Outputs Does the program read a file? What format? Does it take user input? How? What information does the input contain? Is there an expected filepath? Does the program produce a file? What format? Does it print to the terminal? What information does the output contain? What filepath does it write the output to? Note: Including all of this^^ is too much info, only include what is necessary to use the program (External/Further) Documentation - If there is a source of more detailed info definitely provide a URL or some instruction on how to access it Readmes can vary greatly in their level of detail and completeness. For this, don't worry too much about it, some basic instructions will suffice. Since it's only mentioned in passing in the instructions and isn't on the rubric I think it's mostly an exercise to get you in the good habit of providing one. The graders are probably just checking that you have one and that it gives some relevant information.

Formal Documentation:

created a repository on github called python-challenge
made a clone on my PC ---used gitbash / terminal to cd and ls my way around to find where I wanted to make the clone ---used git clone link in the python-challenge
using bash created the necessary folders and files and nested them in the python-challenge folder ----mkrdir for creating the PyBank PyPoll folders and inside those folders created Analysis and Resources folders ----touch for creating the main.py python and analysis.txt text files for each homework assignment
pushed changes to the repo on github ---cd to python-challenge folder ---git status (new things added/updated are red) ---git add . ---git status (new things added/updated turn green) ---git commit -m "made a comment" ---git push
#PyBank

read the instructions throughly and tried to take one step at a time
added the instructions to the visual studio file for easy reference
started with dependencies - have to have these in order to create file paths ---used Activity 03-Python.08.read_csv.py ------import the os module = this allows to create file paths across operating systems ---import os -------module for reading CSV files ---import csv
created the file path for the csv file and created the text path as well since that was the last step of the homework's instructions ----used Activity 03-Python.08.read_csv.py ---csvpath = os.pathjoin("Resource", "budget_analysis.csv") ---txtpath = os.path.join("Analysis", "Financial_Analysis.txt")
Set the variables, I started with total months so the first variable I set was total_months and added to the variable list as I moved down the instructions. I ended up messing around with different types of code so I had a lot of variables I commented out that I ended up not needing. ---total_months = 0 ---later as I worked through the instructions: I added variables and set the values to either 0, an empty list [] I can append to later or a list with specific values: total_profit = 0; changes_in_profit = [] empty list; date = [], number_months = 0; greatest_increase = ["1900", 0] created a list of dates and numbers; greatest_decrease = ["1900", 999999999] created a list of dates and then a BIG number
open the file path and added newline=''The newline keeps data in empty strings from being altered. ---with open(csvpath, newline='') as csvfile: ---#CSV reader specifies delimiter and variable that holds contents csvreader = csv.reader(csvfile, delimiter=',') # Read the header row first (skip this step if there is now header) csv_header = next(csvreader) first_data = next(csvreader)
---Used Homework 2.9-Netflix to start the loop

#PyPoll

##To count the number of voters I used the len function ---used Activity 03-Python.09.lists.py

##To find the candidate witht the most votes and call him the winner I used a nested if/elif statement ---used Activity 03-Python.07.conditionals.py ---if (Khan) > (Correy) > (Li) > (O'Tooley): Winner = "Khan" elif (Correy) > (Khan) > .... Winner = "Correy" else (O'Tooley) > .... Winner = "O'Tooley"