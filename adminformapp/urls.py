from django.urls import path
from  . import views
app_name='adminformapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('reg',views.reg,name='reg'),
    path('login',views.login,name='login'),

]