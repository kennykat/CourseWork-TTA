name = "Guido"

print name[0]
# changes string to uppercase
print name.upper()
# changes string to lowercase
print name.lower()
# capitalizes the first letter of the string
print name.capitalize()

'''
Capitalizes the first letter of every word in string
.title()
Switches the case of every character in the string
.swapcase()
Removes the whitespace, tabs and indents from the string
.strip()

'''

####################
date = "11/12/2013"

# goes through string and splits where there is a '/'
date_manip = date.split('/')

# shows the outcome
# print date_manip

print date_manip[0]
print date_manip[1]
print date_manip[2]


# concatenation
print 'Month: ' + date_manip[0]
print 'Day: ' + date_manip[1]
print 'Year: ' + date_manip[2]

# or

print ('Month: ' + date_manip[0] +
    '. Day: ' + date_manip[1] +
    '. Year: ' + date_manip[2])
