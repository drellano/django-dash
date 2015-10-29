'''
__author__ = 'David Arellano'
__date__ = '7/9/2015'
'''

from django.template.loader import render_to_string
from dash.base import BaseDashboardPluginWidget
from update_widget import update_fuel_table

class BaseLineGraphWidget(BaseDashboardPluginWidget):
    """
    Line Graph Widget.
    """
    media_js = (
        'js/polychart2.standalone.js',
        'js/rickshaw.min.js',
    )

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'title': self.plugin.data.title,
            'data': str(self.plugin.data.data),
            'width': self.get_width(),
            'height': self.get_height(),
        }
        return render_to_string('lineGraph/plugins/render.html', context)
