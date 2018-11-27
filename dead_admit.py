""" Project : Road Accident
    Team    : Space X
    Data    : Dead, Admit
    Year    : 2015
"""

def dead_admit():
    import csv
    import pygal as pg

    # Open File csv
    file = open('AccidentDataset.csv')
    data = csv.reader(file)
    table = [row for row in data]

    # data_list = [[MONTH, YEAR, ADMIT, DEAD, GENDER, AGE], [MONTH, YEAR, ADMIT, DEAD, GENDER, AGE]]
    num = 0
    data_list = []
    for i in range(0, len(table)):
        # ----------> Check Year <----------
        if table[i][4] == "15":
            num += 1
            data_list.append([table[i][3], table[i][4], table[i][6], table[i][7], \
                table[i][17], table[i][18]])

    # Dead Variable
    dead_list = []
    dead_month1, dead_month2, dead_month3, dead_month4, dead_month5, dead_month6, dead_month7, \
    dead_month8, dead_month9, dead_month10, dead_month11, dead_month12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # Admit Variable
    admit_list = []
    admit_month1, admit_month2, admit_month3, admit_month4, admit_month5, admit_month6, admit_month7, \
    admit_month8, admit_month9, admit_month10, admit_month11, admit_month12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # Total Data
    for i in data_list:
        # Check Month
        if i[0] == "1":
            dead_month1 += int(i[3])
            admit_month1 += int(i[2])
        elif i[0] == "2":
            dead_month2 += int(i[3])
            admit_month2 += int(i[2])
        elif i[0] == "3":
            dead_month3 += int(i[3])
            admit_month3 += int(i[2])
        elif i[0] == "4":
            dead_month4 += int(i[3])
            admit_month4 += int(i[2])
        elif i[0] == "5":
            dead_month5 += int(i[3])
            admit_month5 += int(i[2])
        elif i[0] == "6":
            dead_month6 += int(i[3])
            admit_month6 += int(i[2])
        elif i[0] == "7":
            dead_month7 += int(i[3])
            admit_month7 += int(i[2])
        elif i[0] == "8":
            dead_month8 += int(i[3])
            admit_month8 += int(i[2])
        elif i[0] == "9":
            dead_month9 += int(i[3])
            admit_month9 += int(i[2])
        elif i[0] == "10":
            dead_month10 += int(i[3])
            admit_month10 += int(i[2])
        elif i[0] == "11":
            dead_month11 += int(i[3])
            admit_month11 += int(i[2])
        elif i[0] == "12":
            dead_month12 += int(i[3])
            admit_month12 += int(i[2])

    # 12 Month in dead_list
    # dead_list = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    dead_list.append([dead_month1, dead_month2, dead_month3, dead_month4, dead_month5, \
    dead_month6, dead_month7, dead_month8, dead_month9, dead_month10, dead_month11, dead_month12])
    dead_list = dead_list[0]

    # 12 Month in admit_list
    # admit_list = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    admit_list.append([admit_month1, admit_month2, admit_month3, admit_month4, admit_month5, \
    admit_month6, admit_month7, admit_month8, admit_month9, admit_month10, admit_month11, admit_month12])
    admit_list = admit_list[0]

    # Create a graph by pygal
    graph = pg.Line(x_labels_major_count=12, show_minor_x_labels=True, truncate_legend=40, \
    legend_at_bottom=False, truncate_label=100)
    # graph title
    graph.title = 'อัตราการเกิดอุบัติเหตุทางถนนในปี 2015'
    # X-Axis Label ---> (Month)
    graph.x_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', \
    'September', 'October', 'November', 'December']
    # Y-Axis and label ---> (Data)
    graph.add('Dead', dead_list)
    graph.add('Admit', admit_list)
    # Range of Y-Axis value
    graph.range = [1, 7000]
    # Save graph into file
    graph.render_to_file('graph_dead_admit.svg')

    #Show information
    print("Dead\t:", dead_list)
    print("Admit\t:", admit_list)
    print("Data\t: %d" %num)
    print("Year\t: 20%s" %data_list[0][1])

dead_admit()
