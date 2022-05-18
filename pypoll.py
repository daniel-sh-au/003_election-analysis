# The data we need to retrieve.
# 1. The total num of votes cast
# 2. A compelte list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# The winner of the elction basec on popular vote

# dependencies
import os
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# candidate information
total_votes = 0
candidate_options = []
candidate_votes = {}

# winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # header row
    headers = next(file_reader)
    
    # Print each row into 
    for row in file_reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        # only unique candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # intialize candidate vote to 0 after 1st instance of candidate name
            candidate_votes[candidate_name] = 0

        # increment for every vote for candidate_name
        candidate_votes[candidate_name] += 1

#print(f"There are {total_votes} total votes")
#print(candidate_votes)

# find percentage votes
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100

    # find winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}).")

winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)
