from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.func, name='main'),
    path('test', views.test),
    path('about', views.Extention, name='about'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


