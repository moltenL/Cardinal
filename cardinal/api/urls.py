from django.conf.urls import url
from django.urls import path, include
from .views import InitialApiView, DataRequestApiView, TestDataGeneratorApiView
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("hello/", InitialApiView.as_view()),
    path("all/", DataRequestApiView.as_view()),
    path("generate/<str:data_structure_type>/", TestDataGeneratorApiView.as_view()),
    url(
        r'^openapi-schema',
        get_schema_view(
            title="Cardinal",
            description="Cardinal",
            version="1.0.0",
            public=True,
        ),
        name='openapi-schema',
    ),
    url(
        r'docs/',
        TemplateView.as_view(
            template_name='swagger-ui.html', extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui',
    ),
]
