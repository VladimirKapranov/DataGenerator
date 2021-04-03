import numpy as np
import random
import string

def buildstring(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def builddate(basedate, n):
    days = np.arange(0, n)
    date = np.datetime64(basedate) + np.random.choice(days)
    return date

def buildint():
    return random.randint(-2147483648, 2147483647)

def builddouble():
    return random.uniform(-100000, 100000)

def buildelement(type):
    if (type == "str"):
        temp = buildstring(random.randint(1, 20))
    if (type == "int"):
        temp = buildint()
    if (type == "date"):
        temp = builddate('1970-01-01', 5000)
    if (type == "double"):
        temp = builddouble()
    return temp

def generatefirst(input, firstN, firstJ, joinsN, columns):
    firsttable = []
    for i in range(0, firstN):
        temprow = {}
        for j in range (0, len(input["columns_first_table"])):
            temp = buildelement(input["columns_first_table"][j][1])
            if (j == firstJ):
                if (i < joinsN):
                    count = 1
                    while (count != 0):
                        count = 0
                        temp = buildelement(input["columns_first_table"][j][1])
                        for k in range(0, i):
                            if (temp == firsttable[k][columns[firstJ]]):
                                count += 1
                if (i >= joinsN):
                    count = 1
                    while (count != 0):
                        count = 0
                        temp = buildelement(input["columns_first_table"][j][1])
                        for k in range(0, joinsN):
                            if (temp == firsttable[k][columns[firstJ]]):
                                count += 1
            temprow.update({input["columns_first_table"][j][0]: temp})
        firsttable.append(temprow)
    return firsttable

def generatesecond(firsttable, input, firstN, secondN, firstJ, secondJ, joinsN, columns):
    secondtable = []
    for i in range(0, secondN):
        temprow = {}
        for j in range (0, len(input["columns_second_table"])):
            temp = buildelement(input["columns_first_table"][j][1])
            if (j == secondJ):
                if (i < joinsN):
                    temp = firsttable[i][columns[firstJ]]
                if (i >= joinsN):
                    count = 1
                    while (count != 0):
                        count = 0
                        temp = buildelement(input["columns_first_table"][j][1])
                        for k in range(0, firstN):
                            if (temp == firsttable[k][columns[firstJ]]):
                                count += 1
                        
            temprow.update({input["columns_second_table"][j][0]: temp})
        secondtable.append(temprow)
    return secondtable