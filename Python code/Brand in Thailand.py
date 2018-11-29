"""
    ***Ramen lover project***
    Title: Brands in Thailand
    Chart type: Bar

"""

import pygal, pandas
from pygal.style import DefaultStyle

def brandthai():
    """ Thaibrandbar """

data_use = pandas.read_csv("ramen-ratings.csv", encoding = "utf-8")

brand_data = {}

for row in range(2580):
    if data_use["Country"][row] == "Thailand" and data_use["Brand"][row] not in brand_data:
        brand_data[data_use["Brand"][row]] = 1
    elif data_use["Country"][row] == "Thailand":
        brand_data[data_use["Brand"][row]] += 1

brand_data = dict(sorted(brand_data.items(), key=lambda x: x[1]))

bar_chart = pygal.Bar(fill=True, interpolate='cubic', style=DefaultStyle)
bar_chart.title = 'Ramen Brands in Thailand'
for i in brand_data:
    bar_chart.add(i, brand_data[i])
    bar_chart.legend_at_bottom = True
    bar_chart.legend_box_size = 16
bar_chart.render_to_file('Brand_Thailand.svg')



brandthai()
