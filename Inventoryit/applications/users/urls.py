from django.urls import path

from . import views

app_name= 'users_app'

urlpatterns = [
    path('register/',views.RegisterUserView.as_view(),name='register_user'),
    path('',views.LoginUserView.as_view(),name='login_user'),
    path('logout/',views.LogoutUserView.as_view(),name='logout_user'),
]