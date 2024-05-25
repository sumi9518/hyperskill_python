# Define the earned amounts for each item
earned_amounts = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}

# Print the earned amounts
print("Earned amount:")
for item, amount in earned_amounts.items():
    print(f"{item}: ${amount}")

# Calculate the total income
total_income = sum(earned_amounts.values())
print(f"\nIncome: ${total_income}")

# Read the staff and other expenses from the user (removed the '>' symbol from prompts)
staff_expenses = int(input("Staff expenses:\n"))
other_expenses = int(input("Other expenses:\n"))

# Calculate the net income
net_income = total_income - (staff_expenses + other_expenses)

# Print the net income
print(f"\nNet income: ${net_income}")
