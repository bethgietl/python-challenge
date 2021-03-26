# python-challenge

1. created a repository on github called python-challenge
2. made a clone on my PC
---used gitbash / terminal to cd and ls my way around to find where I wanted to make the clone
---used git clone link in the python-challenge
3. using bash created the necessary folders and files and nested them in the python-challenge folder
----mkrdir for creating the PyBank PyPoll folders and inside those folders created Analysis and Resources folders
----touch for creating the main.py python and analysis.txt text files for each homework assignment
4. pushed changes to the repo on github
---cd to python-challenge folder
---git status (new things added/updated are red)
---git add .
---git status (new things added/updated turn green)
---git commit -m "made a comment"
---git push

#PyBank 
1. read the instructions throughly and tried to take one step at a time
2. added the instructions to the visual studio file for easy reference
3. started with dependencies - have to have these in order to create file paths
---used Activity 03-Python.08.read_csv.py
------import the os module = this allows to create file paths across operating systems
---import os
-------module for reading CSV files
---import csv
4. created the file path for the csv file and created the text path as well since that was the last step of the homework's instructions
----used Activity 03-Python.08.read_csv.py
---csvpath = os.pathjoin("Resource", "budget_analysis.csv")
---txtpath = os.path.join("Analysis", "Financial_Analysis.txt")
5. Set the variables, I started with total months so the first variable I set was total_months and added to the variable list as I moved down the instructions
---Used Homework 2.9-Netflix to start the loop
    #Set Variables [] empty lists and helps to append


#PyPoll

##To count the number of voters I used the len function
---used Activity 03-Python.09.lists.py

##To find the candidate witht the most votes and call him the winner I used a nested if/elif statement
---used Activity 03-Python.07.conditionals.py
---if (Khan) > (Correy) > (Li) > (O'Tooley): 
      Winner = "Khan"
   elif (Correy) > (Khan) > ....
      Winner = "Correy"
   else (O'Tooley) > ....
      Winner = "O'Tooley"
      
   
