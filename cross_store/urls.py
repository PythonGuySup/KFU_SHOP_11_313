from django.urls import path

from cross_store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = "index" ),
    path('index', views.index, name = "index"),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)