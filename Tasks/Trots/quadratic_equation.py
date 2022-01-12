import math

a = 3
b = -14
c = -5
discriminant = b**2 - 4*a*c

x_1 = ((-b) + math.sqrt(discriminant))/(2*a)
x_2 = ((-b) - math.sqrt(discriminant))/(2*a)

print(x_1)
print(x_2)