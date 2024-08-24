from rest_framework import serializers
from .models import MyUser, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'name', 'address', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Password should not be exposed in the API
        }

    def create(self, validated_data):
        # Create a new MyUser instance
        user = MyUser(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            address=validated_data['address'],
        )
        # Hash the password before saving it
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # Update a MyUser instance
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        
        # If password is provided, hash it before saving
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer to show user details
    user_id = serializers.PrimaryKeyRelatedField(queryset=MyUser.objects.all(), write_only=True, source='user')

    class Meta:
        model = Order
        fields = ['id', 'user', 'user_id', 'item_name', 'amount', 'created_at']
