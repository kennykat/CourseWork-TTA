''' -- Item 36 of 68 -- '''

print "\n1. assigning int to variable"
shoeSize = 10
print shoeSize

print "\n2. assigning string to variable"
shoeBrand = "Adidas"
print shoeBrand

print "\n3. assigning float to variable"
shoePrice = 59.99
print shoePrice

print "\n4. print function and .format() notation to print assigned variable"

print "{} is the price for the size {} {} shoes.".format(shoePrice,shoeSize,shoeBrand)

print "\n5. operators"
x = 10
y = 5

print x + y
print x - y
print x * y
print x / y

x += 2
print x

print x % y

print "\n6 & 7. logical operators & conditional statements"

if x == 300:
    print "x is not equal to 300"

elif x and y == 10:
    print "x and y are equal to 10"

else:
    print "else statement is working"

if x or y == 6:
    print "either x or y are equal to 5"

if not x == 10:
    print "x does not equal 10"

print "\n8. while loops"

while (x < 18):
    x = x + 1
    print x

print "\n9. for loops"

for i in range(9):
    y = y + 1
    print y

print "\n10. lists with for loops"

lyrics = ["this", "is", "how", "we", "do", "it"]
for l in lyrics:
    print l

print "\n11. tuples with for loops"

myTuple = ("tuple", "for loops", 8.56,)
for t in myTuple:
    print t

print "\n12. function with string variable"


def practiceFunction(x,y):
    addition = x + y
    return addition

print practiceFunction(3,5)
