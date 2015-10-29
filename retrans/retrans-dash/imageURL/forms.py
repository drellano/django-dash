from django import forms
from django.utils.translation import ugettext_lazy as _
from dash.base import DashboardPluginFormBase


class ImageURLForm(forms.Form, DashboardPluginFormBase):
    """
    Image form for `ImageURLPlugin` plugin.
    """
    plugin_data_fields = [
        ("title", ""),
        ("image", ""),
        ("sizing", ""),
    ]
    title = forms.CharField(label=_("Title"), required=False)
    image = forms.CharField(label=_("Enter Image URL"), required=True)
    sizing = forms.ChoiceField(label=_("Choose sizing option"), required=True, choices=([("contain", "Contain"),("fill", "Fill"),("cover", "Cover"),("none", "None"),("scale-Down", "Scale-down")]))
