import os
import csv

budget_path = os.path.join("Resources", "budget_data.csv")

with open(budget_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csvfile)
        
    print(f"Header: {csv_header}")

    # Priming the variables we will be using
    entries = 0
    bud_sum = 0
    maxinc = 0
    maxdec = 0

    for row in csv_reader:
        # Tracking the number of months
        entries = entries + 1
        # Creating a sum for the budget
        bud_sum = bud_sum + float(row[1])

        if int(row[1]) > int(maxinc):
            maxinc = row[1]
            incdate = row[0]

        if int(row[1]) < int(maxdec):
            maxdec = row[1]
            decdate = row[0]

    avg_change = bud_sum / entries
    
    # Printing to bash

    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {entries}")
    print(f"Total: ${round(bud_sum)}")
    print(f"Average Change: ${round(avg_change, 2)}")
    print(f"Greatest Increase in Profits: {incdate} (${maxinc})")
    print(f"Greatest Decrease in Profits: {decdate} (${maxdec})")

    # Printing to txt file
    text = open("PyBank.txt","w+")
    text.write("Financial Analysis\n")
    text.write("---------------------------\n")
    text.write(f"Total Months: {entries}\n")
    text.write(f"Total: ${round(bud_sum)}\n")
    text.write(f"Average Change: ${round(avg_change, 2)}\n")
    text.write(f"Greatest Increase in Profits: {incdate} (${maxinc})\n")
    text.write(f"Greatest Decrease in Profits: {decdate} (${maxdec})\n")