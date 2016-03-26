## Variables and Types

variable_name = 10;

variable_name2 = variable_name

#3 most commonly used built-in data types:
## 1. Numbers
## 2. String
## 3. List
## 4. Tuple

## T U P L E S  -- Tuple is immutable it's value cannot be changed.

## remember tuples start counting from value 0 and stops before the value you told it to.
# tup1 = ['John','M','27']
## one way to access values of a tuple
## 0:2 means "get 0 and all the rest before you reach 2".
# print tup1[0:2]

## create a tuple -- name('a','b')
# myTuple1 = ('Richard','27','Male','Insurance and Banking')
## print it's value
# print myTuple1
## delete the tuple
# del myTuple1
## tuple is non existent now that 'del' has occured
# print myTuple1

## find length of tuple -- len(tuple_value)
print len(('a','b',9,12.75))
myTuple1 = ('a','b',9,12.75)
## shortcut to find length of tuple
print len(myTuple1)

## to Concatenate Tuples
myTuple = (('a','b',9,12.75))
myTuple=myTuple+('Richard','27','Male','Insurance and Banking')
print myTuple

## check if particular value exists in a tuple
print myTuple
16 in myTuple
