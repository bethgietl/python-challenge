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
changes_in_profit = []
date = []
number_months = 0
avg_changes = 0
greatest_increase = ["1900",0]
greatest_decrease = ["1900",99999999999999999999999999]

#       1. Open the path, CSV reader specifies delimiter and variable that holds contents, Read the header and first rows
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)   
    first_data = next(csvreader)
    
    total_months = 1
    total_profit += int(first_data[1])
    previous_net = int(first_data[1])

#       2. to find the total months start with appending the months list to col. 0 (Months) then use the len funtion to find the length of the month list    
    for row in csvreader:
        months.append(row[0])
    
    total_months = (len(months))+1
#print(total_months) #86
#print(total_profit) #= 867884
#print(previous_net) = 867884
#       3. net the total amount of "Profit/Losses" over the entire period sum
    total_profit += int(row[1]) #867884 + 984655 + 322013 + -69417
    net_profit_change = int(row[1]) - previous_net #-69417 - 322013
    changes_in_profit.append (net_profit_change) #[116771, -662642, -391430]
    previous_net = int(row[1]) #-69417
    if net_profit_change > greatest_increase[1]:  #["1900", 0]
        greatest_increase[0] = row[0] #[Feb-10, 0]
        greatest_increase[1] = net_profit_change #[Feb-10,116771]
    
if net_profit_change < greatest_decrease[1]:  #["1900",999999999999999999999999999999999999]
            greatest_decrease[0] = row[0] #[Feb-10, 0]
            greatest_decrease[1] = net_profit_change #[Feb-10,116771]

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



