# def is the keyword to define a function 
#what type is the name of the function
# userInput is the parameter of the function 
def whatType(userInput):
    print(type(userInput))
    # print is a Python built-in fuction that prints to the console 
    # type is a Python-built in function that finds the data type 
    # userInput is the variable that the user enters 
    print(type(userInput))
# the pound symbol is for one line comments
# the program ignores all comments 
"""
multiple line comments 
"""
#Call the function with different inputs 
#If you dont call the functions, nothing will run in the program 


"""
Test SUITE
"""
whatType(3)
whatType(3.0)
whatType("3.0")
whatType(True)
whatType("Alice")
whatType('p')

#create a variable named message 
message = """this is a 
multiline message 
to my bestie."""
print(message)

#test inputs to print and see how they print 
print(42000)
#every time you have a comma between values, it will understand it as a different 
#parameter input 
print(42, "poly", 3, "chem", "computer")
print(42000)
print(42,000)


name = "polyana"
newName = "poly"
name = newName
newName = name 


print(name)
print(newName)


classOf2026 = ("Student 1", "Student 2")
#seinors = not a good variable and name because it is not specific 


#MLA formatting for GEEKS
#Global varibale for things that can not change 

#In naming varibale the variable day <> Day 
#we want to use lower case as much as possible
#for Python day_of_the_week
#in Java dayOfTheWeek 

"""
ILLEGAL VARIABLE NAMES!
21yeasold ="party!"
dolla$$$$
def = "def"
class = python 
"""

"""
Some kinds of statements are:
-While statements 
-for statements 
-import statements 
-if statemnts 
-and so on...
"""
print(2+2)
print("hello")
print(len("hello"))
#len will give you the length of the keyword 

print(20+12)
hour = 1
print(hour - 1)
print(hour * 60, "minutes in", hour, "hour")

myName = "alice" 
print(myName * 5)
# str is casting the integer date type to a string 
# so you can cocatenate (add) two strings together 
print(myName + str(5))

#Operations
# Addition 
#  add numbers or concatenate string 
# Subtraction
#  to numbers only 
# Division 
#  numbers only 
#  -/- division (typical) but the answer is always a float 
#  -//- floor division (divides to the largest integer) answer in an int 
#  -%- modulous operator (finds the remainder of the division) answer is an int 
print(10/3) #3.333333
print(10//3) #3
print(10%3) #1
# multipication 
#  for numbers and strings 
#  -*- multiplies only 
#  -**- 
print(8*2)
print(8**2)

#always round down 
print(int(3.14))
print(int("1977"))
print(int(-4.11212132))
print(int(-4.9999))
#print(int("Alice")) will not work "alice" is not a number 
    

print(float(1977))
print(float(3.1415))

print(str(1977))
print(str(3.0))
