import decimal
from decimal import Decimal

a = decimal.Decimal('20000') 
n = decimal.Decimal('5')
p = decimal.Decimal('15')

s = (a*((1+(p/(100*12)))**(n*12)))
s = s.quantize(Decimal("1.00"))
print("Current balance is", s, "BYN")

