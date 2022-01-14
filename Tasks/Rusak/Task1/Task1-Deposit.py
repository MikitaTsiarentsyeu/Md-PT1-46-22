from decimal import Decimal

deposit = Decimal('20000')
period = 5
rate = Decimal('15')/Decimal('100')

rate_in_month = rate/Decimal('12')
period_in_month = period*12

for month in range(period_in_month):
     deposit = deposit + (deposit*rate_in_month)

print('По истечении срока депозита на вашем счету будет', deposit.quantize(Decimal('1.00')), 'BYN')