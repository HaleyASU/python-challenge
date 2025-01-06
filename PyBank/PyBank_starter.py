# -*- coding: UTF-8 -*- 
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_value = 0 
total_net = 0 
average_change = 0 
greatest_increase = float('-inf')
greatest_decrease = float('inf')
greatest_increase_month = ""
greatest_decrease_month = ""
previous_value = 0
changes = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    print(f"CSV Header: {header}")

    # Track the total and net change
    data = next(reader)
    total_value = int(data[1])
    total_months = 1  # Starting count for months
    previous_value = int(data[1])

    # Process each row of data
    for row in reader:
        # Track the months
        total_months += 1

        # Track the total value
        total_value += int(row[1])

        # Calculate the net change for the month
        change = int(row[1]) - previous_value
        changes.append(change)

        # Track the net total 
        total_net += change #possibly try total_net += change if results keep returning incorrectly

        # Calculate the greatest increase in profits (month and amount)
        if change > greatest_increase:
            greatest_increase = change #try = change
            greatest_increase_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease:
            greatest_decrease = change #try = change
            greatest_decrease_month = row[0]

        # Update the previous value for next iteration
        previous_value = int(row[1])

# Calculate the average net change across the months
average_change = sum(changes) / len(changes) if changes else 0

# Print the output
print(f"Financial Analysis")
print(f"-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_value:,.2f}")
print(f"Average Change: ${average_change:,.2f}")
print(f"Greatest Increase In Profits: {greatest_increase_month} / ${greatest_increase:,.2f}")
print(f"Greatest Decrease In Profits: {greatest_decrease_month} / ${greatest_decrease:,.2f}")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"---------------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_value:,.2f}\n")
    txt_file.write(f"Average Change: ${average_change:,.2f}\n")
    txt_file.write(f"Greatest Increase In Profits: {greatest_increase_month} / ${greatest_increase:,.2f}\n")
    txt_file.write(f"Greatest Decrease In Profits: {greatest_decrease_month} / ${greatest_decrease:,.2f}\n")
