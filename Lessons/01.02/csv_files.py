import csv

fieldnames = ["col1", "col2", "col3"]

with open("test.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerow({"col1":"val1", "col2":"val2", "col3":"val3"})

    # writer = csv.writer(f)
    # writer.writerow(["cat", "dog", "rat"])
    # writer.writerows([["cat", "dog", "rat"], ["tigger", "bear", "rabbit", "pig"]])
    # f.write("val1,val2,val3")

with open("test.csv", 'r', newline='') as f:
    reader = csv.DictReader(f, fieldnames)
    for l in reader:
        print(l)

    # reader = csv.reader(f)
    # for l in reader:
    #     print(repr(l))
    #     for elem in l:
    #         print(elem)