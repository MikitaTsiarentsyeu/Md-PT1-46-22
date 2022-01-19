from decimal import Decimal

p = Decimal("20000") 
n = Decimal("15")
t = Decimal("5")
d = Decimal(p*((1 + n/100/12)**(t*12)))

print(d.quantize(Decimal("1.00")), "BYN")