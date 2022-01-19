import decimal

initial_sum = decimal.Decimal('20000')
months_in_year = 12
period = 5 * months_in_year
depo_rate = decimal.Decimal('0.15')


final_sum = initial_sum * (1 + (depo_rate/months_in_year))**period


print(f'Sum you deposit: {initial_sum} BYN')
print(f'The sum on your account after {period//months_in_year} years: {final_sum:.2f} BYN')