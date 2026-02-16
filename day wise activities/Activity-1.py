import math

# Taking input from user
print("Enter sides of first triangle (a1 b1):")
a1, b1 = map(int, input().split())

print("Enter sides of second triangle (a2 b2):")
a2, b2 = map(int, input().split())

# Calculate hypotenuse
h1 = int(math.sqrt(a1*a1 + b1*b1))
h2 = int(math.sqrt(a2*a2 + b2*b2))

# Print result
print("Difference between hypotenuse values is:", abs(h1 - h2))
