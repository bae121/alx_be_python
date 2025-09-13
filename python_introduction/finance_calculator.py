# Prompt user for input
monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your total monthly expenses: '))

# Calculation of monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Results
print(f'Your monthly savings are: ${monthly_savings}')
print(f'Your projected annual savings after 5% interest are: ${projected_savings}')
