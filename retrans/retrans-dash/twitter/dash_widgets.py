'''
__author__ = 'David Arellano'
__date__ = '7/9/2015'
'''

from django.template.loader import render_to_string
from dash.base import BaseDashboardPluginWidget


class BaseTwitterWidget(BaseDashboardPluginWidget):
    """
    Twitter Widget.
    """
    media_js = (
                
    )

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'title': self.plugin.data.title,
            'width': self.get_width(),
            'height': self.get_height(),
        }
        return render_to_string('twitter/plugins/render.html', context)
