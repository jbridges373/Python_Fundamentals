event = input("What was the event or occasion? ")
cost = input("How much was it? ")
service_charge = input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%) : ")
group_size = input("How many people were in your group? ")
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
