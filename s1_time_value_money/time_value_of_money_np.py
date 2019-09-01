import platform
import os
import sys
import numpy as np
import pandas as pd

try:
    if platform.system() == "Windows":
        os.system("cls")

    else:
        os.system("clear")
except:
    pass

print("Future of value of cash flow: assuming $1000 at 10% for 3 years:")
C = 1000
r = 0.1
t = 3

fv = C * (1+r)**t
print(f"Future value is:  ${round(fv, 2)}")


print("\nPresent value of cash flow: assuming $1000 at 10% three years from now:")
pv = C / ((1+r)**t)
print(f"Present value is:  ${round(pv, 2)}")

print()

print("Multiple streams of cash flow: $1000 each year for 3 years at 10%")
fv = 0
cashflows = [1000, 1000, 1000]
t = len(cashflows)

for c in cashflows:
    fv += c * (1+r)**t 
    t -= 1

print(f"Future value of $1000 per year for 3 years at 10% is:  ${round(fv)}")

print()

print("Current value of future cash flows:  ")
print("Suppose we will receive 5000, 8000, 8000, 8000 each year," \
    "what is the current value we should lend out if we would otherwise earn 6% per year")

s = pd.Series([5000, 8000, 8000, 8000])
t = pd.Series([1,2,3,4])
df = pd.DataFrame({"cashflow": s, "time": t})
df["rate"] = 0.06
print(df)

print("apply discount factor by time")
df["discounted"] = df.apply(lambda x: x.cashflow / ((1+x.rate) ** x.time), axis=1)
print(f"Present value of loan should be:  ${round(df.discounted.sum(), 2)}")
print()

print("#" * 80)
print("Net present value of an investment opportunity")
print("#" * 80)
print("Suppose we invest 1000 in year 1, then receive 500 per year for next 3 years that would otherwise earn 10% per year:")

df = pd.DataFrame({"cashflow": [-1000, 500, 500, 500]})
df["time"] = df.index
df["discounted"] = df.apply(lambda x : (x.cashflow / (1.10) ** x.time), axis=1)

print(f"\nThe NPV of the investment opportunity is  ${round(df.discounted.sum(), 2)}\n")