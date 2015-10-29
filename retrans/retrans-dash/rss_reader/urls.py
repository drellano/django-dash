from django.conf.urls import patterns, url

import views

urlpatterns = patterns('retrans.retrans-dash.rss_reader.views',
    url(r'^get_feed/(?P<layout_uid>[\w_]+)/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/$', \
        view='get_feed', name='rss_reader.get_feed'),
)
