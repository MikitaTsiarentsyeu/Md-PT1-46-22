from decimal import Decimal
deposit = Decimal(20000)
months = 60
interest_rate = Decimal(0.15)

while months >  0:
    deposit = deposit + ((deposit * interest_rate)/12)
    months -= 1

print(round(deposit, 2))