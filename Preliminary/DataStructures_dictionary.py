#Dictionary is key value pair
#empty dictionary
counties={}
counties["Arapahoe"] = 422829
counties["Denver"] = 463353
counties["Jefferson"] = 432438
print(counties)
#initilize dictionary
counties = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
print(counties)

#access by key
print('counties["Arapahoe"]=',counties["Arapahoe"])
print('counties.get("Arapahoe")=',counties.get("Arapahoe"))
#count elements
print("len(counties)=",len(counties))
#list of key value pair turple
print("counties.items()=",counties.items())
#list of keys
print("counties.items()=",counties.keys())
#list of values
print("counties.items()=",counties.values())

#Lists of Dictionaries
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
voting_data.insert(2,{"county":"El Paso", "registered_voters": 500235})
print(voting_data)
voting_data.remove({"county":"El Paso", "registered_voters": 500235})
print(voting_data)
voting_data.insert(2,{"county":"El Paso", "registered_voters": 500235})
print(voting_data)
voting_data.pop(2)
print(voting_data)




