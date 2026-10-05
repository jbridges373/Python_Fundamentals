# decibels = 20

# if decibels < 89:
#     print("Warning: Loud Environment")
# else:
#     print("Safe Environment")

# Challenge: Quiz Pass or Fail
# You're building the results screen for an online course quiz. A student
# needs at least 60 points to pass.

# 1. Ask the student for their score and convert it to an int.
score = int(input("Enter your quiz score: "))

# 2. If their score is 60 or higher, print that they passed.
if score >= 60:
    print("Congratulations! You passed the quiz.")

# 3. Otherwise, print that they didn't pass this time.
else:
    print("Sorry, you didn't pass this time.")