eq = input("Please input your eq:")
x = int(input("Please input your x val:"))

print(eq, x)

eq = eq.replace(" ", "").replace("y=", "")
print(eq)

coeff = eq.split('x')
print(coeff)

res = x*int(coeff[0])+int(coeff[1])
print(res)