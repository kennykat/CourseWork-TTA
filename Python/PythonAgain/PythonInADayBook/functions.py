''' --- Functions --- '''
# def function(parameters):
#     >> what to do with parameters aka variables
#     >> return value
# 'def' lets python know this is a function

someValue = 5

def addFunction(x,y):
    addition = x + y
    sameValue = 10
    return addition

print addFunction(3, 5)
print someValue

def subtraction(a,b):
    subtract = a - b
    return subtract

print subtraction(10, 4)

def moreSubtraction(d,e,f):
    subtract = d - e - f
    return subtract

print moreSubtraction(40, 3, 11)

def multiplicationFunction(x,y,z):
    multiply = x * y * z
    return multiply

print multiplicationFunction(2, 1, 4)
print "break"

''' --- Built-in Functions --- '''
# len() - gets length of what you pass into it
length = len("this is a string")
print length

# str() - turns what you pass into it into a string
x = 23
print str(x)
x = 2.32
print str(x)

# float() - turns what you pass into it into a fractional number which allows decimal points to be shown
y = float(40)/float(7)
print y

# int() - convert from float to integer w/ no decimal point
yInt = int(y)
print yInt

# round() - rounds float to nearest whole number
print round(y)
print int(round(y))
