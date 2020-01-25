print("Arapahoe and Denver are not in the list of counties.")

interest = 3000
print("Your interest for the year is $" + str(interest))

print("You","are","awesome")

my_votes = 3000
total_votes = 5000
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

candidate_votes = 3000
total_votes = 5000
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


print(f'{2.325:10.2f}')
print(f'{20000.323235:10,.2f}')