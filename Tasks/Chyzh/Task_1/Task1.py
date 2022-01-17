import decimal
from decimal import Decimal
y = 5
N = 12*y
K = 20000
P = 15
d = 30
D = 365
temp = 1+(P*d)/D/100
S = Decimal(K* (temp ** N))
print(S.quantize(Decimal("1.00"))) 