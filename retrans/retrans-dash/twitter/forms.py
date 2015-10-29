'''
__author__ = 'David Arellano'
__date__ = '7/9/2015'
'''

from django import forms
from django.utils.translation import ugettext_lazy as _
from dash.base import DashboardPluginFormBase


class TwitterForm(forms.Form, DashboardPluginFormBase):
    """
    Form for `TwitterPlugin` plugin.
    """

    plugin_data_fields = [
        ("title", ""),
    ]

    title = forms.CharField(label=_("Title"), required=True)