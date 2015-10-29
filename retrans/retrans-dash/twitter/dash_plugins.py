'''
__author__ = 'David Arellano'
__date__ = '7/9/2015'
'''

from django.utils.translation import ugettext_lazy as _
from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory
from dash_widgets import BaseTwitterWidget
from forms import TwitterForm

class BaseTwitterPlugin(BaseDashboardPlugin):

    name = _("Twitter")
    group = _("Internet")
    form = TwitterForm

# ********************************************************************************
# ********** Generating and registering the plugins using factory ****************
# ********************************************************************************
sizes = (
    (6, 3),
)

plugin_factory(BaseTwitterPlugin, 'twitter', sizes)

# ********************************************************************************
# ********************************* Registering widgets **************************
# ********************************************************************************

# Registering chart plugin widgets
plugin_widget_factory(BaseTwitterWidget, 'android', 'main', 'twitter', sizes)
plugin_widget_factory(BaseTwitterWidget, 'windows8', 'main', 'twitter', sizes)
plugin_widget_factory(BaseTwitterWidget, 'bootstrap2_fluid', 'main', 'twitter', sizes)
plugin_widget_factory(BaseTwitterWidget, 'testing', 'main', 'twitter', sizes)
