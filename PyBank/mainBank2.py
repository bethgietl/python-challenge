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

#import os/csv
import os
import csv

#select the file path
csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("Analysis", "Financial_Analysis.txt")

# Used Homework 2.9-Netflix to start the loop. Set Variables [] empty lists and helps to append
total_months = 0
total_profit = 0
changes_in_profit = []
date = []
avg_changes = 0
number_months = 0
greatest_increase = ["1900",0]
greatest_decrease = ["1900",999999999999999999999999999999999999]


# Open the CSV - use the newline argument per a classmate and research to keep data in empty strings from being altered 
with open(csvpath, newline='') as csvfile:
        #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
        # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    first_data = next(csvreader)   
    #print out total months (col. 0)
    total_months = 1
    #print out total profit/losses (col. 1), used int since the pl is a number (no decimals)
    total_profit += int(first_data[1]) #867884
    previous_net = int(first_data[1]) #867884

        # Read each row of data after the header
    for row in csvreader:
        #start on row 3 so can subtract from above
        total_months = total_months + 1 
        
        total_profit += int(row[1]) 
        net_profit_change = int(row[1]) - previous_net 
        changes_in_profit.append (net_profit_change) 
        previous_net = int(row[1]) 
        
        if net_profit_change > greatest_increase[1]:  
            greatest_increase[0] = row[0] 
            greatest_increase[1] = net_profit_change 
        
        
        if net_profit_change < greatest_decrease[1]:  
            greatest_decrease[0] = row[0] 
            greatest_decrease[1] = net_profit_change 
        
avg_changes = sum(changes_in_profit) / len(changes_in_profit)

print ("Financial Analysis")
print ("-----------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(avg_changes, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")

f = open(txtpath,"w+")
print ("Financial Analysis", file=f)
print ("-----------------------------------------------", file=f)
print(f"Total Months: {total_months}", file=f)
print(f"Total: ${total_profit}", file=f)
print(f"Average Change: ${round(avg_changes, 2)}", file=f)
print(f"Greatest Increase in Profits: {greatest_increase}", file=f)
print(f"Greatest Decrease in Profits: {greatest_decrease}", file=f)
f.close