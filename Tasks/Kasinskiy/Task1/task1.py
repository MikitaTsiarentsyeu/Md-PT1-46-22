import decimal as d

initial_deposit = 20000
interest_rate = 15
deposit_term = 60

final_income = d.Decimal(initial_deposit*(1+interest_rate/100/12)**60)

print(final_income, 'BYN')
