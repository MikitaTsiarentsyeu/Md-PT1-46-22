from decimal import Decimal as dD

initial_deposit = 20000
interest_rate = 15
deposit_term = 60

final_income = dD(initial_deposit*(1+interest_rate/(100*12))**deposit_term)
print(final_income, 'BYN')
print(type(final_income))
