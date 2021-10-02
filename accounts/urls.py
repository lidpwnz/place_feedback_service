from .views import RegisterView, ProfileView, UpdateUser, UpdatePassword
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', RegisterView.as_view(), name='register'),
    path('<int:pk>/profile', ProfileView.as_view(), name='profile'),
    path('<int:pk>/profile/update', UpdateUser.as_view(), name='update_user'),
    path('<int:pk>/profile/change_password', UpdatePassword.as_view(), name='change_password')
]
