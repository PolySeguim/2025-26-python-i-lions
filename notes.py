# def is the keyword to define a function
# whatType is the name of the function
# userinput is the parameter of the function
def whatType(userinput):
    #print is a Python built-in function that prints to the console
    # type is a Python built-in function that finds the datatype
    #
    print (type(userinput)) 

# The pound symbol is for one line comments
# The program ignores all comments

""" 
multiple line comments
"""
#Call the function with different user inputs
whatType(3)
whatType(3.0)
whatType(True)
whatType("abbymiles")
whatType('a')
