from django.urls import path, include
from .views import index

urlpatterns = [
    path('api/', include('cardinal.api.urls')),
    path('', index, name='index'),
]

