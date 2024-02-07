from django.urls import path
from .views import registration, user_login, user_logout, user_profile, upload_avatar

urlpatterns = [
    path('user/registration/', registration, name='regist'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('upload_avatar/', upload_avatar, name='upload_avatar'),
]
