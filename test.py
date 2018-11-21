"""DATA"""

def main(num):
    import csv
    #import pygal as pg

    # Open File csv
    file = open('AccidentDataset.csv')
    data = csv.reader(file)
    table = [row for row in data]

    # data_list = [[MONTH, YEAR, ADMIT, DEAD, GENDER, AGE], [MONTH, YEAR, ADMIT, DEAD, GENDER, AGE]]
    data_list = []
    for i in range(0, len(table)):
        if table[i][2] == "15":
            num += 1
            data_list.append([table[i][1], table[i][2], table[i][3], table[i][4], \
                table[i][5], table[i][6]])

    # Deaths in 20xx
    dead_list_2015 = []

    # Deaths of month
    dead_month1, dead_month2, dead_month3, dead_month4, dead_month5, dead_month6, dead_month7, \
    dead_month8, dead_month9, dead_month10, dead_month11, dead_month12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # Total Deaths of month
    for i in data_list:
        if i[0] == "1":
            dead_month1 += int(i[3])
        elif i[0] == "2":
            dead_month2 += int(i[3])
        elif i[0] == "3":
            dead_month3 += int(i[3])
        elif i[0] == "4":
            dead_month4 += int(i[3])
        elif i[0] == "5":
            dead_month5 += int(i[3])
        elif i[0] == "6":
            dead_month6 += int(i[3])
        elif i[0] == "7":
            dead_month7 += int(i[3])
        elif i[0] == "8":
            dead_month8 += int(i[3])
        elif i[0] == "9":
            dead_month9 += int(i[3])
        elif i[0] == "10":
            dead_month10 += int(i[3])
        elif i[0] == "11":
            dead_month11 += int(i[3])
        elif i[0] == "12":
            dead_month12 += int(i[3])

    # dead_list_20xx = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    dead_list_2015.append([dead_month1, dead_month2, dead_month3, dead_month4, dead_month5, \
            dead_month6, dead_month7, dead_month8, dead_month9, dead_month10, dead_month11, dead_month12])
    dead_list_2015 = dead_list_2015[0]

    #print(dead_list_2015)
    #print("DATA : %d" %num)
    #print("YEAR : 20%s" %data_list[0][1])

    chart = pg.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, \
        legend_at_bottom=True, truncate_label=100)
    # Chart title
    chart.title = 'Deaths in 2015'
    # X-Axis Label
    chart.x_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', \
    'September', 'October', 'November', 'December']
    # Y-Axis and label
    chart.add('อัตราการตายของปี 2015', dead_list_2015)
    # Range of Y-Axis value
    chart.range = [1, 2100]
    # Save chart into file
    chart.render_to_file('chart.svg')

main(0)
