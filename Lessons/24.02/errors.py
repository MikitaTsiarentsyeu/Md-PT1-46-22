
from prompt_toolkit import Application


x = [1,2,3,4,5]

try:
    print(x[10])
except NameError as er:
    print(er)
except IndexError:
    try:
        raise(RuntimeError)
    except:
        print("Gotch youa!")
    finally:
        print("inner finally")
    print("Index Error")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("finally")
    # raise(RuntimeError)

try: pass
finally: pass

print("after error")

# with open("text.txt", 'w') as f:
#     f.write("test")

# try:
#     f = open("text.txt", 'w')
#     f.write("test")
# finally:
#     f.close()

# for i in range(20):
#     if i % 2 == 0:
#         print("Even number detected, it will be skiped")
#         continue
#     print(i)


for i in range(20):
    try:
        # if i % 2 == 0:
        #     raise(RuntimeError("Even number detected, it will be skiped"))
        print(i)
        print(x[i])
    except IndexError as er:
        print(er)
        continue
