import json
import pickle
import csv

s = '{"width":500,"height":500,"resolution":96,"quality":96,"settings":[{"filename":"_preview1.jpg","seek":10},{"filename":"_preview2.jpg","seek":35},{"filename":"_preview3.jpg","seek":70},{"filename":"_preview4.jpg","seek":95}]}'
my_obj = json.loads(s)

with open("test.json", 'r') as f:
    my_obj = json.load(f)

print(my_obj, type(my_obj["width"]))
print(my_obj["settings"][0]["filename"])

# print(json.dumps(my_obj))

my_obj["settings"][0]["seek"] = 25
my_obj["test_tuple"] = (1,2,3,4,5)
with open("test.json", 'w') as f:
    json.dump(my_obj, f)

print(pickle.dumps(my_obj))
with open("test.pickle", 'wb') as f:
    pickle.dump(my_obj, f)
id_1 = id(my_obj)

with open("test.pickle", 'rb') as f:
    test_obj = pickle.load(f)
    print(test_obj, test_obj == my_obj, test_obj is my_obj)

s = pickle.dumps(print)
new_print = pickle.loads(s)
print(new_print)

new_print("hello from the new_print")

# s = json.dumps(print)


data_v1 = {"model":["80 1.6 Specs", "80 1.6 Specs"],
"year":[1989,1986], "horsepower":[69,75]}

data_v2 = {"data":[{"model":"80 1.6 Specs", "year":1989, "horsepower":69}, 
        {"model":"80 1.8 Specs", "year":1986, "horsepower":75}]}

headline = ["model", "year", "horsepower"]

with open("v2.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headline)
    for line in data_v2["data"]:
        #writer.writerow(list(line.values()))
        row = []
        for key in headline:
            row.append(line[key])
        writer.writerow(row)

with open("v1.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headline)
    for i in range(len(data_v1[headline[0]])):
        row = []
        for key in headline:
            row.append(data_v1[key][i])
        writer.writerow(row)

with open("v1.json", 'w') as f:
    json.dump(data_v1, f)

with open("v2.json", 'w') as f:
    json.dump(data_v2, f)

with open("v1.pickle", 'wb') as f:
    pickle.dump(data_v1, f)

with open("v2.pickle", 'wb') as f:
    pickle.dump(data_v2, f)