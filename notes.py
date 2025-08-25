# def is the keyword to define a function
# whatType is the name of the function
# userInput is the parameter of the function
def whatType(userinput):
    #print is a Python built-in function that prints to the console
    # type is a Python built-in function that finds the datatype
    #userinput is the variable that the user enters
    print (type(userinput)) 

# The pound symbol is for one line comments
# The program ignores all comments

""" 
multiple line comments
"""
#Call the function with different user inputs
#is your dont call the function, nothing will run in the program
"""
TEST SUITE
"""
"""
whatType(3)
whatType(3.0)
whatType(True)
whatType("abbymiles")
whatType('a')

#create a variable named message
message = """this is a 
miltiline message
to my bestie."""

print(message)
