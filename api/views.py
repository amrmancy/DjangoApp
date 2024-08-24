from rest_framework import generics
from .models import MyUser, Order
from .serializers import UserSerializer, OrderSerializer

# User Views

class UserListCreate(generics.ListCreateAPIView):
    """
    Handles listing all users and creating a new user.
    GET: Returns a list of all users.
    POST: Creates a new user.
    """
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single user.
    GET: Retrieves a single user by ID.
    PUT/PATCH: Updates the user details.
    DELETE: Deletes the user.
    """
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

# Order Views

class OrderListCreate(generics.ListCreateAPIView):
    """
    Handles listing all orders and creating a new order.
    GET: Returns a list of all orders.
    POST: Creates a new order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single order.
    GET: Retrieves a single order by ID.
    PUT/PATCH: Updates the order details.
    DELETE: Deletes the order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
