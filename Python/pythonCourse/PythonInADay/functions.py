## Python example of a function
## def someFunction(< input variables >):
##         < do stuff here with input variables >
##         return < some value >

someOtherValue = 5

def letsAdd(x,y):
    addition = x + y
    someValue = 10
    return addition

print letsAdd(3,5)
# print someValue # won't print because the variable, someValue doesn't exist outside the function; local variable
print someOtherValue # the variable works because it is global, not local

def subtraction(x,y):
    subtract = x - y
    return subtract

print subtraction(10,4)

def moreSubtraction(x,y,z):
    subtract = x - y - z
    return subtract

print moreSubtraction(40,3,11)

def mulitplication(w,x,y,z):
    multiply = w * x * y * z
    return multiply

print mulitplication(2,2,1,3)

def division(x,y):
    divide = x / y
    # divide = float(x) / float(y) # to not get a whole number
    return divide

print division(27,3)

################################
# Built-in Functions

length = len("Len is a function that gets the length of whatever you pass into it.")
print length

# str turns whatever is passed to it into a string
x = 23
print str(x)

y = 2.32
print str(y)

# float requires whatever passed into it to be converted into a fractional number,
# which allows for decimal points to be shown

# float is any number with a decimal point; int, integer, is any whole number

z = float(40)/float(7)
print z
# convert the float into an integer but does not round
zInt = int(z)
print zInt
# to round the number:
print round(z) # is not an integer

print int(round(z))
