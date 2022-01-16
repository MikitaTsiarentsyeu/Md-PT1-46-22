# начальная сумма - 20000 BYN
# срок - 5 лет
# процент (годовой) - 15%

# Вычислить сумму на счету в конце указанного срока





from decimal import Decimal

depozit = Decimal('20000')
procent = Decimal('15')
god = Decimal('60')
c = depozit * (1 + procent / 100 / 12) ** god
print(c.quantize(Decimal('1')))





