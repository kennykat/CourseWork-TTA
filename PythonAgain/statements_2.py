'''
--- Statements ---

-- IF --
if (condition):
    < Start code if (condition) is True >
    ...
    < End of code >

-- ELSE --
if (condition):
    < Indented space runs if (condition) is True >
else:
    < Indented space runs if (condition) is False >

-- ELIF --
if (condition 1):
    < Indented space runs if (condition 1) is True >
elif (condition 2):
    < Indented space runs if (condition 2) is True and (condition 1) is False >
else:
    < Indented space runs if (condition 1 and condition 2) are False >
'''

## define variable
x = 1

## if statement
if x == 10:
    print 'x = 10'

## if 'if' statement is incorrect
elif x == 9:
    print 'x = 9'

## if both 'if' and 'elif' statements are incorrect
else:
    print 'x does not equal 9 or 10'
