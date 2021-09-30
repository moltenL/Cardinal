from django.conf.urls import url
from django.urls import path, include
from .views import (
    InitialApiView,
    CollectionDataRequestApiView,
    TestDataGeneratorApiView,
    api_docs,
    SupportedCollectionsApiView,
)

urlpatterns = [
    path("hello/", InitialApiView.as_view()),
    path("collection/<str:collection_name>/", CollectionDataRequestApiView.as_view()),
    path("supported-collections/", SupportedCollectionsApiView.as_view()),
    path("generate/<str:data_structure_type>/", TestDataGeneratorApiView.as_view()),
    path("", api_docs, name="index"),
]
