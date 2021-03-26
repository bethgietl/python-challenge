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
total_profit = 0

#       1. Open the path, CSV reader specifies delimiter and variable that holds contents, Read the header and first rows
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)   
    first_data = next(csvreader)

#       2. to find the total months start with appending the months list to col. 0 (Months) then use the len funtion to find the length of the month list    
    for column in csvreader:
        months.append(column[0])
    
    total_months = (len(months))+1

    #print(total_months)

#       3. net the total amount of "Profit/Losses" over the entire period sum

    total_profit += int(first_data[1]) 
    previous_net = int(first_data[1])

    for row in csvreader:
        total_months = total_months + 1 #4
        
        total_profit += int(row[1]) #867884 + 984655 + 322013 + -69417
        net_profit_change = int(row[1]) - previous_net #-69417 - 322013
        changes_in_profit.append (net_profit_change) #[116771, -662642, -391430]
        previous_net = int(row[1]) #-69417

print(previous_net)
        
        #if net_profit_change > greatest_increase[1]:  #["1900", 0]
            #greatest_increase[0] = row[0] #[Feb-10, 0]
            #greatest_increase[1] = net_profit_change #[Feb-10,116771]



