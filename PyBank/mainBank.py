#Your task is to create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period


import os
import csv
#set a path for the csv file
csvpath = os.path.join("Resources", "budget_data.csv")
#Use csvreader module to read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter="")
    print("Financial Analysis:")
    print("---------------------------------")

    #create a list for each month in the csv file

    #list for profitt loss

    #initial value and varialbe for net total