'''
#method 1 
from math import sqrt, pi 

result = sqrt(9) * pi 
print(result)

# method 2 result (9.424)
import math as m 

result = m.sqrt(9) * m.pi
print(result)

import math

print(dir(math))
print(math.nan,type(math.nan))


# method how to import code from other file and mearsed
from back import welcome, akshay

welcome()
print(akshay)
'''
# another method to import * will import all the code from code
from back import *

welcome()
print(akshay)
