from rest_framework import serializers
from productsapi.models import ProductItems
from django.contrib.auth.models import User # imported model
class MySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    price = serializers.IntegerField()
    rating = serializers.IntegerField()
    category = serializers.CharField()
    description = serializers.CharField()

    def validate(self, data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("No negative Price baby")
        return data

class ModelSerializer(serializers.ModelSerializer):
    # id = serializers.CharField(read_only=True)
    class Meta:
        model = ProductItems
        fields = "__all__"  # very careful about spellings
        # Or I can write fields=["id",name",..etc]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)