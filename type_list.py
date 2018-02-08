l = ['magical unicorns',19,'hello',98.98,'world']
m = [2,3,1,7,4,12]
n = ['magical','unicorns']

def listType(varList):
    strString = "String: "
    sum = 0
    strings = 0
    ints = 0
    for val in varList:
        if isinstance(val, str):
            strings += 1
            strString += val + " "
        elif isinstance(val, int) or isinstance(val, float):
            ints += 1
            sum += val

    if ints != 0 and strings !=0:
        print ("The list you entered is of mixed type")
        print (strString)
        print ("Sum: " + str(sum))
    elif strings != 0:
        print ("The list you entered is of string type")
        print (strString)
    elif ints != 0:
        print ("The list you entered is of numberical type")
        print ("Sum: " + str(sum))

listType()