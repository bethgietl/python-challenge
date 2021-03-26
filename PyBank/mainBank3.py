#homework 2.8 shows how to import
    # First import the os module. This will allow us to create file paths across operating systems
import os
    # Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("Analysis", "Financial_Analysis.txt")

# Used Homework 2.9-Netflix to start the loop
    #Set Variables [] empty lists and helps to append
total_months = 0
#profit_losses = 0
total_profit = 0
changes_in_profit = []
date = []
#total_changes = []
avg_changes = 0
number_months = 0
greatest_increase = ["1900",0]
greatest_decrease = ["1900",999999999999999999999999999999999999]
#define as a string
#date_increase = ""
#date_decrease = ""

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
    #previous_format_net = "${:}".format(previous_net)

        # Read each row of data after the header
    for row in csvreader:
        #start on row 3 so can subtract from above
        total_months = total_months + 1 #4
        
        total_profit += int(row[1]) #867884 + 984655 + 322013 + -69417
        #total_format_profit = "${:,.0f}".format(total_profit)
        total_format_profit = "${:}".format(total_profit)
#print(total_format_profit)
        net_profit_change = int(row[1]) - previous_net 
        #net_format_profit_change = "${:}".format(net_profit_change)
#print(net_format_profit_change)
        changes_in_profit.append (net_profit_change) #[116771, -662642, -391430]
#print(changes_in_profit)
        previous_net = int(row[1])

        if net_profit_change > greatest_increase[1]:  #["1900", 0]
            greatest_increase[0] = row[0] #[Feb-10, 0]
            greatest_increase[1] = net_profit_change #[Feb-10,116771]
        
        if net_profit_change < greatest_decrease[1]:  #["1900",999999999999999999999999999999999999]
            greatest_decrease[0] = row[0] #[Feb-10, 0]
            greatest_decrease[1] = net_profit_change #[Feb-10,116771]

print(greatest_increase)

print ("Financial Analysis")
print ("-----------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_format_profit}")
print(f"Average Change: ${round(avg_changes, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")
#print(f"Average Change: ${round(avg_changes, 2)}")