"""
    Ramen lover project
    Top 10 Countries that make a lot of ramen brand
    Bar chart

"""

import pygal, pandas
from pygal.style import DefaultStyle

def brand():
    """ brandbar """

    data_use = pandas.read_csv("ramen-ratings.csv", encoding = "utf-8")

    brand_data = {}

    for row in range(2580):
        if data_use["Country"][row] not in brand_data:
            brand_data[data_use["Country"][row]] = 1
        elif data_use["Country"][row] in brand_data:
            brand_data[data_use["Country"][row]] += 1

    brand_data = dict(sorted(brand_data.items(), key=lambda x: x[1]))
    count = 0
    branddict = {}
    for i in brand_data:
        if count >= 28:
            branddict[i] = brand_data[i]
        count += 1

    print(branddict)
    bar_chart = pygal.Bar(fill=True, interpolate='cubic', style=DefaultStyle)
    bar_chart.title = 'Top 10 Countries that make a lot of ramen brand'
    for i in branddict:
        bar_chart.add(i, branddict[i])
        bar_chart.legend_at_bottom = True
        bar_chart.legend_box_size = 16
    bar_chart.render_to_file('TopCountries.svg')

brand()
