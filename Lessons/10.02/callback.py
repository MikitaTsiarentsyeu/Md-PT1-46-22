import time, threading

def show_text():
    print("some ad here")

def show_signs():
    print("!!!!@@@@####$$$$%%%%%&&&&&&&")

def timer(t, callback):
    callback()
    time.sleep(t)
    print("after sleep")
    timer(t, callback)

def call():
    show_signs()
    threading.Timer(3, call).start()
    for i in range(10000000000000000):
        print(i)

# timer(3, show_text)
# timer(3, show_signs)

call()