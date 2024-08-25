from rest_framework import serializers
from .models import FibonacciNumber

class FibonacciNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FibonacciNumber
        fields = '__all__'