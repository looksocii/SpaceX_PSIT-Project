""" Project : Road Accident
    Team    : Space X
    Data    : Age
    Year    : 2015
"""

def age():
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

    # Age Variable
    age_all = []

    # Total Data
    num2 = 0
    for i in data_list:
        # Check Less than 112 years old
        if int(i[5]) < 112:
            age_all.append(int(i[5]))

    # Frequency Check
    age = histogram(age_all)[0]
    his = histogram(age_all)[1]

    # Create a graph
    graph = pg.Bar(show_minor_x_labels=False, truncate_legend=40, \
    legend_at_bottom=True, truncate_label=100)
    # graph title
    graph.title = 'ความถี่อายุของผู้ที่เกิดอุบัติเหตุทางถนนในปี 2015'
    # X-Axis Label ---> (Age)
    graph.x_labels = age
    # Y-Axis and label ---> (Histogram)
    graph.add('ความถี่ที่เกิดอุบัติเหตุในแต่ละช่วงอายุ', his)
    # Range of Y-Axis value
    graph.range = [1, 1000]
    # Save graph into file
    graph.render_to_file('graph_age.svg')

    #Show information
    print("Age\t: %d" %len(age))
    print("Data\t: %d" %num)
    print("Year\t: 20%s" %data_list[0][1])

def histogram(lst):
    """ Function is Frequency Check """
    dic = {}
    lst2 = []
    lst3 = []
    total = []
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        lst2.append(i)
    lst2.sort()
    for i in lst2:
        lst3.append(dic[i])
    total = [lst2, lst3]
    return total

age()
