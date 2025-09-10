#new notes


age = 48
print(type(age))
age = float(age)
print(type(age))

#create a list of new emails 
#create a list of names and name studentNames
studentNames = ["Poly" , "Ana" , "Chris" , "Tommy"]
emailAddress = "@ursulineacademy.org"
for student in studentNames:
    email = student + emailAddress
    print(email)

#input function
userName = input("What is your name? ")
userAddress = input("What is your address? ")
userCity = input("What is your city? ")
userZip = input("What is your zip code? ")

print(userName, userAddress, userCity, userZip)

#Calculates the area of a circle
circleRadius = input("what is the radius? ")
circleRadius = float(circleRadius)
circleArea = 3.14 * circleRadius * circleRadius
print(circleArea)

n = float(12.0)
r = float(.08)
P = float(10000)
t = input("Number of years? ")
a = P*(1+ r/n) **(n*t)
print(a)

