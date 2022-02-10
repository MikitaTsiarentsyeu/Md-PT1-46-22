def maker(n):
    def action(x):
        return x ** n
    return action

square = maker(2)
cube = maker(3)
forth = maker(4)

print(square(4), cube(4), forth(4))

# maker = maker(10)
# for i in range(10):
#     print(maker(i))