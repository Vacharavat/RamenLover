"""
    Ramen lover project
    Most Variety in Thailand
    SolidGauge chart

"""

import pygal, pandas
from pygal.style import DefaultStyle

def varietythai():
    """ Thaivariety """

    data_use = pandas.read_csv("ramen-ratings.csv", encoding = "utf-8")

    data = {}

    for row in range(2580):
        if data_use["Country"][row] == "Thailand":
            data[data_use["Variety"][row]] = data_use["Stars"][row]

    data = dict(sorted(data.items(), key=lambda x: x[1]))
    count = 0
    dadict = {}
    for i in data:
        if count >= 158:
            dadict[i] = data[i]
        count += 1

    dadict = dict(sorted(dadict.items(), key=lambda x: x[1]))

    solid_chart = pygal.SolidGauge(half_pie=True, inner_radius=0.70,style=pygal.style.styles['default'](value_font_size=10))
    solid_chart.title = 'Top 20 Flavour in Thailand (Arrange by star)'
    for i in dadict:
        solid_chart.add(i, [{"value": float(dadict[i]), 'max_value': 5}])
    solid_chart.legend_at_bottom = True
    solid_chart.legend_box_size = 16
    solid_chart.render_to_file('TopFlavourThai.svg')

varietythai()
