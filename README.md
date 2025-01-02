# python-challenge
Module 3 challenge - create python scripts to analyze financial records for a company and to modernize a vote-counting process
ChatGPT corrected Code for PyBank:
1. Handling of the Greatest Increase and Decrease in Profits; initially I set the values to "date" which is a string when it was supposed to be integers so thats how I got
greatest_increase = float('-inf')
greatest_decrease = float('inf)
2. Tracking Net Total Profit and Loss; I had set variables which were not being utilized so ChatGPT suggested changes to the variables to be more clear
3. Calculating the Total_Value; ChatGPT helped me convert "total_value = data[1]" to an integer by using "total_value = int(data[1])
4. Corrected string formatting in my print and write statements
5. changed "greatest_increase_month" and "greatest_decrease_month" from " = date" to unassigned variable. Fix: greatest_increase_month = ""
6. added a new line to the txt_file.write function by adding (\n)
