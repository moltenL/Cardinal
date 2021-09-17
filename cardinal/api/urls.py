from django.conf.urls import url
from django.urls import path, include
from .views import InitialApiView, DataRequestApiView, TestDataGeneratorApiView

urlpatterns = [
    path("home/", InitialApiView.as_view()),
    # TODO: all, obj_tim, etc.
    path("all/", DataRequestApiView.as_view()),

    path("generate/<str:data_structure_type>/", TestDataGeneratorApiView.as_view()),
]
