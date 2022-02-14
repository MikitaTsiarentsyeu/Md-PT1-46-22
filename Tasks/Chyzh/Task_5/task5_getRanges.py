#third function <--"get_ranges"--> that shorten the list of non-repeated integers

list = [1,2,3,5,8,9,11,12,13,15]

def get_ranges(list):
    N1 = N2 = None
    for i in list:
        if N1 is None:
            N1 = N2 = i
        elif i == N2 or i == N2 + 1:
            N2 = i
        else:
            yield (N1, N2)
            N1 = N2 = i
    if N1 is not None:
        yield (N1, N2)
print(repr(','.join([f"{N1}" if N1 == N2 else f"{N1}-{N2}" for (N1, N2) in get_ranges(list)]))) 
    
  