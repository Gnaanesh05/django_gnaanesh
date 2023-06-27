from django.urls import path
from .import views

urlpatterns = [
    path('', views.IndexPage, name='Index'),
    path('home', views.Home, name='home'),
    path('loadlogin', views.loadLogin, name='loadlogin'),
    path('Alogin', views.adminlogin, name='Alogin'),
    path('delFood<int:fid>',views.delFoodConsume,name='delFood'),

]
