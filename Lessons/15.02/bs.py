[1,2,3,4,5,6,7,8,9] #1

# def search(l, elem) -> int:
#     "return the index of the elem, -1 if it's not in l"
#     pass

def iterate(l, counter = 0):
    if counter == len(l):
        return
    print(l[counter])
    iterate(l, counter+1)

iterate([1,2,3,4,5])
l = [1,2,3,4,5]

def search(l, target, low, high):
    if high >= low:
        mid = (low + high) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            return search(l, target, low, mid-1)
        else:
            return search(l, target, mid+1, high)
    else:
        return -1

print(search(l, 7, 0, len(l)-1))