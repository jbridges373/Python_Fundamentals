# Challenge: Apply type conversion to the PayUp app.
# 1. Wrap the appropriate input() calls in float() or int().
# 2. Type check cost, service_charge, and group_size.
# 3. Run the program and make sure everything still works as expected.

event = input("What was the event or occasion? ")
cost = float(input("How much was it? "))
service_charge = int(input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%): "))
group_size = int(input("How many people were in your group? "))
grand_total = 330
total_per_person = 110

print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for {event}:")
print()
print(f"Cost: ${cost}")
print(f"Service charges: ${service_charge}")
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total}")
print()
print(f"Each person must PayUp: ${total_per_person}")

print(type(cost))
print(type(service_charge))
print(type(group_size))
