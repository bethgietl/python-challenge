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

        # Read each row of data after the header
    for row in csvreader:
        #start on row 3 so can subtract from above
        total_months = total_months + 1 #4
        
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
print(f"Greatest Increase in Profits: ${max(greatest_increase)}")
print(f"Greatest Decrease in Profits: ${min(greatest_decrease)}")

#print(avg_changes)
#print(greatest_decrease)
#print(greatest_increase)




#print(total_months)      
#print(total_profit)
#print(changes_in_profit)   
#print(min(changes_in_profit))   
#print(max(changes_in_profit))

        
        #date.append(row[0])
    
     #in this loop I did total of difference between all row of column "Profit/Losses" and found total PL change. Also found out max PL change and min PL change. 
     #for i in range(len(changes_in_profit)-1):
        #total_changes += changes_in_profit[i]
        #total_changes.append(changes_in_profit[i] - changes_in_profit[i-1])   
        #avg_changes = total_changes / len(changes_in_profit)

   
        
        #avg_changes = round(total_profit / total_months, 2)

        #change_in_profit.append(profit_losses) 
        #change_in_profit.append(row[0])
        #number_months += 1   

            # Determine percent of review left to 2 decimal places
        #percent = round(int(row[6]) / int(row[5]), 2)
        #review_percent.append(percent)       


#print ("Financial Analysis")
#print ("-----------------------------------------------")
#print(f"Total Months: {total_months}")
#print(f"Total: ${total_pl}")
#print(f"Average Change: ${avg_changes}")
#print(f"Greatest Increase in Profits: ${greatest_incrase}")
#print(f"Greatest Decrease in Profits: ${greatest_decrease}")
    