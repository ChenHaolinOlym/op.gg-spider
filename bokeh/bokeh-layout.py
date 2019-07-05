from bokeh.layouts import widgetbox, layout, Row
from bokeh.plotting import curdoc, figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs, RadioButtonGroup, TextInput
from bokeh.models.widgets import RadioGroup, Select, Paragraph
from bokeh.models.widgets import Button, DataTable, TableColumn
from bokeh.core.properties import value
from functools import partial




# layout

page = layout(
    [widgetbox(tabs, width=1000)]       
)

# display & interaction
curdoc().add_root(page)