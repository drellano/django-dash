'''
Created on Jul 10, 2015

@author: david
'''
from django.utils.translation import ugettext_lazy as _
from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory
from dash_widgets import BaseImageLocalWidget
from forms import ImageLocalForm
from helpers import delete_file, clone_file
# *****************************************************************************
# ***************************** Base Image plugin *****************************
# *****************************************************************************
class BaseImageLocalPlugin(BaseDashboardPlugin):
    """
    Base imageURL plugin.
    """
    name = _("ImageLocal")
    group = _("Image")
    form = ImageLocalForm
    
    def delete_plugin_data(self):
        """
        Deletes uploaded file.
        """
        delete_file(self.data.image)

    def clone_plugin_data(self, dashboard_entry):
        """
        Clone plugin data, which means we make a copy of the original image.

        TODO: Perhaps rely more on data of `dashboard_entry`?
        """
        cloned_image = clone_file(self.data.image, relative_path=True)
        return self.get_cloned_plugin_data(update={'image': cloned_image})

# ********************************************************************************
# ********** Generating and registering the plugins using factory ****************
# ********************************************************************************
sizes = (
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
    (3, 4),
    (4, 3),
    (4, 4),
    (4, 5),
    (5, 4),
    (5, 5),
    (6, 3),
    (7, 7),
    (7, 13),
    (8, 8),
    (9, 9),
    (13, 7),
    (7, 13),
    (6, 5),
    (12, 7),
    (12, 8),
)

plugin_factory(BaseImageLocalPlugin, 'imageLocal', sizes)

# ********************************************************************************
# ********************************* Registering widgets **************************
# ********************************************************************************

# Registering chart plugin widgets
plugin_widget_factory(BaseImageLocalWidget, 'android', 'main', 'imageLocal', sizes)
plugin_widget_factory(BaseImageLocalWidget, 'windows8', 'main', 'imageLocal', sizes)
plugin_widget_factory(BaseImageLocalWidget, 'bootstrap2_fluid', 'main', 'imageLocal', sizes)
plugin_widget_factory(BaseImageLocalWidget, 'testing', 'main', 'imageLocal', sizes)
