#print("Hello World")
#Notes
# list.append("xx") = add to end
# list.insert(3, "xx") = add to location
# list.remove("xx") = remove first instance of xx
# list.pop(3) or list.pop(-1) = remove from location or remove from end
# list[1], list[2] = list[2], list[1] == swap location in list
# lists - can be changed - list=["a","b","c"]
# Tuple - cannot be changed - tuple=("a","b","c") 
# Dictionary - {"Python": 999999}
# dict.keys and dict.values
# list of dictionaries

# Ex. User input and if/elif/else statements
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')