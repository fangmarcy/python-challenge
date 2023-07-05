import os
import csv

pypollpath = os.path.join("C:\\Users\\dtrob\\repos\\Challenges\\Challenge 3\\python-challenge\\PyPoll\\Resources\\election_data.csv")

found = False

# Initializing of variables
total_votes = 0
# Create a dictionary to store the votes for each candidate
candidate_votes = {}

# Open the CSV file and read the data
with open(pypollpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment the total_votes counter for each row
        total_votes += 1
        # Get the candidate names
        candidate_name = row[2]

        # Check if the candidate already exists in the dictionary
        if candidate_name in candidate_votes:
            # If the candidate name exists, increment their vote count by 1
            candidate_votes[candidate_name] += 1
        else:
            # If the candidate is new, add them to the dictionary
            candidate_votes[candidate_name] = 1

print("Total Votes:", total_votes)

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(candidate + ":", votes, "(", round(percentage, 2), "%)")

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

print("Winner:", winner)


# Prepare the content to be written to the output file
output_content = f"Election Results\n"
output_content += f"----------------------------\n"
output_content += f"Total Votes: {total_votes}\n"
output_content += f"----------------------------\n"
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    output_content += f"{candidate}: {votes} ({round(percentage, 2)}%)\n"
output_content += f"----------------------------\n"
output_content += f"Winner: {winner})\n"

# Specify the output file name
output_file = "election_results.txt"

# Write the content to the output file
with open(output_file, 'w') as file:
    file.write(output_content)

print("Election Results exported to", output_file)
