name = "Kristopher"
print(name)
country = "Peru"
print(country)
age = 32
print(age)
hourly_wage = 165
print(hourly_wage)
satisfied = True
print(satisfied)
daily_wage = hourly_wage*8
print(daily_wage)
str_result = name + ":" + country + ":" + str(age) + ":" + str(hourly_wage)
print(str_result)
fstr_result = f"{daily_wage}:{satisfied}"
print(fstr_result)

grocery = ["milk","eggs","Jelly","peanut butter"]
print(grocery)
grocery[3]= "almond butter"
print(grocery)
grocery.pop(2)
print(grocery)
grocery.append("coffee")
print(grocery)

dict_yourseft = {"name":"Kristopher", "age": 32, "hobbies": ["craft","paint","running"], "wake up": {"monday":"8:00","tuesday":"8:30","wednesday":"6:30"}}
print(dict_yourseft["name"])
print(f"total hobbies is {len(dict_yourseft['hobbies'])}")
print(f"Wednesday alarm at {dict_yourseft['wake up']['wednesday']}")

x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")

