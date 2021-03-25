#Your task is to create a Python script that analyzes the records to calculate each of the following:
        #Financial Analysis
        #-----------------------------------------
    #The total number of months included in the dataset
        #Total Months: 86
    #The net total amount of "Profit/Losses" over the entire period
        #Total: 38382578
    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        #Average Change: $-2315.12
    #The greatest increase in profits (date and amount) over the entire period
        #Greatest Increase in Profits: Feb-2012 ($1926159)
    #The greatest decrease in losses (date and amount) over the entire period
        #Greatest Decrease in Profits: Sep-2013 ($-2196167)

#main lessons:
    #len
    #list
    #Print summary and answers
    #nested if statements
    #for loop and while


#homework 2.8 shows how to import
    # First import the os module. This will allow us to create file paths across operating systems
import os
    # Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("Analysis", "Financial_Analysis.txt")

# Used Homework 2.9-Netflix to start the loop
    #Set Variables
total_months = 0
profit_losses = 0
total_pl = 0
changes_in_pl = []
date = []
total_changes = []
avg_changes = 0
number_months = 0
greatest_incrase = 0
greatest_decrease = 0
#define as a string
date_increase = ""
date_decrease = ""

#revenue = [] = changes_in_pl
#date = [] = date
#rev_change = [] = total_changes

# Open the CSV   
with open(csvpath) as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
        # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
        # Read each row of data after the header
    for row in csvreader:
        total_months = total_months + 1
        total_pl += int(row[1])
      # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
        changes_in_pl.append(float(row[1])
        #date.append(row[0])
    
     #in this loop I did total of difference between all row of column "Profit/Losses" and found total PL change. Also found out max PL change and min PL change. 
    for i in range(len(changes_in_pl)):
        total_changes += changes_in_pl[i]
        #total_changes.append(changes_in_pl[i] - changes_in_pl[i-1])   
    avg_changes = total_changes / len(changes_in_pl)

   
        
        #avg_changes = round(total_pl / total_months, 2)

        #change_pl.append(profit_losses) 
        #change_pl.append(row[0])
        #number_months += 1   

            # Determine percent of review left to 2 decimal places
        #percent = round(int(row[6]) / int(row[5]), 2)
        #review_percent.append(percent)       

print ("Financial Analysis")
print ("-----------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_pl}")
print(f"Average Change: {avg_changes}")
print(f"Greatest Increase in Profits: {greatest_incrase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")
    