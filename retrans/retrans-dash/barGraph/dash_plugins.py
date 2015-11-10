'''
__author__ = 'David Arellano'
__date__ = '7/9/2015'
'''

from django.utils.translation import ugettext_lazy as _
from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory
from dash_widgets import BaseBarGraphWidget
from forms import BarGraphForm
from update_widget import update_graph

class BaseBarGraphPlugin(BaseDashboardPlugin):

    name = _("BarGraph")
    group = _("Charts")
    form = BarGraphForm
    
    def update_plugin_data(self, dashboard_entry):
        return update_graph(self)

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
    (4, 6),
    (5, 4),
    (5, 5),
    (6, 4),
    (6, 5),
    (6, 3),
)

plugin_factory(BaseBarGraphPlugin, 'bar_graph', sizes)

# ********************************************************************************
# ********************************* Registering widgets **************************
# ********************************************************************************

# Registering chart plugin widgets
plugin_widget_factory(BaseBarGraphWidget, 'android', 'main', 'bar_graph', sizes)
plugin_widget_factory(BaseBarGraphWidget, 'windows8', 'main', 'bar_graph', sizes)
plugin_widget_factory(BaseBarGraphWidget, 'bootstrap2_fluid', 'main', 'bar_graph', sizes)
plugin_widget_factory(BaseBarGraphWidget, 'testing', 'main', 'bar_graph', sizes)
