# f = open("test.txt", 'w')
# f.write("test content")
# f.close()

with open("test.txt", 'w') as f:
    print(f, type(f))
    f.write("new test content\n")
    f.writelines(["test line 1\n", "test line 2\n", "test line 3"])
    # f.read() ERROR

with open("test.txt", 'r') as f:
    for l in f:
        print(repr(l))
    # f.write("") ERROR

    # print(repr(f.readline()))
    # print(f.readlines())

    # f.seek(10)
    # print(f.read(3))
    # print(f.read(5))

    # print(f.read())
    # f.seek(0)
    # print(f.read())

with open("test.txt", 'a') as f:
    f.write("\nappended content")
    # f.seek(0)
    # f.read() ERROR
    # f.write("prepended content\n") writing to the end anyway

with open("test.txt", 'a+') as f:
    f.write("\nappended content #2")
    f.seek(0)
    f.write("prepended content\n")
    print(f.read())

with open("test.txt", 'r+') as f:
    f.write("prepended content from the r+ mode\n")
    print(f.read())

with open("test.txt", 'w+') as f:
    f.write("totally new file content")
    f.seek(0)
    f.write("after moving to zero\n")
    print(f.read())


