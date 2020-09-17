import os
import csv

cwkdir = os.getcwd()
election_data = os.path.join(cwkdir, "Resources", "election_data.csv")

# The total number of votes cast
total_votes = 0

# A complete list of candidates who received votes
candidates = []

# The percentage of votes each candidate won
percent_votes = []

# A list to capture the number of votes each candidate receives
num_votes = []


with open(election_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")



    for row in csvreader:
        
        total_votes += 1 

    
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")