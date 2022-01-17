import decimal
from decimal import Decimal

d_amount=decimal.Decimal('20000')
term=decimal.Decimal('5')
rate=decimal.Decimal('15')

deposit=d_amount*((1+rate/100/12)**(term*12))


print('Сумма на счету в конце составит:', deposit.quantize(Decimal('1.00')),'', end='BYN')
#print('Cумма на счету в конце составит:',(deposit.quantize(1.00)),'',end='BYN')
