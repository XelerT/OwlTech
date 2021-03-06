"""selfedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


from account.views import (
    register_view,
    login_view,
    logout_view,
    account_search_view,
)

# from products.views import (
#     creation_view,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('fizmat/', include('fizmat.urls')),
    path('news/', include('News.urls')),

    path('register', register_view, name="register"),
    path('logout', logout_view, name="logout"),
    path('login', login_view, name="login"),
    path('account/', include('account.urls', namespace='account')),
    path('search/', account_search_view, name="search"),


    # path('products', include('products.urls', namespace='products')),
    path('products', include('ProducT.urls', namespace='products')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('tinymce/', include('tinymce.urls')),

    path('password_change', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), name='password_change_done'),
    path('password_reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_change'),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

