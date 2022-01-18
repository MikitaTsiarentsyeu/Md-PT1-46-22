from datetime import datetime           # import class
curTime = str(datetime.now().time())    # get current time as a string
CT = list(curTime)[0:8]                 # turn string to list splitting milliseconds
print("".join(CT))                      # output of current time as a string

usersCurTime = input("Enter current time in hh:mm format:")     #input of current time
timeDict = {"00":"двенадцать часов", "01":"час", "02":"два часа", "03":"три часа", "04":"четыре часа", "05":"пять часов",
                "06":"шесть часов", "07":"семь часов", "08":"восемь часов", "09":"девять часов", "10":"десять часов", 
                "11":"одиннадцать часов", "12":"двенадцать часов", "13":"час", "14":"два часа", "15":"три часа", "16":"четыре часа",
                "17":"пять часов", "18":"шесть часов", "19":"семь часов", "20":"восемь часов", "21":"девять часов", "22":"десять часов",
                "23":"одиннадцать часов"}   # define dictionary with time mapping
print(usersCurTime)