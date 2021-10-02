from django.urls import path
from app.views import product_views as views


urlpatterns = [
    path('create/', views.CreateProduct.as_view(), name='create_product'),
    path('<int:pk>/detail', views.DetailProduct.as_view(), name='detail_product'),
    path('', views.ListProduct.as_view(), name='list_product'),
    path('<int:pk>/update', views.UpdateProduct.as_view(), name='update_product'),
    path('<int:pk>/delete', views.DeleteProduct.as_view(), name='delete_product')
]
