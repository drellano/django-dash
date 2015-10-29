'''
Created on Jul 10, 2015

@author: david
'''
from django.utils.translation import ugettext_lazy as _
from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory
from dash_widgets import BaseWidgetSwitcherWidget
from forms import WidgetSwitcherForm
# *****************************************************************************
# ***************************** Base Image plugin *****************************
# *****************************************************************************
class BaseWidgetSwitcherPlugin(BaseDashboardPlugin):
    """
    Base WidgetSwitcher plugin.
    """
    name = _("WidgetSwitcher")
    group = _("WidgetSwitcher")
    form = WidgetSwitcherForm

# ********************************************************************************
# ********** Generating and registering the plugins using factory ****************
# ********************************************************************************
sizes = (
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (4, 3),
    (4, 4),
    (4, 5),
    (5, 3),
    (5, 4),
    (5, 5),
    (6, 3),
    (7, 7),
    (7, 13),
    (8, 8),
    (9, 9),
    (13, 7),
    (7, 13),
    (6, 5),
    (12, 7),
    (12, 8),
)

plugin_factory(BaseWidgetSwitcherPlugin, 'WidgetSwitcher', sizes)

# ********************************************************************************
# ********************************* Registering widgets **************************
# ********************************************************************************

# Registering chart plugin widgets
plugin_widget_factory(BaseWidgetSwitcherWidget, 'android', 'main', 'WidgetSwitcher', sizes)
plugin_widget_factory(BaseWidgetSwitcherWidget, 'windows8', 'main', 'WidgetSwitcher', sizes)
plugin_widget_factory(BaseWidgetSwitcherWidget, 'bootstrap2_fluid', 'main', 'WidgetSwitcher', sizes)
plugin_widget_factory(BaseWidgetSwitcherWidget, 'testing', 'main', 'WidgetSwitcher', sizes)
