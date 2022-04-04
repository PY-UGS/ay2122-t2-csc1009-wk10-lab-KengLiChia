#Create another Python project, repeat the Question 2b and 2c from Laboratory Wk01.

#question lab1 2b
moduleCode = input("Please enter module code: ") #ask for module code

if (moduleCode == "CSC1006"):
    print("Mathematics 2")
elif (moduleCode == "CSC1007"):
    print("Operating Systems")
elif (moduleCode == "CSC1008"):
    print("Data Structures and Algorithms")
elif (moduleCode == "CSC1009"):
    print("Object-Oriented Programming") #when input CSC1009; OOP
elif (moduleCode == "CSC2902"):
    print("Career and Professional Development")
else:
    print("Invalid Module Code") #when key in invalid module code

#question lab1 2c
print("Descending odd numbers from 102 to 66:")

for i in range(102, 65, -1): # creates iterable from 102 to 66
    if (i % 2 == 1): # checks if i is an odd number
         print(i,end=" ") #print out i in one single line