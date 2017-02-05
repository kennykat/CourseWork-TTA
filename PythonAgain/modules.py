''' --- Modules --- '''
# import math

# print math.sqrt(16)
# print int(math.sqrt(16))

from math import sqrt, exp

print sqrt(16)
print exp(2)
print "break"

''' --- importing self created 'smallMathModule' --- '''

import smallMathModule

# print module.function(variable)
print smallMathModule.multiplyBy5(3)

print smallMathModule.add5(9)

print smallMathModule.randomAdd(8)
