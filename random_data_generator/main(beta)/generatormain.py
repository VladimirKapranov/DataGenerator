import csv
import numpy as np
import random
import string
import json
import click
import generatorfunc

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

    firsttable = generatorfunc.generatefirst(input, firstn, firstj, joinsn, columnsfirst)

    columnssecond = []

    for j in range (0, len(input["columns_second_table"])):
        columnssecond.append(input["columns_second_table"][j][0])

    secondtable = generatorfunc.generatesecond(firsttable, input, firstn, secondn, firstj, secondj, joinsn, columnsfirst)

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
