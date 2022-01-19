# Депозит: начальная сумма 20 000 BYN, срок 5 лет, годовой процент 15%, ежемесячная капитализация.

import decimal
K = 20000
P = 15
m = 12
n = 5
S = decimal.Decimal(K) * ( 1 + decimal.Decimal(P) / (100 * decimal.Decimal(m)))**(decimal.Decimal(m)*decimal.Decimal(n))
print (round (S,2))