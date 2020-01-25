# While condition is true, execute the below statements
x = 0
while x <= 5:
    print(x)
    x = x + 1

# For each item in the list or tuple 
counties = ["Arapahoe","Denver","Jefferson"]
#access by item
for county in counties:
    print(county)
#access by item index
for i in range(len(counties)):
    print(counties[i])
#Range generate a list from 0 to end - 1
for i in range(20):
    if (i%3==0):
        print(i)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#default is keys
for county in counties_dict:
    print(county)
#access value
for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))
#access iter by  key  and value
for key,value in counties_dict.items():
    print(f"{key}:{value}")

for county,registers in counties_dict.items():
    print(f"{county} county has {registers} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
        print(county_dict["county"])


