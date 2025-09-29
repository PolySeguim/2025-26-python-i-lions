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
#create a variable named message
message = """this is a mutli line message
to my bestie"""
print(message)
print(42000)
print(42,000)
print(42,000)
#every time you have a comma it will understand as a different
#parameter input
print(42,"poly",3,"chem","computer")
name = "lucy"
newName = "lkrebs"
name = newName
newName = name
print(name)
print(newName)
classof2026 = {"student 1", "student 2"}
seniors = "not a good variable"
print(classof2026)
#MLA formatting for GEEKS
#global variable for things that cannot change
"""
global JANUARY = "January"
"""

#in naming vairable the variable day does not equal the vairable day
#we want to use lower case as much as possible
#for python day_of_the_week
#in java dayOfTheWeek
"""
illegal variable names
21yearsold = "party!"
dolla$$$$$
def = "def"
class = "python"
"""
print(2+2)
print(len("hello"))
print(20+12)
hour = 1
print(hour - 1)
print(hour * 60, "minutes in", hour, "hour")
myName = "lucy"
print(myName * 5)
print(myName + str(5))
#str is casting the integer data type to a string
#so you can concatenate (add) two strings together
"""
lkrebs2026
"""
#operations
#addition
# add numbers or concatenate string
#subtraction
# to numbers only
#division
# to numbers only
# - / - division (typical) but the answer is always a float
# - // - floor division (divides to the largest interfer) answer in an int
# - % - modules operator (finds the remainder of the divsision) answer is an int

print(10/3) #3.333333335
print(10//3) #3
print(10%3) #1

#multiplication
# for numbers and strings only
# - * - multiplication
# - ** - exponentiation

print(8*2) #16
print(8**2) #64
print(int(3.14))
print(int("1977"))
print(int(3.9999))

print(float(1977))
print(float(3.1415))

#create a list of new emails

#create a list of names and name studentNames

#python allows different data types to be stored side by side in a list
#for example:
alist = ("Poly", "Anna", 48, 3.0, True)
alist = (studentNames) = ["lucy", "marya", "anna", "poly"]
emailAddress = "@ursulineacademy.org"

for student in studentNames:
     #addition between two strings is concatenation
    email = student + emailAddress
    print(email)

#input function
userName = input("What is your name?")
userAddress = input ("What is your address?")
userCity = input("What is your city?")
userZip = input("What is your zip code?")

print(userName, userAddress, userCity, userZip)

"""
# Calculate the area of a circle
diameter = float(input("Diameter: "))
print(type(diameter))

"
area = (diameter/2)**2*3.14
print("area of your circle is", area)
"""
#compound interest formula
P=100000
n=12
r=0.08
t = float(input("how many year will money be compounded?"))
A = P * (1 + r/n)**(n*t)
print("finalamount after t years", A)






