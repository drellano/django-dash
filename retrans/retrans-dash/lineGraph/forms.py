'''
__author__ = 'David Arellano'
__date__ = '7/9/2015'
'''

from django import forms
from django.utils.translation import ugettext_lazy as _
from dash.base import DashboardPluginFormBase


class LineGraphForm(forms.Form, DashboardPluginFormBase):
    """
    Chart form for `LineGraphPlugin` plugin.
    """

    plugin_data_fields = [
        ("title", ""),
        ("data", ""),
    ]

    title = forms.CharField(label=_("Title"), required=True)
    #data_test = "testtest"#update() #forms.CharField(label=_("Test"), required=True, widget=forms.widgets.Textarea)