'''
__author__ = 'David Arellano'
__date__ = '7/9/2015'
'''

from django.template.loader import render_to_string
from dash.base import BaseDashboardPluginWidget


class BaseBarGraphWidget(BaseDashboardPluginWidget):
    """
    Bar Graph Widget.
    """
    media_js = (
        'js/rickshaw.min.js',
    )
    media_css = (
        'css/rickshaw.css',
    )

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'data': str(self.plugin.data.graph_data),
            'title': str(self.plugin.data.title),
            'width': self.get_width(),
            'height': self.get_height(),
        }
        return render_to_string('barGraph/plugins/render.html', context)
