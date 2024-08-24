from django.urls import path
from .views import UserListCreate, UserDetail, OrderListCreate, OrderDetail

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<uuid:pk>/', UserDetail.as_view(), name='user-detail'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<uuid:pk>/', OrderDetail.as_view(), name='order-detail'),
]
