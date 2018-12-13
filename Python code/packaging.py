"""
    Ramen lover project
    Most packageing in Thailand
    PIE chart

"""

import pygal, pandas
from pygal.style import DefaultStyle

def packthai():
    """ ThaiPackPie """

    data_use = pandas.read_csv("ramen-ratings.csv", encoding = "utf-8")

    pack_data = {}

    for row in range(2580):
        if data_use["Country"][row] == "Thailand" and data_use["Style"][row] not in pack_data:
            pack_data[data_use["Style"][row]] = 1
        elif data_use["Country"][row] == "Thailand":
            pack_data[data_use["Style"][row]] += 1
    pack_data = dict(sorted(pack_data.items(), key=lambda x: x[1]))

    pie_chart = pygal.Pie(inner_radius=.75)
    pie_chart.title = 'Most packaging in Thailand'
    for i in pack_data:
        pie_chart.add(i, pack_data[i])
    pie_chart.render_to_file('PackagingThai.svg')

packthai()
