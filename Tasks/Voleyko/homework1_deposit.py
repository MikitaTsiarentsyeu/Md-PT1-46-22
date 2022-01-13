d_amount=20000
term=5
rate=15

deposit=d_amount*((1+rate/100/12)**(term*12))

print('Cумма на счету в конце составит:',int(deposit),'',end='BYN')
