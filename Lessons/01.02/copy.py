chunk = 100

with open("IMG_2436.JPG", "rb") as donor:
    with open("IMG_2436_copy.JPG", "wb") as receiver:
        while True:
            file_part = donor.read(chunk)
            if file_part:
                receiver.write(file_part)
            else:
                break

print("done")