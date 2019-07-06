# issue: initiallize a language processer

from bokeh.layouts import widgetbox, layout, Row
from bokeh.plotting import curdoc, figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs, RadioButtonGroup, TextInput
from bokeh.models.widgets import RadioGroup, Select, Paragraph, PreText
from bokeh.models.widgets import Button, DataTable, TableColumn
from bokeh.core.properties import value
from functools import partial

def ChamStatData():
    pass

pre = PreText(text="Korea - Version: 9.13",width=200, height=100)

source = ColumnDataSource({'x' :[1, 2, 3, 4], 'y1':[3, 5, 2, 7], 'y2':[4, 7, 5, 9]})
plot = figure(plot_width=1000, plot_height=500)
plot.line('x','y1',  source=source, line_color="red")
plot.line('x','y2',  source=source, line_color="blue")




# layout

page = layout(
    [widgetbox(pre, width=1000)], 
    [widgetbox(plot, height=500, width=1000)]       
)

# display & interaction
curdoc().add_root(page)



# bokeh serve --show bokeh/bokeh-layout.py