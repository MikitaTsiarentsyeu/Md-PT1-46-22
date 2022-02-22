global_val = [5]

def print_global_val():
    print(f"global val from module2 is {global_val}")

print(__name__)
if __name__ == "__main__":
    print_global_val()
    print("HUGE PRINT")