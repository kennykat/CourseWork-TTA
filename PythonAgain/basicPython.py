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

print "\n8 & 9. while and for loops"

while (x < 4):
    x = x + 1
    print x
