from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
    path("sign_up/", views.sign_up, name="sign_up"),
    # path("login", views.login_request, name="login"),
    path('login/', views.LogInView.as_view(), name='login'),
    path("logout", views.logout_request, name= "logout"),

    path("password_reset", views.password_reset_request, name="password_reset"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/auth/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/auth/password_reset_complete.html'), name='password_reset_complete'),   
]