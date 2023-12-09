
import random
number = random.randint(-10, 10)
print("The number is:", number)
print("is positive" if number > 0 else "is zero" if number == 0 else "is negative")
