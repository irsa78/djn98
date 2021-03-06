from django.urls import path
# from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView,\
#     PasswordResetConfirmView, PasswordResetCompleteView,TemplateView
from django.contrib.auth.views import  PasswordResetView, PasswordResetDoneView,\
    PasswordResetConfirmView, PasswordResetCompleteView,TemplateView,LoginView
from .views import LogoutView, RegisterView,baseView
from django.conf.urls import url
from .views import student_show
urlpatterns = [
    # path('home', HomePageView.as_view(), name='home'),
    path('home/',TemplateView.as_view(template_name='home.html'), name='home'),
    path('',baseView.as_view(),name='base'),
    path('base/', LogoutView.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login'),
    # login throuh gmail reset password
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    # # 
    # # gmail password reset
    # path('password_reset/done/', PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('password_reset/confirm/<uidb64>/<token>/',
    #      PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/complete/', PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    # path('profile/picture/', ImageUpdateView.as_view(), name='update_image'),
    # logout_request
    # path('logout/', logout_request.view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # path('index',student_show)
    path('index/',student_show, name = 'student_show'),
]
