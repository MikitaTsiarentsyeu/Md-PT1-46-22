import decimal
s = decimal.Decimal('20000') 
y = decimal.Decimal('5')
p = decimal.Decimal('15')
m = decimal.Decimal('12')

x = (s*((1+(p/(100*m)))**(y*m)))
print ("With an initial deposit of 20,000 BYN, after 5 years your account will be", round (x,2), "BYN")
