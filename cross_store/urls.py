from django.urls import path

from cross_store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('shop.html', views.shop, name="shop"),
    path('blog.html', views.blog, name="blog"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)