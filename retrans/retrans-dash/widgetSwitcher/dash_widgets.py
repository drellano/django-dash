'''
Created on Jul 10, 2015

@author: david
'''
from django.template.loader import render_to_string
from dash.base import BaseDashboardPluginWidget

# **********************************************************************
# ************************ Base Image URL widget plugin ********************
# **********************************************************************


class BaseWidgetSwitcherWidget(BaseDashboardPluginWidget):
    """
    Base widgetSwitcher plugin widget.
    """
    media_js = (
        'js/jquery.textfill.min.js',
    )
    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'width': self.get_width()-10,
            'height': self.get_height()-10,
            'timer': self.plugin.data.timer,
        }
        return render_to_string('widgetSwitcher/render.html', context)
