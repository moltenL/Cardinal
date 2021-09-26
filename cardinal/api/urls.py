from django.conf.urls import url
from django.urls import path, include
from .views import InitialApiView, DataRequestApiView, TestDataGeneratorApiView, api_docs

urlpatterns = [
    path("hello/", InitialApiView.as_view()),
    path("all/", DataRequestApiView.as_view()),
    path("generate/<str:data_structure_type>/", TestDataGeneratorApiView.as_view()),
    path('', api_docs, name='index'),
]
