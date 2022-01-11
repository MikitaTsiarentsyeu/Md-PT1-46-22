deposit = 20000
period = 5
rate = 15/100

rate_in_month = rate/12
period_in_month = period*12

for month in range(period_in_month):
     deposit += (deposit*rate_in_month)

print('По истечении срока депозита на вашем счету будет', round(deposit, 2), 'BYN', sep=' ')