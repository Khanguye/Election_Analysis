#(1) The data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# A complete list of counties where votes casted
# Total number of votes each county casted

#(2) The calculated data to save to file and to terminal
# total number of votes
# Percentage of votes each county casted
# The largest county votes casted
# Percentage of votes each candidate won
# The winner of the election based on popular vote
#-------------------------
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate and Votes dictionary
# Initilize the empty dictionary 
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County Name and Votes Dictionary 
# Initilize the empty dictionary 
county_votes = {}

# Langest Vote County Tracker
largest_county_vote = ""
largest_votes = 0

# Open the election results and read the file.
# Calculate the votes results for total_votes, candidate_votes dictionary, and county_votes dictionary
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Skip the first row becuase it is a header 
    headers = next(file_reader)

    # each row is a list with order values: BallotID (index 0) ,County (index 1), and Canidate Value (index 2)
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        # retrive candinate name from row index 2
        candidate_name = row[2]
        # insert new candiate if candidate name is not in a key of the candidate votes dictionary
        if (candidate_name not in candidate_votes.keys()):
            candidate_votes[candidate_name] = 0
        # increase by one vote for candidate name
        candidate_votes[candidate_name] += 1
        
        # retrieve county name from row index 1
        county_name = row[1]
        # insert new county if county name is not a key of the county votes dictionary 
        if (county_name not in county_votes.keys()):
            county_votes[county_name] = 0
        # increase by one vote for county name
        county_votes[county_name] += 1

##print total votes for debug
#print(total_votes)
##print candidate votes for debug
#print(candidate_votes)
##print county votes for debug
#print(county_votes)

# Using the open() function with the "w" mode we will write data to the file.
# Using total_votes, candidate_votes dictionary, and county_votes dictionary to calculate outcomes
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    # To the terminal
    print(election_results, end="")
    # Save to the file
    txt_file.write(election_results)

    # Loop through keys in county_votes
    # Calculate the county vote and percentage
    for county in county_votes:
        # Retrieve the total votes of county
        county_vote_count = county_votes[county] 
        # calculate county vote percentage
        county_vote_percentage = (county_vote_count/total_votes)*100
        # format output string
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        
        # To the terminal
        print(county_results,end="")
        # save to the file
        txt_file.write(county_results)

        # keep track the largest vote county 
        if county_vote_count > largest_votes :
            largest_votes = county_vote_count
            largest_county_vote = county

    # Print the largest county vote
    largest_vote_county_results = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_vote}\n"
        f"-------------------------\n")
    # to the terminal
    print(largest_vote_county_results,end="")
    # save the file
    txt_file.write(largest_vote_county_results)

   
    # Loop through keys in candidate_votes
    # Caculate percent and print out results
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = (votes/total_votes) * 100
        
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results,end="")
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if votes > winning_count :
            # Keep track the max values
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    # print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------")
    # to the terminal
    print(winning_candidate_summary)
    #  Save the winner candidate results to our text file.
    txt_file.write(winning_candidate_summary)




