import decimal
start_amount = decimal.Decimal(20000)
years_amount = decimal.Decimal(5)
year_percent = decimal.Decimal(15) / 100  # dividing year % to 100 for better calculation
month_amount = years_amount * 12
result = start_amount * (1 + year_percent / 12) ** month_amount
print('Start amount is', start_amount, 'after', years_amount, 'years you will have:', end=' ')
print(round(result, 2), 'BYN')
