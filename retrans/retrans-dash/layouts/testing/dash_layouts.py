'''
Created on Jul 14, 2015

@author: david
'''
from dash.base import BaseDashboardLayout, BaseDashboardPlaceholder
from dash.base import layout_registry

class DevMainPlaceholder(BaseDashboardPlaceholder):
    uid = 'main'  # Unique ID of the placeholder.
    cols = 19  # Number of columns in the placeholder.
    rows = 11  # Number of rows in the placeholder.
    cell_width = 100  # Width of a single cell in the placeholder.
    cell_height = 100  # Height of a single cell in the placeholder.


class DevLayout(BaseDashboardLayout):
    uid = 'testing'  # Layout UID.
    name = 'Dev'  # Layout name.

    # View template. Master template used in view mode.
    view_template_name = 'view_layout.html'

    # Edit template. Master template used in edit mode.
    edit_template_name = 'edit_layout.html'

    # All placeholders listed. Note, that placeholders are rendered in the
    # order specified here.
    placeholders = [DevMainPlaceholder]

    # Cell units used in the entire layout. Allowed values are: 'px', 'pt',
    # 'em' or '%'. In the ``ExampleMainPlaceholder`` cell_width is set to 150.
    #  It means that in this particular case its' actual width would be `150px`.
    cell_units = 'px'

    # Layout specific CSS.
    media_css = ('css/dash_layout_dev.css', 'css/dash_solid_borders.css')

    # Layout specific JS.
    media_js = ('js/dash_layout_dev.js',)

# Registering the layout.
layout_registry.register(DevLayout)
