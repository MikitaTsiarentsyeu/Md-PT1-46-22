d = {9103976271:("Reina Meinhard", "Memphis, Tennessee"),
4199392609:("Stephanie Bruce", "Greensboro, North Carolina"),
9099459979:("Ermes Angela", "Dallas, Texas"),
6123479367:("Lorenza Takuya", "Indianapolis, Indiana"),
9103976271:("Margarete Quintin", "Raleigh, North Carolina")}

x = int(input("Please enter phone number:"))

# val = d.get(x, -1)
# if val == -1:
#     print("not found")
# else:
#     print(f"{val[0]} from {val[1]}")

val = d.get(x)
if not val:
    print("not found")
else:
    print(f"{val[0]} from {val[1]}")

# if x in d.keys():
#     val = d[x]
#     print(f"{val[0]} from {val[1]}")
# else:
#     print("not found")

# if x in d:
#     val = d[x]
#     print(f"{val[0]} from {val[1]}")
# else:
#     print("not found")

n = 1

n = n - 12 if n > 12 else n 

d = {1:"один", 2:"два"}
d[n]