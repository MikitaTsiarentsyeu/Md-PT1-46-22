import decimal

p = decimal.Decimal(20000)
n = decimal.Decimal(0.15)

t = 12 * 5

d = p * (1 + n / 12) ** t
print(d)
