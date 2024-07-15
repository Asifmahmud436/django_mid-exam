
from django.urls import path,include
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('register',views.register,name='register'),
    path('login',views.Login.as_view(),name='login'),
    # path('logout',views.user_logout.as_view(),name='logout'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('profile',views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
]
