'''
Created on Jul 10, 2015

@author: david
'''
from django.template.loader import render_to_string
from dash.base import BaseDashboardPluginWidget
from django.conf import settings

# **********************************************************************
# ************************ Base Image URL widget plugin ********************
# **********************************************************************


class BaseImageLocalWidget(BaseDashboardPluginWidget):
    """
    Base image plugin widget.
    """

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
            'MEDIA_URL': settings.MEDIA_URL,
        }
        return render_to_string('imageLocal/render.html', context)
