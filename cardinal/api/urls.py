# todo/api/urls.py : API urls.py
from django.conf.urls import url
from django.urls import path, include
from .views import InitialApiView, DataRequestApiView

urlpatterns = [
    path("test/", InitialApiView.as_view()),

    # TODO: all, obj_tim, etc.
    path("all/", DataRequestApiView.as_view()),
]
