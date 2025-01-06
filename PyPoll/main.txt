# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
vote_counts = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        # print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1 

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            vote_counts[candidate_name] = 0 

        # Add a vote to the candidate's count
        vote_counts[candidate_name] += 1 

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    results=(
        f"\n\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes:{total_votes}\n"
        f"---------------------------\n"
    )
    print(results, end="")

    # Write the total vote count to the text file
    txt_file.write(results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in vote_counts:

        # Get the vote count
        votes = vote_counts[candidate_name]

        #calculate the percentage of total votes candidate won
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_candidate = candidate_name
            winning_count = votes

        # Print and save each candidate's vote count and percentage
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n"
        )
        print(candidate_results, end="")

 # Write the candidate's results to the text file
        txt_file.write(candidate_results)

    # Print and save the winning candidate summary
    winning_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------------\n"
    )
    print(winning_summary)
    txt_file.write(winning_summary)