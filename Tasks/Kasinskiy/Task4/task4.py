while True:
    s = int(input("Enter the desired string length more than 35 characters: "))
    if s <= 35:
        print('you must enter an integer > 35')
        continue
    break
with open("text.txt", "r") as f:
    flag = True
    pos = 1
    while flag:
        t = f.read(s+1)
        if t[0] == ' ':
            pos += 1
        if t[len(t)-1] == " " or len(t) < s:
            m = t.split()
        else:
            m = t.split()
            m.pop()
        t1 = " ".join(m)
        pos = pos + len(t1)
        f.seek(pos)
        count = s - len(t1)
        while count > 0:
            if len(m) == 1:
                break
            for i in range(1, len(m)):
                m[i] = " " + m[i]
                count -= 1
                k = len(m)-i
                if count > 0 and (k - i) >= 1:
                    m[k] = " " + m[k]
                    count -= 1
                else:
                    break
                if (k - i) <= 1 or count == 0:
                    break
        t1 = " ".join(m)
        with open("your_text.txt", "a") as f1:
            f1.write(t1+'\n')
        if len(t) < s:
            flag = False
