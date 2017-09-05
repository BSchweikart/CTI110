# Base meal price before tip & Tax
total_meal = float(input('Enter meal cost:'))

# Calculate tip from meal
tip = total_meal * 0.18

# Calculate tax from meal
tax = total_meal * 0.07

# Display meal w/tax and tip added
print('meal_cost =',total_meal)
print('tax =', tax)
print('tip =',tip)
print('Total meal cost is $',total_meal + tip + tax)


