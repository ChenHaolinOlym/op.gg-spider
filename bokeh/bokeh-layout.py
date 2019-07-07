# issue: initiallize a language processer


# imports
from bokeh.layouts import widgetbox, layout, Row
from bokeh.plotting import curdoc, figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs, RadioButtonGroup, TextInput
from bokeh.models.widgets import RadioGroup, Select, Paragraph, PreText
from bokeh.models.widgets import Button, DataTable, TableColumn, Slider, RangeSlider
from bokeh.core.properties import value
from functools import partial
import pandas as pd



## function definitions
# callbacks
def ChamStatData():
    pass

def onClick(part, value):
    if part == 'Postion':
        pass

    if part == 'Type':
        pass

def onChange(part, attr, old, new):
    pass

# widget gettings




# layouts
patch = Paragraph(text="Korea - Version : 9.13")







## Change Chart -- layout1
# widgets
btnGroupPosition1 = RadioButtonGroup(labels=['All', 'Top', 'Jug', 'Mid', 'ADC', 'Sup'], active=0)
table_data = dict(
    course_ID=[1, 2, 3, 4],
    title=[6, 3, 8, 3],
    department=[6, 0, 3, 2],
    credit=[4, 8, 3, 0],
    instructor=[5, 2, 6, 4]
    )
columns = [
        TableColumn(field="course_ID", title="Course ID"),
        TableColumn(field="title", title="Title"),
        TableColumn(field="department", title="Department"),
        TableColumn(field="credit", title="Credit"),
        TableColumn(field="instructor", title="Instructor")
    ]
data_source = ColumnDataSource(table_data)
table1 = DataTable(source=data_source, columns=columns, width=1000, height=1000)

# callbacks
btnGroupPosition1.on_click(partial(onClick, 'Position1'))





## Change Plot -- layout2
# widgets
btnGroupPosition2 = RadioButtonGroup(labels=['All', 'Top', 'Jug', 'Mid', 'ADC', 'Sup'], active=0)
btnGroupType1 = RadioButtonGroup(labels=['Win Rate', 'Pick Rate', 'Ban Rate'], active=0)

# callbacks
btnGroupPosition2.on_click(partial(onClick, 'Position2'))
btnGroupType1.on_click(partial(onClick, 'Type1'))





## Data Chart -- layout3
# widgets
btnGroupPosition3 = RadioButtonGroup(labels=['All', 'Top', 'Jug', 'Mid', 'ADC', 'Sup'], active=0)
table_data = dict(
    course_ID=[1, 2, 3, 4],
    title=[6, 3, 8, 3],
    department=[6, 0, 3, 2],
    credit=[4, 8, 3, 0],
    instructor=[5, 2, 6, 4]
    )
columns = [
        TableColumn(field="course_ID", title="Course ID"),
        TableColumn(field="title", title="Title"),
        TableColumn(field="department", title="Department"),
        TableColumn(field="credit", title="Credit"),
        TableColumn(field="instructor", title="Instructor")
    ]
data_source = ColumnDataSource(table_data)
table2 = DataTable(source=data_source, columns=columns, width=1000, height=1000)


# callbacks
btnGroupPosition3.on_click(partial(onClick, 'Position3'))



## Data Plot -- layout4
# widgets
btnGroupPosition2 = RadioButtonGroup(labels=['All', 'Top', 'Jug', 'Mid', 'ADC', 'Sup'], active=0)
btnGroupType4 = RadioButtonGroup(labels=['Win Rate', 'Pick Rate', 'Ban Rate'], active=0)
source = ColumnDataSource({'x' :[1, 2, 3, 4], 'y1':[3, 5, 2, 7], 'y2':[4, 7, 5, 9]})
plot = figure(plot_width=1000, plot_height=600,
    x_range=[0, 10], y_range=[0, 10],
    x_axis_label='Days', x_axis_type='datetime', y_axis_label='percent of ')
plot.line('x','y1',  source=source, line_color="red")
plot.line('x','y2',  source=source, line_color="blue")


# callbacks
btnGroupPosition2.on_click(partial(onClick, 'Position2'))
btnGroupType4.on_click(partial(onClick, 'Type4'))










# layouts
layout1 = layout(
    table1
)

layout2 = layout(
    [widgetbox(btnGroupType4), widgetbox(btnGroupPosition2)],
    [widgetbox(patch, plot, height=500, width=1000)]
)

layout3 = layout(
    table2
)

layout4 = layout(
    [widgetbox(btnGroupType4), widgetbox(btnGroupPosition2)],
    [widgetbox(patch, plot, height=500, width=1000)]
)









tab1 = Panel(child=layout1, title='Change Chart')
tab2 = Panel(child=layout2, title='Change Plot')
tab3 = Panel(child=layout3, title='Data Chart')
tab4 = Panel(child=layout4, title='Data Plot')
tabs = Tabs(tabs=[tab1, tab2, tab3, tab4])








# layout

page = layout(
    [widgetbox(tabs)]
)

# page = layout(
#     [widgetbox(btnGroupType), widgetbox(btnGroupPosition)],
#     [widgetbox(patch, plot, height=500, width=1000)],      
# )

# display & interaction
curdoc().add_root(page)





# bokeh serve --show bokeh/bokeh-layout.py





# available corlors
# 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple',
# 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'