from ntpath import join


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

print(s.upper())
print(s)
print("TeSt_sTrInG".upper())
print("TeSt_sTrInG".lower())

print(s.find('y'))
print(s.find('!'))

print(s.find(' very '))
print(s.find(' very !!!'))

x = s.replace('n', 'N')
print(x)
x = x.replace('very', 'not so')
print(x)
print(s)

print(s.split('o'))
x = s.split()
print('_'.join(x))
print('_'.join(x) == s.replace(' ', '_'))

print("!!!test!!!".strip('!'))

c, d, p = "cat", "dog", "parrot"
s = "a " + c + ", a " + d + ", a " + p #bad approach, do not use!!!!!!!!!!!!!!!!!!

print("a {}, a {}, a {}".format("dog", "cat", "parrot"))
print("a {}, a {}, a {}".format("cat", "dog", "parrot"))
print("a {1}, a {2}, a {0}".format("cat", "dog", "parrot"))
print("a {c}, a {d}, a {p}".format(c="cat", d="dog", p="parrot"))

print("a {}, a {}, a {}".format("cat", "dog", "parrot", "another dog"))

print(f"a {c}, a {d}, a {p}")
x = 25/4.9
print(x)
print(f"high {x:.10f}!")

print("%s %d" % ("test", 45)) # old style, do not use!!!!!!!!!