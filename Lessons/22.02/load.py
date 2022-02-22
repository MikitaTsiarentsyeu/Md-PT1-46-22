import timer

timer.start()

for i in range(100000000):
    i = i*i

print(timer.finish())