from decimal import Decimal

deposit_amount_raw = input('input deposit sum: ')
# place for input verification
deposit_amount = Decimal(deposit_amount_raw)
rate_raw = input('input rate, %: ')
# place for input verification
rate = Decimal(rate_raw) / 100
invested_term_raw = input('input invested term, years: ')
# place for input verification
invested_term = Decimal(invested_term_raw)

print('------------------------------')
invested_term_months = invested_term * 12
dividend = deposit_amount*(1+rate/12)**invested_term_months

print(f'{dividend.quantize(Decimal("1.00"))} BYN')








