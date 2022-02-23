def recursion_sum(summable_list, total_sum=0):
    """calculates using recursion the sum of a list of any nesting"""
    if isinstance(summable_list, int):
        return summable_list
    else:
        for i in summable_list:
            total_sum = total_sum + recursion_sum(i)
    return total_sum


print(recursion_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def number_fibonacci(n, dict_fibonacci={1: 0, 2: 1}, simple_dict_fibonacci={1: 0, 2: 1}, temporary_list=[]):
    """calculates the n-first fibonacci numbers"""
    assert n > 0, 'the number must be a positive integer'
    if n in simple_dict_fibonacci:
        for i in dict_fibonacci.values():
            temporary_list.append(i)
        print(*temporary_list[:n], sep=', ')
        return
    elif n in dict_fibonacci:
        return dict_fibonacci[n]
    else:
        simple_dict_fibonacci.clear()
        temporary_list.append(n)
        if len(temporary_list) > 1:
            temporary_list.pop()
        dict_fibonacci[n] = number_fibonacci(n-1) + number_fibonacci(n-2)
        if temporary_list[0] == n:
            temporary_list.clear()
            for i in dict_fibonacci.values():
                temporary_list.append(i)
            print(*temporary_list, sep=', ')
    return dict_fibonacci[n]


number_fibonacci(10)
