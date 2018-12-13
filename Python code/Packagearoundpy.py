"""
    Ramen lover project
    Most packageing around the world
    PIE chart

"""

import pygal, pandas
from pygal.style import DefaultStyle

def packaround():
    """ Package around """

    data_use = pandas.read_csv("ramen-ratings.csv", encoding = "utf-8")

    pack_data = {}

    for row in range(2580):
        if data_use["Style"][row] not in pack_data:
            pack_data[data_use["Style"][row]] = 1
        elif data_use["Style"][row] in pack_data:
            pack_data[data_use["Style"][row]] += 1
    pack_data = dict(sorted(pack_data.items(), key=lambda x: x[1]))


    count = 0
    packdict = {}
    for i in pack_data:
        if count >= 3:
            packdict[i] = pack_data[i]
        count += 1

    pie_chart = pygal.Pie(half_pie=True)
    pie_chart.title = 'Top 5 Packaging around the world'
    for i in packdict:
        pie_chart.add(i, [{"value": packdict[i]}])
    pie_chart.render_to_file('PackagingAround.svg')


packaround()
