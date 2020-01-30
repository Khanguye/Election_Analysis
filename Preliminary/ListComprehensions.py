# Create a list that prompts the user for the names of five people they know.
# Run the provided program. Note that nothing forces you to write the name "properly"—e.g., as "Jane" instead of "jAnE". You will use list comprehensions to fix this.
# First, use list comprehensions to create a new list that contains the lowercase version of each of the names your user provided.
# Then, use list comprehensions to create a new list that contains the title-cased and swap-cased versions of each of the names in your lower-cased list.
print(dir(str))
li = ["ReBBecca VERges","SheRYll MCgrew ","JoDY Guadarrama","JIMMie Curtsinger","eLKe capLInger "]
print(li)

li_low = [name.lower() for name in li]
print("Lower Case:\n",li_low)

li_title = [name.title() for name in li_low]
print("Title Case:\n",li_title)

li_swapcase = [name.swapcase() for name in li_title]
print("Swap Case:\n",li_swapcase)

