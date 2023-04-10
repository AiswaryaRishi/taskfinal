from . import views
from django.urls import path
app_name='credentials'

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('dept',views.dept,name='dept'),
    path('details',views.details,name='details')
]