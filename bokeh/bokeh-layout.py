from bokeh.layouts import widgetbox, layout, Row
from bokeh.plotting import curdoc, figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs, RadioButtonGroup, TextInput
from bokeh.models.widgets import RadioGroup, Select, Paragraph
from bokeh.models.widgets import Button, DataTable, TableColumn
from bokeh.core.properties import value
from functools import partial

def ChamStatData():
    pass


plot = figure(plot_width=500, plot_height=500)
plot.multi_line([[1, 2, 3, 4, 5, 6, 7], [5, 9, 3]],[[5, 4, 9, 2, 6, 2, 0], [7, 3, 4]],
    line_alpha=['1.0','0.2'], line_color=['blue', 'red'], line_width=[1, 10])




# layout

page = layout(
    [widgetbox(plot, width=1000)]       
)

# display & interaction
curdoc().add_root(page)