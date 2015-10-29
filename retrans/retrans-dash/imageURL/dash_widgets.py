'''
Created on Jul 10, 2015

@author: david
'''
from django.template.loader import render_to_string
from dash.base import BaseDashboardPluginWidget

# **********************************************************************
# ************************ Base Image URL widget plugin ********************
# **********************************************************************


class BaseImageURLWidget(BaseDashboardPluginWidget):
    """
    Base image plugin widget.
    """

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'width': self.get_width()-10,
            'height': self.get_height()-10,
            'image': self.plugin.data.image,
            'sizing': self.plugin.data.sizing,
        }
        return render_to_string('imageURL/render.html', context)
