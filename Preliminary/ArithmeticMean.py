import statistics 
print(dir(statistics))
list_1 = [1,2,3,4,5,6,7,8,9,0]
list_2 = [12,435,34,567,4,56,3,245,3,7,45,5]

print("Mean",statistics.mean(list_1))
print("PStdev",statistics.pstdev(list_1))
print("median",statistics.median(list_1))
print("Q1",statistics.median_low(list_1))
print("Q3",statistics.median_high(list_1))
print("IQR",statistics.median_high(list_1) - statistics.median_low(list_1))
print("-"*30)
print("Mean",statistics.mean(list_2))
print("PStdev",statistics.pstdev(list_2))
print("median",statistics.median(list_2))
print("Q1",statistics.median_low(list_2))
print("Q3",statistics.median_high(list_2))
print("IQR",statistics.median_high(list_2) - statistics.median_low(list_2))


def mean(a_list):
    return sum(a_list)/len(a_list)

print(mean(list_1))
print(mean(list_2))


