monthEarnings = int(input("Please enter the amount of money you earned this month:"))
totalSpent = []
foodSpent = int(input("How much did you spend on Food this month:"))
transportSpent = int(input("How much did you spend on transport this month: "))
entertainmentSpent = int(input("How much did you spend on transport this month: "))

totalSpent = foodSpent + transportSpent + entertainmentSpent

monthlyBudget = monthEarnings - totalSpent
print( f"This month you have earned {monthEarnings} , and your combined monthly costs are:  {totalSpent} Which leave you with after the month:  {monthlyBudget}")
