monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

Monthly_Savings = monthly_income - monthly_expenses

Projected_Savings = (Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05))

print(f"Your monthly savings after one year, with interest, is {Projected_Savings}")