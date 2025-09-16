# def is the keyword to define a function
# whatType is the name of the function
# userInput is the parameter of the function
def whatType(userInput):
    # print is a Python built-in function that prints to the console
    # type is a Python built-in function that finds the datatype
    # userInput is the variable that the user enters
    print(type(userInput))

# The pound symbol is for one line comments
# The program ignores all commments

"""
multiple lines comments
"""
# Call the function with different user inputs
# If you don't call the function, nothing will run in the program

"""
Test SUITE
"""

whatType(3)
whatType(3.0)
whatType("3.0")
whatType(True)
whatType("Wubi")
whatType('W')


#Create a variable named message
message = """this is a
multiline message
to my bestie."""
print(message)

#test inputs to print and see how they print
print(42000)
#every time you have a comma between values, it will understand as a different
#parameter input
print(42,"Wubi",3,"chem","computer")
print(42,000)
print(42.000)

name = "Wubi"
newName = "poly"
name = newName
newName = name

print(name)
print(newName)

classOf2026 = ["Student 1", "Student 2"]
seniors = "not a good variable name...  why???"

# MLS formatting for GEEKS
#Global variable for things that cannot change

# In naming variable the variable day <> Day
# we want to use lower case as much as possible...
# for Python day_of_the_week
# in Java dayOfTheWeek

"""
ILLEGAL VARIABLE NAMES!
21yearsold = "party!"
dolla$$$$

def = "def"
class = "python"
"""

print(20+12)
hour = 3
print(hour - 1)
print(hour * 60, " minutes in ", hour, " hour")

myName = "poly"
print(myName * 5)
# str is casting the integer data type to a string
# so you can concatenate (add) two strings together
print(myName + str(5))

#Operations
# Addition
#   add numbers or concatenate string
# Subtraction
#   to numbers only
# Division
#   numbers only... 
#   - / - division (typical) but the answer is always a float
#   - // - floor division (divides to the largest integer) answer is an int
#   - % - modulus operator (finds the remainder of the division) answer is an int
print(10/3)  #3.3333333333333335
print(10//3) #3
print(10%3)  #1
# Multiplication
#   for numbers and strings
#   - * - multiplies only
#   - ** - exponential
print(8*2)
print(8**2)

print(int(3.14))
print(int(3.99999))
print(int(-4.11212132))
print(int(-4.99999))
print(int("1977"))
#print(int("Wubi"))


print(float(1977))
print(float(3.1415))

print(str(1977))
print(str(3.0))

age = 15
print(type(age))
age = float(age)
print(type(age))

#Create a list of new emails
#Python allows different data types to be
# stored side by side in a list
#For example:
aList = ["She", "Saw", "Seashells", "Seashore"]
emailAdress = "@ursulineacademy.org"

for student in aList:
    # addition between two strings in concatenation
    email = student+emailAdress 
    print(email)
    
#input fuction
userName = input("What is your name? ")
userAdress = input("What is your adress? ")
userCity = input("What is your city? ")
userZip = input("What is your zip code? ")

print(userName,userAdress,userCity,userZip)
"""
#computing amount if one is given compound interest
#Classroom Exercise
# A = P*(1+r/n)**(n*t)

def calculatorPrinciple():
    principal = float(input("Enter the initial principal amount: "))
    r = 0.08 
    n = 12
    t = float(input("Time: "))

    amount = principal * (1 + (r/n))**(n*t)
    print("Total Accumulated", amount)
    
    calculatorPrinciple()

 #Mailing adress exercise

def mailingAdress():
    Name = input("What is your Name?")
    StreetAddress = input("What is your StreetAddress?")
    City = input("What is your City?")
    State = input("What is your State?")
    ZipCode = input("What is your zip code?")
    print(Name)
    print(StreetAddress)
    print(City , State , ZipCode)

#mailingAdress()


def bottleDeposists():
       # reads the number of bottles
       numOneLiterBottle = input("Number of 1L bottles: ")
       numMoreOneLiterBottle = input("Number of more than 1L Bottles : ")
       refund = numMoreOneLiterBottle*0.25+numOneLiterBottle*0.1
       print("Your refund will be: $", refund)
       # adding everything less than 1
       # adding everything greater than 1

#bottleDeposists()
"""