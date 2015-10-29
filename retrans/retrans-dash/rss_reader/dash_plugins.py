__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseReadRSSFeedPlugin',)

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory
from forms import ReadRSSFeedForm
from dash_widgets import BaseReadRSSFeedWidget

# ********************************************************************************
# ********************************* Base Read RSS feed plugin ********************
# ********************************************************************************

class BaseReadRSSFeedPlugin(BaseDashboardPlugin):
    """
    Base Read RSS feed into HTML plugin.
    """
    name = _("Read RSS feed")
    form = ReadRSSFeedForm
    group = _("Internet")

# ********************************************************************************
# ********** Generating and registering the plugins using factory ****************
# ********************************************************************************
sizes = (
    (4, 2),
    (5, 2),
    (6, 2),
    (7, 2),
    (8, 2),
    (9, 2),
    (10, 2),
    (4, 3),
    (5, 3),
    (6, 3),
    (7, 3),
    (8, 3),
    (9, 3),
    (10, 3),

)

plugin_factory(BaseReadRSSFeedPlugin, 'read_rss_reader', sizes)

plugin_widget_factory(BaseReadRSSFeedWidget, 'android', 'main', 'read_rss_reader', sizes)
plugin_widget_factory(BaseReadRSSFeedWidget, 'windows8', 'main', 'read_rss_reader', sizes)
plugin_widget_factory(BaseReadRSSFeedWidget, 'bootstrap2_fluid', 'main', 'read_rss_reader', sizes)
plugin_widget_factory(BaseReadRSSFeedWidget, 'testing', 'main', 'read_rss_reader', sizes)