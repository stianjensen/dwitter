from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^id/(?P<dweet_id>[0-9]*)$', views.fullscreen_dweet, name='fullscreen_dweet'),
]
