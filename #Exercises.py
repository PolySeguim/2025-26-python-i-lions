#Exercises 
#Exercise 1
print("Megan Bailey")
print("1250 Timbe Ridge Ct.")
print("Batavia, OH")
print("45103")

#Exercise 2 
#Write a program that asks the user to enter his or her name.
# The program should respond with a message that says hello to
# the user, using his or her name.
print("Hello")
userName = input("What is your name? ")
print("Hello " + userName)
#Exercise 3 
#Write a program that asks the user to enter the width and length or a room.  Once the values have been read, your program should compute and display the area of the room.  
# The length and the width will be entered as floating point 
# numbers.  Include units in your prompt and output message;  
# either feet or meters, depending on which unit you are more 
# comfortable working with.  (13 lines)

print("Hello")
width = float(input("What is the width in feet? "))
length = float(input("What is the length in feet? "))
area = width * length
print(area)

#Excersize 4
# Exercise 4:  Area of a Field
# Create a program that reads the length and width of a 
# farmer’s field from the user in feet.  Display the 
# area of the field in acres.  
# Hint: There are 43,560 square feet in an acre

length = float(input("What is the length of the field in feet? "))
width = float(input("What is the width of the field in feet? "))
area = (length * width)/ 43560
print(area)

"""
Exercise 5:  Bottle Deposits
In many jurisdictions a small deposit is added to drink 
containers to encourage people to recycle them.  In one 
particular jurisdiction, drink containers holding one liter 
or less have a $0.10 deposit, and drink containers holding 
more than one liter have $0.25 deposit.
Write a program that reads the number of containers of each 
size from the user.  Your program should continue by computing 
and displaying the refund that will be received for returning 
those containers.  Format the output so that it includes a dollar 
sign and always displays exactly two decimal places.  (15 lines)
"""
howmanyliterbottles = float(input("How many liter bottles do you have? "))
howmanybiggerliter = float(input("How many bottles that are more than one liter do you have? "))
dollarfromliterbottles = howmanyliterbottles * .10
dollarfrombigger = howmanybiggerliter * .25
refund = dollarfromliterbottles + dollarfrombigger 
print("$" + str(refund)) 

"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of  the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""
mealcost = int(input("What is the cost of your meal?"))
taxrate = 0.067
tip = 0.18
mealtax = 0 
mealtax = mealcost * taxrate 
mealtip = 0
mealtip = mealcost * tip
totalcost = 0
totalcost = mealtax + mealtip + mealcost
print(totalcost)

"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""
n = int(input("Write a positive integer "))
sum = (n*(n+1))/2
print("Here's the sum" + str(sum)) 
"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)

"""
widgetweight = 75 
gizmoweight = 112
howmanywidgets = int(input("How many widgets do you have? "))
howmanygizmos = int(input("How many gizmos do you have? "))
totalweight = (widgetweight * howmanywidgets) + (gizmoweight * howmanygizmos)
print("The total weight is " + str(totalweight) + " grams")


"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""
interest = 0.04
balance = int(input("What is your bank balance? "))
print(balance)


