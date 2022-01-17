import decimal
from decimal import Decimal

a = decimal.Decimal('20000') 
b = decimal.Decimal('5')
c = decimal.Decimal('15')

d = (a*((1+(c/(100*12)))**(b*12)))
d = d.quantize(Decimal("1.00"))
print("After 5 years on your account will be", d, "BYN")
