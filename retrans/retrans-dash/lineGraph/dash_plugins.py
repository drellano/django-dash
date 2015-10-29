'''
__author__ = 'David Arellano'
__date__ = '7/9/2015'
'''

from django.utils.translation import ugettext_lazy as _
from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory
from dash_widgets import BaseLineGraphWidget
from forms import LineGraphForm
from update_widget import update_fuel_table

class BaseLineGraphPlugin(BaseDashboardPlugin):

    name = _("LineGraph")
    group = _("Charts")
    form = LineGraphForm

    def update_plugin_data(self, dashboard_entry):
        return update_fuel_table(self)
# ********************************************************************************
# ********** Generating and registering the plugins using factory ****************
# ********************************************************************************
sizes = (
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
    (3, 4),
    (4, 3),
    (4, 4),
    (4, 5),
    (5, 4),
    (5, 5),
    (6, 4),
    (6, 5),
    (6,3),
)

plugin_factory(BaseLineGraphPlugin, 'line_graph', sizes)

# ********************************************************************************
# ********************************* Registering widgets **************************
# ********************************************************************************

# Registering chart plugin widgets
plugin_widget_factory(BaseLineGraphWidget, 'android', 'main', 'line_graph', sizes)
plugin_widget_factory(BaseLineGraphWidget, 'windows8', 'main', 'line_graph', sizes)
plugin_widget_factory(BaseLineGraphWidget, 'bootstrap2_fluid', 'main', 'line_graph', sizes)
plugin_widget_factory(BaseLineGraphWidget, 'testing', 'main', 'line_graph', sizes)
