from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/add_item/', views.add_item, name='add_item'),
    path('registration/', views.registration, name='reg'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
