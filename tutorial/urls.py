from django.urls import path
from django.conf.urls import include
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="Pastebin API")

urlpatterns = [
    path('', include('snippets.urls')),
    path('login/', include('rest_framework.urls')),
    path('schema/', schema_view),
]
