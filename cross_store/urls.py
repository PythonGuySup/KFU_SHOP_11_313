from django.urls import path
from cross_store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('shop', views.shop, name="shop"),
    path('shop/<int:page>', views.shop, name="shop_with_page"),
    path('blog.html', views.blog, name="blog"),
    path('private-office.html', views.private_office, name="private-office"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
