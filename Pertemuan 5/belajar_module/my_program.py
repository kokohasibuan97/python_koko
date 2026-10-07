a = 10
b = 15

import calculate 

print(calculate.note)

res = calculate.calc_hypotenuse(a, b) 
print("hypotenuse:", res)

res = calculate.sqrt(a**2 + b**2) 
print("hypotenuse:", res)

res = calculate.sqrt(calculate.pow(a) + calculate.pow(b)) 
print("hypotenuse:", res)

#keyword from dan import
a = 10
b = 15

from calculate import note
from calculate import calc_hypotenuse 
from calculate import sqrt


from calculate import note
from calculate import calc_hypotenuse 
from calculate import sqrt

# vs

from calculate import note, calc_hypotenuse, sqrt

#Statement from <module> import*
a = 10
b = 15

from calculate import * 

print(note)

res = calc_hypotenuse(a, b) 
print("hypotenuse:", res)

res = sqrt(a**2 + b**2) 
print("hypotenuse:", res)

res = sqrt(pow(a, 2) + pow(b, 2)) 
print("hypotenuse:", res)

#keyword as
a = 10
b = 15

import calculate as calc
from calculate import calc_hypotenuse as hptns, sqrt 
print(calc.note)

res = hptns(a, b) 
print("hypotenuse:", res)

res = sqrt(a**2 + b**2) 
print("hypotenuse:", res)

res = sqrt(calc.pow(a) + calc.pow(b)) 
print("hypotenuse:", res)
