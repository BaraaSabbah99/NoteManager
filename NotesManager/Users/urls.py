
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
   path('register/',views.registeration,name='register'),
   path('login/',views.login,name='login'),
   path('logout/',views.logout,name='logout'),
   path('admin/',views.dashbored,name='admin'),
   path('admin/search/',views.search,name='search'),
   path('admin/deleteuser/<int:userId>',views.deleteuser,name='deleteuser'),

]
