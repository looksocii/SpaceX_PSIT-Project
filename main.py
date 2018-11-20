"""DATA"""

def main(num):
    import csv

    file = open('AccidentDataset.csv')
    data = csv.reader(file)
    table = [row for row in data]

    print("MONTH\tYEAR\tADMIT\tDEAD\tGENDER\tAGE\tPROVINCE")
    for i in range(1, len(table)):
        if table[i][2] == "16":
            num += 1
            print(table[i][1]+"\t"+table[i][2]+"\t"+table[i][3]+"\t"+\
                table[i][4]+"\t"+table[i][6]+"\t"+table[i][5]+"\t"+table[i][7][-2:])
    print("DATA : %d" %num)

main(0)
