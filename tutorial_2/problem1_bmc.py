import math
import numpy as np

initialinvestment = 10000
tax = 0.34
time = 4
depre = 2500 

sales = 7000
costs = 2000 
print(sales-costs-depre)

ebit = sales-costs-depre 
noplat = ebit * (1-tax)

print(noplat+depre)
delta_wc = [200, 50, 50, -100, -200]

np.npv(.12, [-10200, 4100, 4100, 4250, 4350])
np.irr([-10200, 4100, 4100, 4250, 4350])
