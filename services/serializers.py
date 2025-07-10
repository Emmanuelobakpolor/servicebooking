from rest_framework import serializers
from .models import Service, ServiceProvider

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    providers = ServiceProviderSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'
