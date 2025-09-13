# User's input of monthly income and expenses

monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings

monthlySavings = monthlyIncome - monthlyExpenses

# Project annual savings with 5% interest

annualSavings = monthlySavings * 12
projectedSavings = annualSavings + (annualSavings * 0.05)

# Results

print("Your monthly savings are:", monthlySavings)
print("Your projected annual savings after 5% interest are:", projectedSavings)
