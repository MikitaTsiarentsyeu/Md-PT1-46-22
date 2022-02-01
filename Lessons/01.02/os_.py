import os

print(os.name)

print(os.sep)

print(os.sep.join(['test level 1', 'test level 2']))

x = os.path.join("test level 1", "test level 2", "test level 3")

print(os.getcwd())

# os.makedirs(x)

# os.chdir(x)
# print(os.getcwd())

print(os.listdir())

print(os.walk(os.getcwd()))
for l in os.walk(os.getcwd()):
    print(l)

os.removedirs(x)