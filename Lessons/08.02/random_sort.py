import random

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def generate_index(n):
    return random.randint(0, n-1)

def swap(l):
    i = generate_index(len(l))
    j = i
    while i == j:
        j = generate_index(len(l))
    l[i], l[j] = l[j], l[i]

def sort(l):
    counter = 0
    while not is_sorted(l):
        counter += 1
        print(counter)
        swap(l)

# l = [25,2,3,5,7,9,7,6,4,3,5,7,8,98,7,4,3,3,5,6,25,4]
l = [7,6,5,4,3,2,1]
print(is_sorted(l))
sort(l)
print(l)