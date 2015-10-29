from django import forms
from django.utils.translation import ugettext_lazy as _
from dash.base import DashboardPluginFormBase


class WidgetSwitcherForm(forms.Form, DashboardPluginFormBase):
    """
    Image form for `widgetSwitcher` plugin.
    """
    plugin_data_fields = [
        ("timer", ""),
    ]
    timer = forms.IntegerField(label=_("Timer in seconds"), required=True, initial=10)