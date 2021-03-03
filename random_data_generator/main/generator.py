import csv
import numpy as np
import random
import string
import json
import click

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

def generatefirst(input, firstN, firstJ, joinsN, columns):
    firsttable = []
    for i in range(0, firstN):
        temprow = {}
        for j in range (0, len(input["columns_first_table"])):
            if (input["columns_first_table"][j][1] == "str"):
                temp = buildstring(random.randint(1, 20))
            if (input["columns_first_table"][j][1] == "int"):
                temp = buildint()
            if (input["columns_first_table"][j][1] == "date"):
                temp = builddate('1970-01-01', 5000)
            if (input["columns_first_table"][j][1] == "double"):
                temp = builddouble()
            if (j == firstJ):
                if (i < joinsN):
                    count = 1
                    while (count != 0):
                        count = 0
                        if (input["columns_first_table"][j][1] == "str"):
                            temp = buildstring(random.randint(1, 15))
                        if (input["columns_first_table"][j][1] == "int"):
                            temp = random.randint(1, 9999)
                        if (input["columns_first_table"][j][1] == "date"):
                            temp = builddate('1970-01-01', 5000)
                        if (input["columns_first_table"][j][1] == "double"):
                            temp = builddouble()
                        for k in range(0, i):
                            if (temp == firsttable[k][columns[firstJ]]):
                                count += 1
                if (i >= joinsN):
                    count = 1
                    while (count != 0):
                        count = 0
                        if (input["columns_first_table"][j][1] == "str"):
                            temp = buildstring(random.randint(1, 15))
                        if (input["columns_first_table"][j][1] == "int"):
                            temp = random.randint(1, 9999)
                        if (input["columns_first_table"][j][1] == "date"):
                            temp = builddate('1970-01-01', 5000)
                        if (input["columns_first_table"][j][1] == "double"):
                            temp = builddouble()
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
            if (input["columns_second_table"][j][1] == "str"):
                temp = buildstring(random.randint(1, 15))
            if (input["columns_second_table"][j][1] == "int"):
                temp = random.randint(1, 9999)
            if (input["columns_second_table"][j][1] == "date"):
                temp = builddate('1970-01-01', 5000)
            if (input["columns_second_table"][j][1] == "double"):
                temp = builddouble()
            if (j == secondJ):
                if (i < joinsN):
                    temp = firsttable[i][columns[firstJ]]
                if (i >= joinsN):
                    count = 1
                    while (count != 0):
                        count = 0
                        if (input["columns_second_table"][j][1] == "str"):
                            temp = buildstring(random.randint(1, 15))
                        if (input["columns_second_table"][j][1] == "int"):
                            temp = random.randint(1, 9999)
                        if (input["columns_second_table"][j][1] == "date"):
                            temp = builddate('1970-01-01', 5000)
                        if (input["columns_second_table"][j][1] == "double"):
                            temp = builddouble()
                        for k in range(0, firstN):
                            if (temp == firsttable[k][columns[firstJ]]):
                                count += 1
                        
            temprow.update({input["columns_second_table"][j][0]: temp})
        secondtable.append(temprow)
    return secondtable

@click.command()
@click.option('--firstN', default=1,
              help='First Table number of rows')
@click.option('--secondN', default=1,
              help='Second Table number of rows')
@click.option('--firstJ', default=0,
              help='First Table join column')
@click.option('--secondJ', default=0,
              help='Second Table join column')
@click.option('--joinsN', default=1,
              help='Number of joined elements')
def generator(firstn, secondn, firstj, secondj, joinsn):
    with open('input.json') as f:
        input = json.load(f)    

    columnsfirst = []

    for j in range (0, len(input["columns_first_table"])):
        columnsfirst.append(input["columns_first_table"][j][0])
    
    
    firsttable = generatefirst(input, firstn, firstj, joinsn, columnsfirst)

    columnssecond = []

    for j in range (0, len(input["columns_second_table"])):
        columnssecond.append(input["columns_second_table"][j][0])

    secondtable = generatesecond(firsttable, input, firstn, secondn, firstj, secondj, joinsn, columnsfirst)

    FILENAME = "firsttable.csv"

    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columnsfirst)
        writer.writeheader()
        writer.writerows(firsttable)
            
    FILENAME = "secondtable.csv"
    
    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columnssecond)
        writer.writeheader()
        writer.writerows(secondtable)

if __name__ == '__main__':
    generator()
