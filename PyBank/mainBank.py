#Your task is to create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

import os
import csv

total = 0
#positive change
profit_change = []
date_change = []
avg_change = 0
profit_loss = 0
number_months = 0
greatest_incrase = 0
greatest_decrease = 0
#define as a string
date_increase = ""
date_decrease = ""

#set a path for the csv and txt files, will print the text file when all said and done
csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("Analysis", "Financial_Analysis.txt")

#Use csvreader module to read csv file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)
    

    #Find total months: lenlist = length of list
    lines = len(list(csvreader))


    for row in csvreader:
        profit_loss: int
        total += profit_loss
        profit_change.append(profit_loss) 
        date_change.append(row[0])
        number_months += 1

#Find net total $
    for row in csvreader



#Find avg change

#Find greatest increase

#Find greatest decrease 

#Print to terminal

#Print to txt file in Analysis folder

print(Financial Analysis)
print("")
print("---------------------------------")
print("")
# Nested if statements from 1.7 Activity
#if x < 10:
    #if y < 5:
        #print("x is less than 10 and y is less than 5")
    #elif y == 5:
        #print("x is less than 10 and y is equal to 5")
    #else:
        #print("x is less than 10 and y is greater than 5")

    #create a list for each month in the csv file

    #list for profitt loss

    #initial value and varialbe for net total