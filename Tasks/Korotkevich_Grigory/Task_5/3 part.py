a = [1,4,5,6,7,8,10,11,44,45,66]
def get_range(a):
    receiving = f'{a[0]}'
    passage = False
    for index in range(len(a) - 1):
        if a[index + 1] - a[index] == 1:
            passage = True
        else:
            if passage:
                receiving += f'-{a[index]}, {a[index + 1]}'
            else:
                receiving += f', {a[index + 1]}'
            passage = False
    if passage:
        receiving += f'-{a[-1]}'
    return print(receiving)

get_range(a)
