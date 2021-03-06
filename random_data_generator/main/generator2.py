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

def generatesecond(firsttable, input, firstN, secondN, firstJ, secondJ, joinsN, columns):
    secondtable = []
    for i in range(0, secondN):
        temprow = {}
        for j in range (0, len(input["columns_second_table"])):
            temp = buildelement(input["columns_second_table"][j][1])
            if (j == secondJ):
                if (i < joinsN):
                    temp = firsttable[i][columns[firstJ]]
                if (i >= joinsN):
                    count = 1
                    while (count != 0):
                        count = 0
                        temp = buildelement(input["columns_second_table"][j][1])
                        for k in range(0, firstN):
                            if (temp == firsttable[k][columns[firstJ]]):
                                count += 1
                        
            temprow.update({input["columns_second_table"][j][0]: temp})
        secondtable.append(temprow)
    return secondtable


@click.command()
@click.option('--firstName', default='firsttable.csv',
              help='Name of the firsttable')
@click.option('--secondN', default=1,
              help='Second Table number of rows')
@click.option('--firstJ', default=0,
              help='First Table join column')
@click.option('--secondJ', default=0,
              help='Second Table join column')
@click.option('--joinsN', default=1,
              help='Number of joined elements')

def generator(firstname, secondn, firstj, secondj, joinsn):
    with open('input.json') as f:
        input = json.load(f)    

    FILENAME = firstname

    with open(FILENAME, "r", newline="") as file:
        firsttable = list(csv.DictReader(file, delimiter = ','))
    
    
    firstn = len(firsttable)
    

    columnsfirst = list(dict(firsttable[0]))

    columnssecond = []

    for j in range (0, len(input["columns_second_table"])):
        columnssecond.append(input["columns_second_table"][j][0])

    secondtable = generatesecond(firsttable, input, firstn, secondn, firstj, secondj, joinsn, columnsfirst)

    FILENAME = "secondtable.csv"

    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columnssecond)
        writer.writeheader()
        writer.writerows(secondtable)

if __name__ == '__main__':
    generator()
