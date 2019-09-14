import math
import numpy as np


## A
# 1000 now for 5 years at 10%
v = 1000 * (1.1)**5
print(round(v, 2))
# $1610.51


## B
# tesla costs 109000 today, how much money should i put
# at 3% and would like to buy it in 20 years
# x*(1.03)**20 = 109000
v = 109000/(1.03**20)
print(round(v,2))
# $60350.66


## C
# 1000 * (1.03**N) = 109000 

print(math.log(109, 1.03))
print(1000 * (1.03**158.7124))
# 158.72 years 


## D
# 75000 when child enters college in 18 years
# you have 7000 to invest now 
# 7000 * (r**18) = 75000
print((75000/7000) ** (1/18))
print(round(7000 * 1.141**18, 2))
# 14.1%

