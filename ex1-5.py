
"""
Exercise 1:  Mailing Address
Create a program that displays your name and complete mailing 
address formatted in the manner that you would usually see it 
on the outside of an envelope.  Your program does not need to 
read any input from the user.  (9 lines)
"""
def mailingAddress():
    #create variables for all the information 
    name = input("What is your name? ")
    #address
    #city
    #state
    #zip
    address = input("What is your address?")
    city = input("What is your city?")
    state = input("What is your state?")
    zip = input("What is your zip?")
    print(name)
    print(address)
    print(city,",", state, zip)
"""
Exercise 2:  Hello
Write a program that asks the user to enter his or her name.  
The program should respond with a message that says hello to 
the user, using his or her name.  (9 lines)
"""
def HelloName():
    name = input("What is your name?")
    print("hello", name)

"""
Exercise 3:  Area of a Room
Write a program that asks the user to enter the width and 
length or a room. Once the values have been read, your 
program should compute and display the area of the room.  
The length and the width will be entered as floating point 
numbers.  Include units in your prompt and output message;  
either feet or meters, depending on which unit you are more 
comfortable working with.  (13 lines)
"""

"""
def AreaRoom():
    print("area of room")
    units = input("what units are you using? feet or meter:")
    width = float(input("width:"))
    length = float(input("length:"))
    AreaOfRoom = width*length
    print(AreaOfRoom, units)
"""

"""
Exercise 4:  Area of a Field
Create a program that reads the length and width of a 
farmer’s field from the user in feet.  Display the 
area of the field in acres.  
Hint: There are 43,560 square feet in an acre
"""
"""
def FarmersField():
    print("area of a farmer's field")
    width = float(input("width:"))
    length = float(input("length:"))
    AreaOfField = width*length/43560
    print("the are of the farmers field is", AreaOfField, "acres")

FarmersField();    
"""

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


def Refund():
    TenCentDeposits = int(input("how many bottles are less than or equal to 1 liter?"))
    TwentyFiveCentDeposits = int(input("how many bottles are more than 1 liter?"))
    OneLiterOrLessBottles = float(TenCentDeposits*0.10)
    MoreThanOneLiterBottles = float(TwentyFiveCentDeposits*0.25)
    RefundPrice = OneLiterOrLessBottles+MoreThanOneLiterBottles
    RefundPrice = round(RefundPrice, 2)
    print("your refund will be","$","{:.2f}" .format(RefundPrice))
Refund()







    # To ensure we have two decimal places
    # number_two_decimal = "{:.2f}".format(number_string)
    # print(number_two_decimal)
