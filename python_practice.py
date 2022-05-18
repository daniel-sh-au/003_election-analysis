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
# counties_dict["Arapahoe"] = 422829, counties_dict["Denver"] = 463353, counties_dict["Jefferson"] = 432438
# dict.keys and dict.values
# list of dictionaries

# Ex. User input and if/elif/else statements
# What is the score?
#score = int(input("What is your test score? "))
# Determine the grade.
#if score >= 90:
#    print('Your grade is an A.')
#elif score >= 80:
#    print('Your grade is a B.')
#elif score >= 70:
#    print('Your grade is a C.')
#elif score >= 60:
#    print('Your grade is a D.')
#else:
#    print('Your grade is an F.')

# Ex. List of Dictionary and for loop
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]
#for county_dict in voting_data:
#    print(county_dict['county'])
#    for value in county_dict.values():
#        print(value)

# Ex. Print() and f-string
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.") 
#    is equal to...
#    print(f"{county} county has {voters} registered voters.")
# \n for newline

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
#                {"county":"Denver", "registered_voters": 463353}, 
#                {"county":"Jefferson", "registered_voters": 432438}]
#for county_dict in voting_data:
#    print(str(county_dict['county']) + " county has " + str(county_dict['registered_voters']) + " registered voters.")
#    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,.2f} registered voters."")

# Ex. datetime
#import datetime as dt
#now = dt.datetime.now()
#print(now)

# Ex. csv
#import csv
#dir(csv)
#print("this is a dir")