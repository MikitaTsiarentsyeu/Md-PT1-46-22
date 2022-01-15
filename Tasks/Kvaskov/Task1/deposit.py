import decimal
ndy = decimal.Decimal("365.2425")                           #number of days in a year
da = decimal.Decimal("20000")                               # deposit amount
dt = decimal.Decimal("5")                                   # deposit term
percent = decimal.Decimal("15")                             # deposit rate
dtd = ndy*dt                                                # deposit term in days
dtm = dt*12                                                 # deposit term in month
result = da*((1+(percent/100)/12)**(dtm))                   # monthly capitalization
result = round(result,2)
print(result)

