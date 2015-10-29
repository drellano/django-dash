from django import forms
from django.utils.translation import ugettext_lazy as _
from dash.base import DashboardPluginFormBase
from helpers import handle_uploaded_file


class ImageLocalForm(forms.Form, DashboardPluginFormBase):
    """
    Image form for `ImageURLPlugin` plugin.
    """
    plugin_data_fields = [
        ("title", ""),
        ("image", ""),
        ("sizing", "")
    ]
    title = forms.CharField(label=_("Title"), required=False)
    image = forms.ImageField(label=_("Image"), required=True)
    sizing = forms.ChoiceField(label=_("Choose sizing option"), required=True, choices=([("contain", "Contain"),("fill", "Fill"),("cover", "Cover"),("none", "None"),("scale-Down", "Scale-down")]))
    
    def save_plugin_data(self, request=None):
        """
        Saving the plugin data and moving the file.
        """
        image = self.cleaned_data.get('image', None)
        if image:
            saved_image = handle_uploaded_file(image)
            self.cleaned_data['image'] = saved_image
