from rest_framework import serializers

class PersonSerializers(serializers.Serializer):
    username = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()