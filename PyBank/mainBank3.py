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

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("Analysis", "Financial_Analysis.txt")

months = []

with open(csvpath, newline='') as csvfile:
        #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
        # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)   
    first_data = next(csvreader)

    for column in csvreader:
        months.append(column[1])
    
    total_months = (len(months))+1

print(total_months)





