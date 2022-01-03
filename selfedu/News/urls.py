from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.News, name='news_home'),
    path('create', views.Create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
