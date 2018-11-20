"""DATA_FULL"""

def datafull():
    import pandas as pd

    datafull = pd.read_csv('AccidentDataset.csv', encoding = "ISO-8859-1")
    print(datafull)

datafull()
