# The data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# an vailable integer (total vote) to hold the counts of each line registered vote
# need List dictionary to hold candidate names and total number of votes {"CanidateName":CanidateVotes}

# open the data file and read each line data in csv (Ballot ID,County,Candidate)
# Skip 1 read line 

# Loop read line to end file
# increase the total vote by each time read line
# Find canidate name from dictionary
# if found then increase the canidate votes by 1
# else insert the new caidate name and vote = 1
# End Loop

# Loop Dictionary
# find percentage of votes = CanidateVotes / total votes of each candidate in dictionary
# keep the max percentage and canidate name
# End Loop

# print out the winner name with the max percentage

#-------------------------
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here. 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        print(row[0])
        break

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
     txt_file.writelines(["Counties in the Election\n","-"*25+"\n"])
     txt_file.write("Arapahoe\n")
     txt_file.write("Denver\n")
     txt_file.write("Jefferson\n")


