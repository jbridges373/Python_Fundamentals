# Challenge: Create the output display for the PayUp app.

# 1. Check out the example output in `example_output.md`
# 2. Define a variable for each item: event name, cost, service charge,
#    group size, grand total, and total per person. Use made-up values for now –
#    we'll do the math later!
# 3. Build the display line by line using print() and f-strings.
#    Remember: an empty print() creates a blank line.
# 4. Run it and make sure it matches the example.


# 1. Gather inputs from the user
event_name = input("Enter the event name (e.g., dinner at Fantastic Pizza): ")
cost = float(input("Enter the initial cost (£): "))
service_charge = float(input("Enter the service charges (%): ").strip("%"))
group_size = int(input("Enter the group size: "))

# 2. Perform the calculations
service_charge_cal = cost * (service_charge / 100)
grand_total = cost + service_charge_cal
split_amount = grand_total / group_size

# 3. Print the formatted output breakdown
print("=" * 40)
print("\nWelcome to PayUp!")
print()
print(f"Here's the breakdown for the fun event at {event_name}:\n")
print(f"Cost: £{cost:.2f}")
print(f"Service charges: £{service_charge_cal:.2f}")
print(f"Group size: {group_size}")
print(f"Grand total: £{grand_total:.2f}\n")
print(f"Each person must PayUp: £{split_amount:.2f}")
print()
print("=" * 40)
print()
