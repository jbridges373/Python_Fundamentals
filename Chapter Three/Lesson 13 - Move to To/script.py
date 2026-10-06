tasks = ["email", "call", "meeting", "report", "presentation"]

tasks.insert(0, "lunch")  # Insert "lunch" at index 0

todo = tasks.pop(2)  # Remove and return the first item from the list
tasks.insert(0, todo)  # Insert the removed item at index 0
print(tasks)