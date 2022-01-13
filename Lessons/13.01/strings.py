x = """my first line
my second line
my third line"""

y = "my\tfirst\tline\nmy\tsecond\tline\nmy\tthird\tline"

# print(x)
# print(y)
# print(x == y)

s = "my very long string"
print(len(s))
print(s[0], s[1], s[2], s[3], s[4], s[5])
print(s[0], s[-1], s[-2], s[-3], s[-4], s[-5])

print(s[len(s)-1])
# print(s[len(s)]) #string index out of range

print(s[-len(s)])
# print(s[-len(s)-1]) #string index out of range

print(s[0:7])
print(s[3:-3])

print(s[3:-3:2])
print(s[::-1])

print('s' in s)
print('long' in s)
print('test' in s)