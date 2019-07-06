# issue: initiallize a language processer

from bokeh.layouts import widgetbox, layout, Row
from bokeh.plotting import curdoc, figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs, RadioButtonGroup, TextInput
from bokeh.models.widgets import RadioGroup, Select, Paragraph, PreText
from bokeh.models.widgets import Button, DataTable, TableColumn
from bokeh.core.properties import value
from functools import partial
import pandas as pd

def ChamStatData():
    pass

def onClick(part, value):
    if part == 'Postion':
        pass

    if part == 'Type':
        pass

btnGroupPosition = RadioButtonGroup(labels=['All', 'Top', 'Jug', 'Mid', 'ADC', 'Sup'], active=0)
btnGroupType = RadioButtonGroup(labels=['Win Rate', 'Pick Rate', 'Ban Rate'], active=0)


btnGroupPosition.on_click(partial(onClick, 'Position'))
btnGroupType.on_click(partial(onClick, 'Type'))


pre = PreText(text="Korea - Version: 9.13",width=200, height=100)

source = ColumnDataSource({'x' :[1, 2, 3, 4], 'y1':[3, 5, 2, 7], 'y2':[4, 7, 5, 9]})
plot = figure(plot_width=1000, plot_height=500,
    x_range=[0, 10], y_range=[0, 10],
    x_axis_label='Days', x_axis_type='datetime', y_axis_label='percent of ')
plot.line('x','y1',  source=source, line_color="red")
plot.line('x','y2',  source=source, line_color="blue")










# layout

page = layout(
    [widgetbox(pre, width=1000)], 
    [widgetbox(plot, height=500, width=1000)],
    [widgetbox(btnGroupPosition, btnGroupType)]       
)

# display & interaction
curdoc().add_root(page)





# bokeh serve --show bokeh/bokeh-layout.py





# available corlors
# 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple',
# 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'