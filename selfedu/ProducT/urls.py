from django.urls import path, include

from ProducT.views import (
    creation_view,
    main_view,
    # ProductsDetailView,
    detailed_view,
)

app_name = "product"

urlpatterns = [
    path('', main_view, name="main_view"),
    # path('<int:pk>', ProductsDetailView.as_view(), name="detailed_product"),
    path('/<int:pk>', detailed_view, name="detailed_product"),
    path('/create_product', creation_view, name="creation_view"),
    # path(r'^tinymce/', include('tinymce.urls')),
]
