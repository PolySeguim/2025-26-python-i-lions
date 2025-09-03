#def is the keyword to define a function
#whatType is the name of the function
#userInput is the parameter of the function
def whatType(userInput):
    #print is a python built in function that prints to the console
    #type is a python built in function that tells us the data type of the variable or value
    #userInput is the variable that the user enters
    #print is a built in function that outputs to the screen
    print(type(userInput))

# The pound symbol is for one line comments
#The program ignores all comments

"""
multiple line comments 
"""

#Call the function with different user inputs
whatType(3)
whatType(3.0)
whatType(True)
whatType("marya")
whatType("p")



#def is the keyword to define a function
#whatType is the name of the function
#userInput is the parameter of the function
def whatType(userInput):
    #print is a python built in function that prints to the console
    #type is a python built in function that tells us the data type of the variable or value
    #userInput is the variable that the user enters
    #print is a built in function that outputs to the screen
    print(type(userInput))

# The pound symbol is for one line comments
# The program ignores all comments

"""
multiple line comments 
"""

#Call the function with different user inputs

"""
Test SUITE
"""

whatType(3)
whatType(3.0)
whatType("3, 0")
whatType(True)
whatType("marya")
whatType("p")

#create a variable named message 
message = """this is a 
multiline message 
to my bestie."""

print(message)

#test inputs to print and see how they print
print(42000)
#every time you have a comma between values, it will understand as a different paramater input
print(42, "poly", 3, "chem", "conputer")
print(42_000)
print(42000.00)

name = "marya"
newName = "mar"
name = newName
newName = name

print(name)
print(newName)

classof2026 = {"student 1", "student 2"}
seniors = "not a good variable name... why?" 

#MLA formatting for GEEKS
#Global variable for things that cannot change

#In naming variable the variable day <> Day
# We want to use lower case as much as possible...
#for python day_of_the_week
#in java dayOfTheWeek

"""
ILLEGAL VARIABLE NAMES
21yearsold = "party"
dolla$$$$

def = "def"
class = "python"
"""

print(2+2)
print("hello")
print(len("hello"))

print(20+12)
hour = 1
print(hour -1)
print(hour * 60, "minutes in", hour, "hour")

myName ="marya"
print(myName + str(5))

#operations
#addition 
#add numbers or concatenate strings
#subtraction
#to numbers only
#division 
# to numbers only
# - / - division (typical) but the answer is always a float
# - // - floor division (divides to the largest integer) answer in an in 
# - % - modulus operator (finds the remainder of the division) answer is an int
print(10/3) #3.3333
print(10//3) #3
print(10%3) #1
#multiplication
# for numbers and strings 
# - * - multiplies only 
# - ** - exponentiation
print(8*2) #16
print(8**2) #64

print(int(3.14))
print(int("1977"))
print(int(-3.111111))
print(int(-4.6473))
#print(int("marya"))

print(float(1977))
print(float("3.14")) 

print(str(1977))
print(str(3.14))

age = 48
print(type(age))
age = float(age)
print(type(age))

#create a list of new emails

#create a list of names and name studentNames
studentNames = ["Poly", "Ana", "Chris", "Tommy"]
emailAddress = "@ursulineacademy.org"

for student in studentNames:
    #addition between two strings in python is called concatenation
    email = student + emailAddress
    print(email)

#Python allows different data types to be 
#stored side by side in a list
#for example
aList = ["Poly", "Ana", 48, True]
print(aList)

#input function mailing address
userName = input("What is your name? ")
userAddress = input("What is your address? ")
userCity = input("What city do you live in? ")
userState = input("What state do you live in? ")
userZip = input("What is your zip code? ")

print(userName, userAddress, userCity, userState, userZip)



#Calculates the area of a circle 
radius = float(input("What is the radius of the circle?"))
area = 3.14 * radius**2
print("The area of the circle is", area)


#Practice Problem
P = 10000
n = 12
r = 0.08
t = float(input("How many years will the money be compounded? "))
A = P * (1 + r/n)**(n*t)
print("The final amount after", t, "years is $", A)

# THIS IS A TEST, YOU CAN DELETE THIS COMMENT

