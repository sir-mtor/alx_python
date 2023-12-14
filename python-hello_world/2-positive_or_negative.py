import random
number = random.randint(-100, 100)
if number > 0:
    print(f"The number {number} is positive")
elif number == 0:
    print(f"The number {number} is zero")
else:
    print(f"The number {number} is negative")
