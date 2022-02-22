# from module2 import global_val as gv, print_global_val as pgv
print(__name__)
global_val = "test"

from module2 import *

# print_global_val = 78

# module2 = "test"
# print(module2)

# import module2 as mdl2
# print(module2)

print("hello from module1")
print(global_val)
print_global_val()
global_val = 42
print_global_val()