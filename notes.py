#def is the keyword the define a function
#whatType is the name of the function
#userInput is the parameter of the function
def whatType(userInput):
    print(type(userInput))
    #print is a Python built-in function that prints to the console
    #type is a Python built-in function that finds the datatype
    #The program ignores all comments
    #userInput is a variable that the user enters
    #The pound symbol is for one line comments
    """For one multiple line comments"""
    #Call the function with different user inputs


"""Test Suite """

whatType(3)
whatType(3.0)
whatType(True)
whatType("polyana")
whatType('p')

#Create a message named message
message = """this is a 
multiline message 
to my bestie."""

print(message)

#test inputs to print and see how they print
print(42000)
#every time you have a comma between values, it will understand as a different
#parameter input
print(42,"poly",3,"chem","computer")
print(42,000)


"""
name = "polyana"
newName = "poly"
name = newName
newName = name

print(name)

#MLS formatting for geeks
#Global variable for things that cannot change

#In naming variable the variable day does NOT equal the variable the variable Day
#We want to use lower case as much as possible
#For Python day_of_the_week
#In Java dayOfTheWeek


ILLEGAL FUNCTIONS

21yearsold = "party!"
dolla$$$$
def = "def"
class = "python"


print(2+2)
print("hello")
print(len("hello"))

print(20+12)
hour = 1
print (hour - 1)
print(hour * 60, " minutes in ", hour, "hour")

myName = "poly"
print(myName * 5)
#str is casting the integer data type to a string
#so you can can concancate (add) two strings together
print(myName + str(5))

#Operation
#Addition
#add numbers or concatenate string
#Subtraction
#to numbers only
#Division
#numbers only...
# - / - division
# - // - floor division
# - % - modulus operator
print(10/3) #3.3333333333333335
print(10//3) #3
print(10%3) #1
#Multiplication
#for numbers and strings 
# - * - multiples only
# - ** - exponents only
print(8*2)
print(8**2)

print(int(3.14))
print(int(3.99999999))
print(int(-4.11212132))
print(int(-4.9999999))
print(int("1977"))
#print(int("polyana"))

print(float(1977))
print(float(3.1415))

print(str(1977))


#input function
userName = input("What is your name? ")
userAddress = input("What is your address? ")
userCity = input("What is your city? ")
userZip = input("What is your zip code? ")

print(userName, userAddress, userCity, userZip)

"""

"""def calculatePrincipal():
    principal = float(input("Principal:"))

    n = 12
    r = 0.08

    print(r/n)
    print(1 + r/n)**(n*t)"""


#Number 1
print("Abigail Molloy \n 9557 Semaphore Court \n West Chester, Ohio, 45069")

#Number 2
"""
userName = input("What is your name? ")
print("Hello", userName)
"""

#Number 3
"""
units = input("what units are you using, feet or meters? ")
width = float (input("What is the room's width? "))
length = float (input("What is the room's length "))
area = width * length
print("Area of the room is ", str(area), units, "squared")
"""

#Number 4
"""
width = float (input("What is the farm width in feet? "))
length = float (input("What is the farm length in feet? "))
area = (width * length)/43560
print("The field is", area, "acres")
"""

#Number 5
"""
def bottleDeposits():
    numOneLiterBottles = int (input("Number of one liter bottles? "))
    numMoreOneLiterBottles = int (input("Number of more than one liter bottles? "))
    refund = numMoreOneLiterBottles * 0.25 + numOneLiterBottles * 0.1
    print("Your refund will be", refund)
bottleDeposits();
"""

#Number 6
