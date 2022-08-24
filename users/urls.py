from django.urls import path
from . import views

urlpatterns = [
    path("users/register/", views.UserRegisterView.as_view()),
    path("users/login/", views.UserAuthToken.as_view()),
    path("users/<user_id>/", views.UserDetailView.as_view()),
    path("users/", views.UserView.as_view()),
]