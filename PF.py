#Personal Finance algorithms

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
