#Personal Finance algorithms

import matplotlib.pyplot as plt

# Some functions can either have an S at the end or not. The difference is that functions with an S at the end graphically show what they are doing.
# For example, the function 'sumCalc' takes arguments in and only prints the requested result, while the function sumCalcS also plots the two entities growing.

# function that takes as input the base net worth that one wants to invest, the amount they can save each year, the interest rate (in decimals) and the time in years, and returns how much the net worth should be after those years, with and without the added interest (to have an understanding of how much the interest affects the total)
def sumCalc(base, save, rate, time):
    base2 = 0
    for i in range(time):
        base = base + save
        base2 = base2 + save
        base = base + (base*rate)
    
    return base, base2

# function that takes as input the base net worth that one wants to invest, the amount they can save each year, the interest rate (in decimals) and the net worth goal, and returns the amount of time needed to reach it
def timeToFire(base, save, rate, goal):
    time = 0
    while(base < goal):
        base = base + save
        base = base + (base*rate)
        time +=1

    return time

# function that takes as input the net worth, the yearly expenses and the interest rate (in decimals), and returns the number of years for which the net worth can cover the expenses
def timeToBroke(base, expense, rate):
    time = 0
    while (base>0):
        base = base-expense
        base = base + (base*rate)
        time +=1

    return time

# function that takes as input the base salary, the yearly prospected raise (in decimals) and the number of years, and returns the final salary 
def salaryGrowth(base, rate, years):
    for i in range(years):
         base *= (1+rate)
    return base

# Here are defined the graphical functions

def sumCalcS(base, save, rate, time):
    x, y, y2 = ([] for i in range(3))
    base2 = base

    for i in range(time):
        
        x.append(i)
        base = base + save
        base2 = base2 + save
        y2.append(base2)
        base = base + (base*rate)
        y.append(base)

    plt.plot(x, y)
    plt.plot(x, y2)
    plt.show()

    return base, base2

def timeToBrokeS(base, expense, rate):
    x = [0]
    y = [base]

    while (base>0):
        base = base-expense
        base = base + (base*rate)
        x.append(x[-1]+1)
        y.append(base)

    plt.plot(x, y)
    plt.show()

    return x[-1]
