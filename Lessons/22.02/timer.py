import time

isRun = False

def start():
    global start_time
    global isRun
    isRun = True
    start_time = time.time()

def finish():
    if isRun:
        global isRun
        isRun = False
        return time.time() - start_time
    else:
        return -1
    

if __name__ == "__main__":
    start()
    for i in range(100):
        print(f"test value {i}")
    print(finish())