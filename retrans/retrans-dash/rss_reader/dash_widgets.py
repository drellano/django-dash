__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseReadRSSFeedWidget', 'ReadRSSFeed2x3Widget', 'ReadRSSFeed3x3Widget')

from django.core.context_processors import csrf
from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ************************************************************************
# ****************** Android widgets for Read RSS feed plugin ************
# ************************************************************************

class BaseReadRSSFeedWidget(BaseDashboardPluginWidget):
    """
    Base read RSS feed plugin widget.
    """
    media_js = (
        'js/jquery.textfill.min.js',
    )

    def render(self, request=None):    
        context = {'plugin': self.plugin, 'csrfmiddlewaretoken': csrf(request)}
        return render_to_string('rss_reader/render.html', context)

