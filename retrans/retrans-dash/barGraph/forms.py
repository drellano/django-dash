'''
__author__ = 'David Arellano'
__date__ = '7/9/2015'
'''

from django import forms
from django.utils.translation import ugettext_lazy as _
from dash.base import DashboardPluginFormBase
from defaults import DEFAULT_GRAPH_DATA, DEFAULT_TITLE


class BarGraphForm(forms.Form, DashboardPluginFormBase):
    """
    Chart form for `BarGraphPlugin` plugin.
    """

    plugin_data_fields = [
        ("title", DEFAULT_TITLE),
        ("graph_data", DEFAULT_GRAPH_DATA),
    ]

    title = forms.CharField(label=_("Title"), required=True, initial=DEFAULT_TITLE)
    graph_data = forms.CharField(label=_("Data"), required=True, widget=forms.widgets.Textarea, initial=DEFAULT_GRAPH_DATA)