val = 2

print(__debug__)

try:
    assert val > 4, "Assertion Error: The value should be greater then 4"
    # if val > 4:
    #     raise AssertionError("The value should be greater then 4")
except AssertionError as er:
    print(er)

print(val)