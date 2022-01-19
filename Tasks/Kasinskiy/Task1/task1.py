from decimal import Decimal as dD

initial_deposit = 20000
interest_rate = 15
deposit_term = 60

final_income = dD(dD(initial_deposit)*(1+dD(interest_rate)/(100*12))**dD(deposit_term))
print(final_income.quantize(dD("1.0000")), 'BYN')

