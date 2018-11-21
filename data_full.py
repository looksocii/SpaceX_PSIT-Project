""" Project : Road Accident
    Team    : Space X
    Data    : All Data
    Year    : 2005 - 2018
"""

def alldata():
    import pandas as pd

    # Open File csv
    datafull = pd.read_csv('AccidentDataset.csv', delimiter=',')
    print(datafull)

alldata()
