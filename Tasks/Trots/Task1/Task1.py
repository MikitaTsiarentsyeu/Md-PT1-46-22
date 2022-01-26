from decimal import Decimal

start_deposit = Decimal('20000')
rate = Decimal('0.15')
term = Decimal('60')

final_sum = start_deposit*(Decimal('1') + rate/Decimal('12'))**term

print("The amount of the deposit at the end of the term will be - ", round(final_sum, 2), "BEL.")
