# cost = float("300")
# service_charge = "30"
# # print(cost + service_charge)

# print(type(cost))
# print(cost)

# budget = float(input("What is your budget for the project? "))
# print(budget)
# print(type(budget))

# print(budget + 100)

# Challenge: Build a simple paycheck calculator.
# 1. Instead of hard coded values, prompt the user for their hourly_rate and hours_worked.
raw_hourly_rate = float(input("Enter your hourly rate: "))
raw_hours_worked = int(input("Enter the number of hours worked: "))

# 2. Convert hourly_rate to a float and hours_worked to an integer.
hourly_rate = float(raw_hourly_rate)
hours_worked = int(raw_hours_worked)

# 3. Type check both variables.
print(type(hourly_rate))
print(type(hours_worked))

# 4. Multiply them together and print the total pay.
total_pay = hourly_rate * hours_worked
print(f"Your total pay is: £{total_pay:.2f}")