#Tuple is immutable type = can not change the size and value
counties = ("Arapahoe","Denver","Jefferson")
print(counties)

#access by positive index from 0
print("counties[0]=",counties[0])
#access by negative index from -1
print("counties[-1]=",counties[-1])
#count elements
print("len(counties)=",len(counties))
#slicing a list index Start and index end without including end index
print("counties[0:2]=",counties[0:2])
print("counties[:2]=",counties[:2])
print("counties[1:]=",counties[1:])

# NOT ALLOW add and remove item in list
# # counties.append("El Paso")
# # print('counties.append("El Paso") list=',counties)
# # counties.remove("El Paso")
# # print('counties.remove("El Paso") list=',counties)
# # counties.insert(2,"El Paso")
# # print('counties.insert(2,"El Paso") list=',counties)
# # #pop the last item if index parameter is none
# # counties.pop(2)
# # print("counties.pop(2) list=",counties)

# NOT ALLOW assign the value at index
# # counties[2] = "El Paso"
# # print('counties[2] = "El Paso" list=',counties)
# # counties[2] = "Jefferson"
# # print('counties[2] = "Jefferson" list=',counties)




