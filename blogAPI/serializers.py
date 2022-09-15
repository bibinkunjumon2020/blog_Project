from rest_framework import serializers

class MobileSerializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    band = serializers.CharField()
    display = serializers.CharField()
    processor = serializers.CharField()
