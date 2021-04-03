import csv
import numpy as np
import random
import string
import json
import click
import generatorfunc


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

    secondtable = generatorfunc.generatesecond(firsttable, input, firstn, secondn, firstj, secondj, joinsn, columnsfirst)

    FILENAME = "secondtable.csv"

    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columnssecond)
        writer.writeheader()
        writer.writerows(secondtable)

if __name__ == '__main__':
    generator()