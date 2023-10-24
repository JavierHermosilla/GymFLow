from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('register/', views.register),
    path('login/', views.LoginView.as_view()),
    path('Refresh/', TokenRefreshView.as_view()),
]

