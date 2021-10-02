from django.urls import path
from app.views import product_views
from app.views import feedback_views


urlpatterns = [
    path('create/', product_views.CreateProduct.as_view(), name='create_product'),
    path('<int:pk>/detail', product_views.DetailProduct.as_view(), name='detail_product'),
    path('', product_views.ListProduct.as_view(), name='list_product'),
    path('<int:pk>/update', product_views.UpdateProduct.as_view(), name='update_product'),
    path('<int:pk>/delete', product_views.DeleteProduct.as_view(), name='delete_product'),
    
    path('feedbacks/<int:product_id>/create', feedback_views.CreateFeedback.as_view(), name='create_feedback'),
    path('feedbacks/<int:pk>/update', feedback_views.UpdateFeedback.as_view(), name='update_feedback'),
    path('feedbacks/<int:pk>/delete', feedback_views.DeleteFeedback.as_view(), name='delete_feedback'),
]
