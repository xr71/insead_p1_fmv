import math
# import numpy as np


pvs = []
for i in range(10):
    pvs.append(30000/(1.05**(30-i)))

# prevent value of pension is only $87,307.23

# 1) it is better to receive a lump sum of 100000 today 

## but if Mary's salary (50000 today) grows by 5% each year for another 20 years
finalsalary = 50000 * 1.05**20
print(finalsalary)

pensionsalary = finalsalary*.6

pvs = []
for i in range(10):
    pvs.append(pensionsalary/(1.05**(30-i)))
# now it is worth $231,652


## breakeven salary 
# first, calculate mary's final pension salary in terms of r
# that is:  50000 * (1+r)**20 * 0.6 
# this is 60% of her final salary given that the 50000 increases by r each year
# now treat this value as a fixed annuity from the time of retirement
# p_salary_r / 0.05 * (1-1/(1.05**10)) to get the "present value" of the pension at time of retirement
# now discount this entire thing back 20 years to get the current day value

def grate(x):
    p_salary = 50000 * (1+x)**20 * 0.6 
    pv_pension_at_retire = p_salary/0.05 * (1-(1/(1.05**10)))

    return pv_pension_at_retire/1.05**20

start_rate = 0.05
step = 0.00005
diff = 100000
while diff > 1:
    diff = grate(start_rate) - 100000 
    start_rate -= step
    print(diff, start_rate*100)
