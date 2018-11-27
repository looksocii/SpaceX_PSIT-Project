""" Project : Road Accident
    Team    : Space X
    Data    : Gender
    Year    : 2015
"""

def gender():
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

    # Male Variable
    male_list = []
    male_month1, male_month2, male_month3, male_month4, male_month5, male_month6, male_month7, \
    male_month8, male_month9, male_month10, male_month11, male_month12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # Female Variable
    female_list = []
    female_month1, female_month2, female_month3, female_month4, female_month5, female_month6, female_month7, \
    female_month8, female_month9, female_month10, female_month11, female_month12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # Total Data
    for i in data_list:
        # Check Month
        if i[0] == "1":
            if i[4] == "1":
                male_month1 += 1
            else:
                female_month1 += 1
        elif i[0] == "2":
            if i[4] == "1":
                male_month2 += 1
            else:
                female_month2 += 1
        elif i[0] == "3":
            if i[4] == "1":
                male_month3 += 1
            else:
                female_month3 += 1
        elif i[0] == "4":
            if i[4] == "1":
                male_month4 += 1
            else:
                female_month4 += 1
        elif i[0] == "5":
            if i[4] == "1":
                male_month5 += 1
            else:
                female_month5 += 1
        elif i[0] == "6":
            if i[4] == "1":
                male_month6 += 1
            else:
                female_month6 += 1
        elif i[0] == "7":
            if i[4] == "1":
                male_month7 += 1
            else:
                female_month7 += 1
        elif i[0] == "8":
            if i[4] == "1":
                male_month8 += 1
            else:
                female_month8 += 1
        elif i[0] == "9":
            if i[4] == "1":
                male_month9 += 1
            else:
                female_month9 += 1
        elif i[0] == "10":
            if i[4] == "1":
                male_month10 += 1
            else:
                female_month10 += 1
        elif i[0] == "11":
            if i[4] == "1":
                male_month11 += 1
            else:
                female_month11 += 1
        elif i[0] == "12":
            if i[4] == "1":
                male_month12 += 1
            else:
                female_month12 += 1

    # 12 Month in male_list
    # male_list = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    male_list.append([male_month1, male_month2, male_month3, male_month4, male_month5, \
    male_month6, male_month7, male_month8, male_month9, male_month10, male_month11, male_month12])
    male_list = male_list[0]

    # 12 Month in female_list
    # female_list = [xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]
    female_list.append([female_month1, female_month2, female_month3, female_month4, female_month5, \
    female_month6, female_month7, female_month8, female_month9, female_month10, female_month11, female_month12])
    female_list = female_list[0]

    # Create a graph
    graph = pg.Bar(x_labels_major_count=12, show_minor_x_labels=True, truncate_legend=40, \
    legend_at_bottom=False, truncate_label=100)
    # graph title
    graph.title = 'อัตราผู้เกิดอุบัติเหตุแยกตามเพศในปี 2015'
    # X-Axis Label ---> (Month)
    graph.x_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', \
    'September', 'October', 'November', 'December']
    # Y-Axis and label ---> (Gander)
    graph.add('Male', male_list)
    graph.add('Female', female_list)
    # Range of Y-Axis value
    graph.range = [1, 4000]
    # Save graph into file
    graph.render_to_file('graph_gender01.svg')

    # Total All data
    male_all = sum(male_list)
    female_all = sum(female_list)

    # Create a total graph
    graph = pg.Pie()
    # graph title
    graph.title = 'อัตราผู้เกิดอุบัติเหตุแยกตามเพศในปี 2015'
    # Variable ---> (Gander)
    graph.add('Male', male_all)
    graph.add('Female', female_all)
    # Save graph into file
    graph.render_to_file('graph_gender02.svg')

    #Show information
    print("Male\t:", male_list)
    print("Female\t:", female_list)
    print("Data\t: %d" %num)
    print("Year\t: 20%s" %data_list[0][1])

gender()
